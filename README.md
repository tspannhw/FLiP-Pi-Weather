## FLiP-Pi-Weather




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
