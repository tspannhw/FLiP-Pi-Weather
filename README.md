## FLiP-Pi-Weather
### FLiP-Py



### Run

````
2022-02-23 08:15:26.720 INFO  [3069356416] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-02-23 08:15:26.720 INFO  [3069356416] ConnectionPool:96 | Created connection for pulsar://pulsar1:6650
2022-02-23 08:15:26.726 INFO  [3032564800] ClientConnection:368 | [192.168.1.203:41680 -> 192.168.1.230:6650] Connected to broker
2022-02-23 08:15:26.729 INFO  [3032564800] HandlerBase:64 | [persistent://public/default/pi-weather, ] Getting connection from pool
2022-02-23 08:15:26.731 INFO  [3032564800] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-02-23 08:15:26.731 INFO  [3032564800] ConnectionPool:96 | Created connection for pulsar://127.0.0.1:6650
2022-02-23 08:15:26.735 INFO  [3032564800] ClientConnection:370 | [192.168.1.203:41682 -> 192.168.1.230:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
2022-02-23 08:15:26.747 INFO  [3032564800] ProducerImpl:189 | [persistent://public/default/pi-weather, ] Created producer on broker [192.168.1.203:41682 -> 192.168.1.230:6650] 
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_vrk_20220223131526', 'ipaddress': '192.168.1.203', 'cputempf': 108, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645622126.9427075', 'te': '0.0004260540008544922', 'cpu': 0.0, 'diskusage': '106175.0 MB', 'memory': 25.5, 'rowid': '20220223131526_117bbc3e-2cdc-46b2-9d5c-ac4fae4eaa46', 'systemtime': '02/23/2022 08:15:27', 'ts': 1645622127, 'starttime': '02/23/2022 08:15:26', 'pressure': 693.07, 'temperature': 59.0, 'humidity': 79.2, 'devicetemperature': 73.0, 'dewpoint': 18.57, 'lux': 323.45}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_jet_20220223131527', 'ipaddress': '192.168.1.203', 'cputempf': 109, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645622127.9905956', 'te': '0.0008008480072021484', 'cpu': 0.2, 'diskusage': '106175.0 MB', 'memory': 25.5, 'rowid': '20220223131527_99a38f64-54a4-4dd3-a0af-95bdadf4e0be', 'systemtime': '02/23/2022 08:15:28', 'ts': 1645622128, 'starttime': '02/23/2022 08:15:27', 'pressure': 1010.22, 'temperature': 78.0, 'humidity': 20.14, 'devicetemperature': 92.0, 'dewpoint': 17.26, 'lux': 161.01}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_vqi_20220223131529', 'ipaddress': '192.168.1.203', 'cputempf': 111, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645622129.0391476', 'te': '0.0007567405700683594', 'cpu': 0.2, 'diskusage': '106175.0 MB', 'memory': 25.5, 'rowid': '20220223131529_76ea6c35-6351-42dd-854e-9671fec018d9', 'systemtime': '02/23/2022 08:15:30', 'ts': 1645622130, 'starttime': '02/23/2022 08:15:29', 'pressure': 1010.23, 'temperature': 78.0, 'humidity': 20.14, 'devicetemperature': 92.0, 'dewpoint': 17.26, 'lux': 163.67}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_nbt_20220223131530', 'ipaddress': '192.168.1.203', 'cputempf': 109, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645622130.0832412', 'te': '0.000690460205078125', 'cpu': 0.0, 'diskusage': '106175.0 MB', 'memory': 25.4, 'rowid': '20220223131530_cc4b7659-9632-4422-9fed-46c3d28a9356', 'systemtime': '02/23/2022 08:15:31', 'ts': 1645622131, 'starttime': '02/23/2022 08:15:30', 'pressure': 1010.23, 'temperature': 78.0, 'humidity': 20.12, 'devicetemperature': 92.0, 'dewpoint': 17.26, 'lux': 163.67}
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_dxk_20220223131531', 'ipaddress': '192.168.1.203', 'cputempf': 108, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645622131.1316664', 'te': '0.0007994174957275391', 'cpu': 0.2, 'diskusage': '106175.0 MB', 'memory': 25.4, 'rowid': '20220223131531_ea2ae348-eaea-4871-8359-a8aec97fb0d0', 'systemtime': '02/23/2022 08:15:32', 'ts': 1645622132, 'starttime': '02/23/2022 08:15:31', 'pressure': 1010.23, 'temperature': 78.0, 'humidity': 20.11, 'devicetemperature': 92.0, 'dewpoint': 17.26, 'lux': 161.89}

````


### Avro

````
pip3 install fastavro
pip3 install pytz
pip3 install pulsar-client[avro]


bin/pulsar-client consume "persistent://public/default/pi-weather-avro" -s "weatherpavroi" -n 0

````

### Example Avro Run

````

root@weather:/opt/demo# python3 weatheravro.py 
Schema info is: {
 "type": "record",
 "name": "weather",
 "fields": [
  {
   "name": "uuid",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "ipaddress",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "cputempf",
   "type": [
    "null",
    "int"
   ]
  },
  {
   "name": "runtime",
   "type": [
    "null",
    "int"
   ]
  },
  {
   "name": "host",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "hostname",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "macaddress",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "endtime",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "te",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "cpu",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "diskusage",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "memory",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "rowid",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "systemtime",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "ts",
   "type": [
    "null",
    "int"
   ]
  },
  {
   "name": "starttime",
   "type": [
    "null",
    "string"
   ]
  },
  {
   "name": "pressure",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "temperature",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "humidity",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "devicetemperature",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "dewpoint",
   "type": [
    "null",
    "float"
   ]
  },
  {
   "name": "lux",
   "type": [
    "null",
    "float"
   ]
  }
 ]
}
2022-02-23 09:57:59.515 INFO  [3069385088] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-02-23 09:57:59.515 INFO  [3069385088] ConnectionPool:96 | Created connection for pulsar://pulsar1:6650
2022-02-23 09:57:59.521 INFO  [3030217792] ClientConnection:368 | [192.168.1.203:41708 -> 192.168.1.230:6650] Connected to broker
2022-02-23 09:57:59.524 INFO  [3030217792] HandlerBase:64 | [persistent://public/default/pi-weather-avro, ] Getting connection from pool
2022-02-23 09:57:59.527 INFO  [3030217792] ClientConnection:182 | [<none> -> pulsar://pulsar1:6650] Create ClientConnection, timeout=10000
2022-02-23 09:57:59.527 INFO  [3030217792] ConnectionPool:96 | Created connection for pulsar://127.0.0.1:6650
2022-02-23 09:57:59.531 INFO  [3030217792] ClientConnection:370 | [192.168.1.203:41710 -> 192.168.1.230:6650] Connected to broker through proxy. Logical broker: pulsar://127.0.0.1:6650
2022-02-23 09:57:59.538 INFO  [3030217792] ProducerImpl:189 | [persistent://public/default/pi-weather-avro, ] Created producer on broker [192.168.1.203:41710 -> 192.168.1.230:6650] 
{'_required_default': False, '_default': None, '_required': False, 'uuid': 'wthr_fxx_20220223145759', 'ipaddress': '192.168.1.203', 'cputempf': 109, 'runtime': 0, 'host': 'weather', 'hostname': 'weather', 'macaddress': 'e4:5f:01:8f:3f:6b', 'endtime': '1645628279.7329316', 'te': '0.0004296302795410156', 'cpu': 0.0, 'diskusage': '106163.7 MB', 'memory': 25.5, 'rowid': '20220223145759_461ff2f9-3efc-4392-95fa-660ebdae884a', 'systemtime': '02/23/2022 09:58:00', 'ts': 1645628280, 'starttime': '02/23/2022 09:57:59', 'pressure': 693.07, 'temperature': 59.0, 'humidity': 79.2, 'devicetemperature': 73.0, 'dewpoint': 18.57, 'lux': 173.08}
^C2022-02-23 09:58:01.364 INFO  [3069385088] ClientImpl:495 | Closing Pulsar client with 1 producers and 0 consumers
2022-02-23 09:58:01.364 INFO  [3069385088] ProducerImpl:686 | [persistent://public/default/pi-weather-avro, standalone-1-2227] Closing producer for topic persistent://public/default/pi-weather-avro
2022-02-23 09:58:01.367 INFO  [3030217792] ProducerImpl:729 | [persistent://public/default/pi-weather-avro, standalone-1-2227] Closed producer
2022-02-23 09:58:01.368 INFO  [3030217792] ClientConnection:1548 | [192.168.1.203:41710 -> 192.168.1.230:6650] Connection closed
2022-02-23 09:58:01.368 INFO  [3030217792] ClientConnection:1548 | [192.168.1.203:41708 -> 192.168.1.230:6650] Connection closed
2022-02-23 09:58:01.407 INFO  [3069385088] ProducerImpl:655 | Producer - [persistent://public/default/pi-weather-avro, standalone-1-2227] , [batching  = off]
2022-02-23 09:58:01.408 INFO  [3069385088] ClientConnection:256 | [192.168.1.203:41708 -> 192.168.1.230:6650] Destroyed connection
2022-02-23 09:58:01.408 INFO  [3069385088] ClientConnection:256 | [192.168.1.203:41710 -> 192.168.1.230:6650] Destroyed connection

2022-02-23T09:55:26,224-0500 [pulsar-client-io-1-1] INFO  com.scurrilous.circe.checksum.Crc32cIntChecksum - SSE4.2 CRC32C provider initialized
----- got message -----
key:[wthr_sqq_20220223145525], properties:[], content:.wthr_sqq_20220223145525?192.168.1.203???weatherweather"e4:5f:01:8f:3f:6b$1645628125.1793094,0.00042438507080078125106163.7 MB?????????Af20220223145525_431e1982-36cd-4d04-b24b-a9213bfc67d0&02/23/2022 09:55:26????????????
                                                                                                               &02/23/2022 09:55:25{D-DlBff???B???B\??????A
````


#### Pulsar SQL

````

use pulsar."public/default";

show tables;

describe "pi-weather";
      Column       |   Type    | Extra |                                   Comment                                   
-------------------+-----------+-------+-----------------------------------------------------------------------------
 uuid              | varchar   |       | ["null","string"]                                                           
 ipaddress         | varchar   |       | ["null","string"]                                                           
 cputempf          | integer   |       | ["null","int"]                                                              
 runtime           | integer   |       | ["null","int"]                                                              
 host              | varchar   |       | ["null","string"]                                                           
 hostname          | varchar   |       | ["null","string"]                                                           
 macaddress        | varchar   |       | ["null","string"]                                                           
 endtime           | varchar   |       | ["null","string"]                                                           
 te                | varchar   |       | ["null","string"]                                                           
 cpu               | real      |       | ["null","float"]                                                            
 diskusage         | varchar   |       | ["null","string"]                                                           
 memory            | real      |       | ["null","float"]                                                            
 rowid             | varchar   |       | ["null","string"]                                                           
 systemtime        | varchar   |       | ["null","string"]                                                           
 ts                | integer   |       | ["null","int"]                                                              
 starttime         | varchar   |       | ["null","string"]                                                           
 pressure          | real      |       | ["null","float"]                                                            
 temperature       | real      |       | ["null","float"]                                                            
 humidity          | real      |       | ["null","float"]                                                            
 devicetemperature | real      |       | ["null","float"]                                                            
 dewpoint          | real      |       | ["null","float"]                                                            
 lux               | real      |       | ["null","float"]                                                            
 __partition__     | integer   |       | The partition number which the message belongs to                           
 __event_time__    | timestamp |       | Application defined timestamp in milliseconds of when the event occurred    
 __publish_time__  | timestamp |       | The timestamp in milliseconds of when event as published                    
 __message_id__    | varchar   |       | The message ID of the message used to generate this row                     
 __sequence_id__   | bigint    |       | The sequence ID of the message used to generate this row                    
 __producer_name__ | varchar   |       | The name of the producer that publish the message used to generate this row 
 __key__           | varchar   |       | The partition key for the topic                                             
 __properties__    | varchar   |       | User defined properties                                                     
(30 rows)
 
select * from pulsar."public/default"."pi-weather";

          uuid           |   ipaddress   | cputempf | runtime |  host   | hostname |    macaddress     |      endtime       |           te  
-------------------------+---------------+----------+---------+---------+----------+-------------------+--------------------+---------------
 wthr_jxm_20220415200425 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053065.5075643 | 0.000751972198
 wthr_jrg_20220415200426 | 192.168.1.203 |      105 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053066.5556061 | 0.000745296478
 wthr_pya_20220415200427 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053067.7026055 | 0.000663518905
 wthr_lxx_20220415200428 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053068.751889  | 0.000751972198
 wthr_nrf_20220415200429 | 192.168.1.203 |      108 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053069.7996137 | 0.000750780105
 wthr_gxo_20220415200430 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053070.846855  | 0.000739574432
 wthr_uxp_20220415200431 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053071.8950646 | 0.000780105590
 wthr_gia_20220415200432 | 192.168.1.203 |      105 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053072.9443476 | 0.000747919082
 wthr_pum_20220415200433 | 192.168.1.203 |      105 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053073.9923508 | 0.000739574432
 wthr_yas_20220415200435 | 192.168.1.203 |      107 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053075.041469  | 0.000785827636
 wthr_gaf_20220415200436 | 192.168.1.203 |      106 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053076.0893412 | 0.000747442245
 wthr_xxq_20220415200437 | 192.168.1.203 |      107 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053077.1381607 | 0.000740051269
 wthr_xxw_20220415200438 | 192.168.1.203 |      107 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053078.186877  | 0.000748157501
 wthr_djv_20220415200439 | 192.168.1.203 |      107 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053079.235591  | 0.000744581222
 wthr_urp_20220415200440 | 192.168.1.203 |      108 |       0 | weather | weather  | e4:5f:01:8f:3f:6b | 1650053080.2825677 | 0.000787973403
 
 select pressure, temperature , humidity , devicetemperature , dewpoint ,lux , uuid, cputempf, "__message_id__" , 
       endtime  
from pulsar."public/default"."pi-weather"


````
