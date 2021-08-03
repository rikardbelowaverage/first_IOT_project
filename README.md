# Tutorial : Build a portable weather station with Pycom LoPy4
#### By Rikard Johansson, rj222pj
###### Tags: `Weather Station, IoT, LNU, LoPy4, Pycom`

## :memo: Summarized Project Overview

Tutorial describes how to create an IoT-device that measures humidity and temperature at given location. Project includes basic programming, wiring and data transportation. An approximation for completing project would be 3 hours, depending on previous experience and how many programs are pre-installed on used PC.

## :bulb: Why This Project
There are a couple of reasons for why this became the chosen project, recently the home-thermometer broke. With this hot summer one must have some temperature measurement. Main purpose of project was learning basics of IoT : how data goes from measured to visualized, how LoPy/Arduino-type boards interact with sensors, energy consumption and data transfer costs.

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

*Note : Pick Sensor kit for more optionalities or DHT sensor for pricing, prices are from 29/07-2021*

| __DHT sensor__            | Specifications         |
| -----------------   |:----------------------- |
|Operating Voltage | 3.3V to 5.5V |
|Humidity range	 | 20% to 90% RH | 
|Humidity accuracy |	±5% RH |
|Humidity resolution |	1% RH |
|Temperature range |	0ºC to 50ºC [32ºF to 122ºF] |
|Temperature accuracy |	±2ºC |
|Temperature resolution | 1ºC |

LoPy4 board with its ease of use of LoRaWAN makes it a good choice for this type of project. For this project everything was purchased as a bundle from a previous student, the bundle included 25 sensor-kit and the LoPy4.


## :computer: Computer Setup
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
8. In the Pymakr plug-in there are five possibilities to interact with device on left hand side. From top to bottom they are : connecting or disconnect the communication port, run selected file, upload project to device and download from device. Not included in the picture is also a possibility to get device info.


![](https://i.imgur.com/SR4XOtX.png=100x100)

[flash]:https://docs.pycom.io/updatefirmware/
[windows_drivers]:https://docs.pycom.io/gettingstarted/software/drivers/
[atom_link]:https://flight-manual.atom.io/getting-started/sections/installing-atom/
[vsc_link]:https://code.visualstudio.com/docs/setup/setup-overview
[nodejs_link]:https://nodejs.org/en/
[basic_examples]:https://docs.pycom.io/tutorials/basic/rgbled/

## :hammer: Putting everything together
In the earlier phase of the project there were several sensors connected, therefore it was easier using a breadbord.
After going back and forward regarding power and data-consumption the only sensor used was the [DHT11-sensor][DHT11_spec].
The DHT11 sensor contains a humidity sensing component and one temperature sensor thermistor. For higher accuracy the [DHT22-sensor][DHT22_spec] is a good option, the cost is about twice as high at approximate 100:- compared to the DHT11 at 49:-. 

[DHT11_spec]:https://www.electrokit.com/uploads/productfile/41015/DHT11.pdf
[DHT22_spec]:https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf
![](https://i.ibb.co/jWDVBJ7/wiring.jpg)

The DHT sensor requires 3.3V so there is no need to use any resistors when powered by the LoPy. This project did not use any casing, for production one could consider [IP-classed casing][pycase] depending on what environment the IoT-device would be placed in.

[pycase]:https://pycom.io/product/universal-ip67-case/

| __DHT sensor__            | Conditions         | Minimum | Typical | Maximum |
| -----------------   |:---------------  |:-------------  |:-------------- |:--------------- |
| Power Supply    | DC         | 3V | 5V | 5.5V |
| Current Supply  | Measuring  | 0.5mA |  | 2.5mA |
|                 | Average    | 0.2mA |  | 1mA |
|                 | Standby | 100uA |  | 150uA |
| Sampling period | Second     | 1 |  |  |

*Note: Sampling period at intervals should be no less than 1 second.*

For this project, measurement is done four times per hour.
Measuring cost : 3.3V × 2.5mA = 0.00825 watts while measuring.
Standby cost : 3.3V × 150uA = 0.000495 watts while sleeping.

To be on the safe side, calculation is done as 1/60 of an hour is measuring while 59/60 time is spent sleeping.
Average cost would be 0.00825×(1/60) + 0.000495×(59/60) = 0,0001375 + 0,00048675 = 0,00062425 watts.
Please note how important sleep is for maximizing the battery-life.
For a battery with 4400mAh and 3.7V output calculation as :
4400mAh × 3.7V = 8.1 Wh -> 8.1Wh / 0,00062425W = 12 976 hours -> approx 1,5 years battery life-time.

## :anchor: Platform
Prior to choosing platform three different platforms were tried : Datacake, Pybytes and Ubidots. Due to the simplicity vizualising the data Ubidots was chosen as the platform to proceed with. Ubidots is a cloud-based, user-friendly platform that is suitable for these types of project. An alternative could be running a [TIG-stack][tig].
Make sure to create a [Ubidots STEM account][ubi_stem] to claim the Ubidots token. For scalability and more features it is easy to upgrade to a suitable payment plan, for most people IoT Entrepreneur should be sufficient, up to 25 devices with support for 20 variables for each device.

[ubi_stem]:https://ubidots.com/stem/
[tig]:https://hackmd.io/@lnu-iot/tig-stack

## :mag_right: The code
As mentioned earlier complete code is available in repository, complete code also includes comments and explanation.

- Code :
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
Data is recieved in Helium console then forwarded to Ubidots and Datacake using built in HTTP and Webhook integration, the data package also referred to as payload is decoded in both applications. To increase the number of variables that would be transferred one must update the payload decoder, below are examples of how different [data structures][data_structures] can be decoded:
```python
decoded_payload['temperature'] = (bytes[0] << 24 >> 16 | bytes[1]) / 100
decoded_payload['humidity'] = (bytes[2])
#decoded_payload['pressure'] = (bytes[3])
``` 
Data from device is packaged into payload :
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
For visualization of the data Ubidots was used, it is a cloud service where the data can be read for a specific time-period.
Ubidots STEM keeps the data for one month. However, if upgrade is done to Ubidots IoT Entrepreneur package data is stored 2 years.
Reason for going with Ubidots is that it is very easy to use, all graphs were out of the box solution. 
To generate graphs below, just decide what variables from the device that should be shown.

![](https://i.imgur.com/Q5VibFh.jpeg)
![](https://i.imgur.com/yRpmZoy.jpeg)
![](https://i.imgur.com/NanrpSB.jpeg)
![](https://i.imgur.com/qG4CtMI.jpeg)


## Finalizing the design
This project is a very good introduction to the IoT-world. The parts are quite cheap, so if any mistakes with wiring a new sensor costs 49:-. This LoPy will remain as a weather-station until I've purchased a new thermometer. If it will remain a weather-station I will probably include CO2, pressure and light measurements.
The DHT11 sensor is extremly cheap, however since there is not too much temperature variance going with the DHT22 with better resolution would give more interesting graphs.
This could also be done reading the temperature from another sensor, this would affect the energy consumption.
The inverse relation-ship between humidity and temperature was quite supprising of how often it was clearly visible in the graphs.

![](https://i.imgur.com/rDd5xk3.jpg)
