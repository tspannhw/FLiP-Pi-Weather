import time
import weatherhat
import pulsar
import logging
import sys
import datetime
import subprocess
import os
import traceback
import math
import base64
import json
from time import gmtime, strftime
import random, string
import time
import psutil
import uuid
from time import sleep
from math import isnan
from subprocess import PIPE, Popen
import socket
from pulsar.schema import *
import ST7789
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import ManropeBold as UserFont

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/

class weather(Record):
    uuid = String()
    ipaddress = String()
    cputempf = Integer()
    runtime = Integer()
    host = String()
    hostname = String()
    macaddress = String()
    endtime = String()
    te = String()
    cpu = Float()
    diskusage = String()
    memory = Float()
    rowid = String()
    systemtime = String()
    ts = Integer()
    starttime = String()
    pressure = Float()
    temperature = Float()
    humidity = Float()
    devicetemperature = Float()
    dewpoint = Float()
    lux = Float()

# IP Address
def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address
# Random Word
def randomword(length):
 return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()) for i in range(length))

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET
# Timer
packet_size=3000

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipaddress = IP_address()

client = pulsar.Client('pulsar://pulsar1:6650')

producer = client.create_producer(topic='persistent://public/default/pi-weather' ,schema=JsonSchema(weather),properties={"producer-name": "weather-py-sensor","producer-id": "weather-sensor" })

sensor = weatherhat.WeatherHAT()

SPI_SPEED_MHZ = 80

# Create LCD class instance.
disp = ST7789.ST7789(
    rotation=90,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000
)

# Initialize display.
disp.begin()

# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

# New canvas to draw on.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Text settings.
font_size = 30
font = ImageFont.truetype(UserFont, font_size)
text_colour = (255, 255, 255)
back_colour = (0, 170, 170)


try:
    while True:
        sensor.update(interval=60.0)

        # wind_direction_cardinal = sensor.degrees_to_cardinal(sensor.wind_direction)

        currenttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        starttime = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        start = time.time()

        # Create unique id
        uniqueid = 'wthr_{0}_{1}'.format(randomword(3),strftime("%Y%m%d%H%M%S",gmtime()))
        uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())

        # CPU Temp
        f = open("/sys/devices/virtual/thermal/thermal_zone0/temp","r")
        cputemp = str( f.readline() )
        cputemp = cputemp.replace('\n','')
        cputemp = cputemp.strip()
        cputemp = str(round(float(cputemp)) / 1000)
        cputempf = str(round(9.0/5.0 * float(cputemp) + 32))
        f.close()

        devicetemp = sensor.device_temperature
        tempc = sensor.temperature
        devicetempf = str(round(9.0/5.0 * float(devicetemp) + 32))
        tempcf = str(round(9.0/5.0 * float(tempc) + 32))

        usage = psutil.disk_usage("/")
        end = time.time()

        weatherRec = weather()
        weatherRec.uuid = uniqueid
        weatherRec.ipaddress = ipaddress
        weatherRec.cputempf = int(cputempf)
        weatherRec.runtime =  int(round(end - start))
        weatherRec.host = os.uname()[1]
        weatherRec.hostname = host_name
        weatherRec.macaddress = psutil_iface('wlan0')
        weatherRec.endtime = '{0}'.format( str(end ))
        weatherRec.te = '{0}'.format(str(end-start))
        weatherRec.cpu = psutil.cpu_percent(interval=1)
        weatherRec.diskusage = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
        weatherRec.memory = psutil.virtual_memory().percent
        weatherRec.rowid = str(uuid2)
        weatherRec.systemtime = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        weatherRec.ts =  int( time.time() )
        weatherRec.starttime = str(starttime)
        weatherRec.pressure = round(sensor.pressure,2)
        weatherRec.temperature = round(float(tempcf),2)
        weatherRec.humidity = round(float(sensor.humidity),2)
        weatherRec.devicetemperature = round(float(devicetempf),2)
        weatherRec.dewpoint =  round(float(sensor.dewpoint),2)
        weatherRec.lux = round(float(sensor.lux),2)
        print(weatherRec)
        producer.send(weatherRec,partition_key=uniqueid)
        message = "W:" + str(weatherRec.temperature) + ":" + str(weatherRec.humidity);
        size_x, size_y = draw.textsize(message, font)
        x = (WIDTH - size_x) / 2
        y = (HEIGHT / 2) - (size_y / 2)
        draw.rectangle((0, 0, WIDTH, HEIGHT), back_colour)
        draw.text((x, y), message, font=font, fill=text_colour)
        disp.display(img)

except KeyboardInterrupt:
    pass

disp.set_backlight(0)
client.close()
