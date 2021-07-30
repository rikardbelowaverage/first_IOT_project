# Tutorial Build a portable weather station with Pycom LoPy4
#### By Rikard Johansson, rj222pj
###### Tags: `Weather Station, IoT, LNU, LoPy4, Pycom`

## :memo: Summarized project overview

This project describes how to create a IoT-device which monitors the air quality and temperature of your home. This involves some light tinkering and just a pinch of programming. Following this guide will probably take about 2-3 hours but someone with experience could complete the project in under an hour. 

Tutorial describes how to create an IoT package which measures humidity and temperature at given location. Project includes basic programming, wiring and data transportation setup. An approximation for completing project would be 3 hours, some variance depending on previous experience and pre-installed programs.

## :bulb: Why this project
There are a couple of reasons for why this became the chosen project, recently the home-thermometer broke. With this summers hot temperatures and no temperature measurement it became the obvious choice. Main purpose of project was learning basics of IoT : how data goes from measured to visualized.
Future plans involves installation of CO2 and air pressure sensors, which would give the weather station possibility to monitor:
- Temperature
- Humidity
- Air pressure
- CO2 concentration

## :microscope: Bill of Materials

| Material            | Purchase here           |
| -----------------   |:----------------------- |
|LoPy4 Basic Bundle, 849:- | [:credit_card:][Electrokit_LoPy] |
|Battery LiPo 3.7V 4400mAh, 249:- | [:credit_card:][Electrokit_Battery] |
|Sensor kit – 25 modules, 299:- | [:credit_card:][Electrokit_Sensors] |
|Digital temperature and humidity sensor DHT11, 49:- | [:credit_card:][Electrokit_DHT] |

[Electrokit_LoPy]: https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-basic-bundle/
[Electrokit_Sensors]: https://www.electrokit.com/produkt/sensor-kit-26-moduler/
[Electrokit_DHT]: https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/
[Electrokit_Battery]: https://www.electrokit.com/produkt/batteri-lipo-3-7v-4400mah/

*Note : prices are from 29/07-2021*

LoPy4 board with its ease of use of LoRaWAN makes it a good choice for this type of project.

## :computer: Computer setup
__Note:__ For complete code, please look into python files in repository.
This tutorial was done using Windows 10, there should be no problems using another operating system. However, the procedures may differ.

### Steps:
1. It is recommended to update the firmware of the expansion board, the board used in tutorial had latest firmware. Guide for upgrading board is available [here][flash].
2. Connect the LoPy4 and expansion board together, make sure both cards are oriented with pycom text in same orientation. Then connect the LoPy4 package to a computer via USB-cable.
3. If you are using an older version of Windows you may need to install drivers, for more information click [here][windows_drivers].
4. Similar to the expansion board it may be needed to upgrade the firmware of the LoPy4, guides for upgrading LoPy4 are available [here][flash]
5. For working with the LoPy board use one of the following IDE's : [Atom][atom_link] or [Visual Studio Code][vsc_link]. Start the IDE when done with the installation, then install the pymakr plug-in. __Note__: [node.js][nodejs_link] is mandatory for running pymakr.
6. Please make sure installation is correct by trying one of the following [basic examples][basic_examples] from pycom.
7. As seen in basic examples from step 6, code is written in pymakr extension and then flashed to LoPy4 device.

[flash]:https://docs.pycom.io/updatefirmware/
[windows_drivers]:https://docs.pycom.io/gettingstarted/software/drivers/
[atom_link]:https://flight-manual.atom.io/getting-started/sections/installing-atom/
[vsc_link]:https://code.visualstudio.com/docs/setup/setup-overview
[nodejs_link]:https://nodejs.org/en/
[basic_examples]:https://docs.pycom.io/tutorials/basic/rgbled/

## :hammer: Putting everything together
![](https://i.ibb.co/jWDVBJ7/wiring.jpg)
## :anchor: Platform

## :mag_right: The code
As mentioned earlier complete code is available in repository, complete code also includes comments and explanation.

- Code:
```python
import time
import socket
import machine
import pycom
import struct
from machine import Pin
from dht import DHT

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

while(True):
    result = th.read()
    
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
        
    temperature = result.temperature
    humidity = result.humidity
    
    payload = struct.pack('>hB', int(temperature * 100), int(humidity))
    s.send(payload)
    
    pycom.rgbled(0x00ff00)
    time.sleep(1)
    pycom.heartbeat(False)
    
    ms_to_minutes = 1000*60
    snooze_timer = 15
    lora.nvram_save()
    machine.deepsleep(ms_to_minutes*snooze_timer)

```

## :helicopter: Transmitting the data / connectivity
In the code example data is transmitted from the sensor once every 10th minute. However, to manage battery-longevity versus resolution set the interval to appropriate value.
Measurement data is transmitted using LoRa, reason for not using e.g. Wi-Fi is to maximize lifetime of the battery and increasing range of where device can be used. This was done in Gothenburg, where [Helium][helium_map] and [The Things Network][ttn_map] coverage is available. During the start of the project TTN was used, there were reliability with the connectivity for TTN, therefore Heliums LoRaWAN network was used instead.
Helium provides a starting credit of 10,000 data credits which would be equivalent to transmitting 240.000 bytes through their network.
Data is recieved in Helium console then forwarded to Ubidots and Datacake using built in HTTP-integrations, the data package also referred to as payload is decoded in both applications. To increase the number of variables that would be transferred one must update the payload decoder, below are examples of how different [data structures][data_structures] can be decoded:
```python
decoded_payload['temperature'] = (bytes[0] << 24 >> 16 | bytes[1]) / 100
decoded_payload['humidity'] = (bytes[2])
#decoded_payload['pressure'] = (bytes[3])
``` 
Data from code is packaged accordingly :
```python
    temperature = XX
    humidity = XX
    payload = struct.pack('>hB', int(temperature * 100), int(humidity))
    s.send(payload)
```


[helium_map]:https://explorer.helium.com/hotspots/hex/881f250699fffff
[ttn_map]:https://www.thethingsnetwork.org/map
[data_structures]:https://docs.python.org/3/library/struct.html



## Presenting the data

## Finalizing the design



