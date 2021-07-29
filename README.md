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
|LoPy4 and sensors bundle, 949:- | [:credit_card:][Electrokit_LoPy] |
|Battery LiPo 3.7V 4400mAh, 249:- | [:credit_card:][Electrokit_Battery] |
|Sensor kit – 25 modules, 299:- | [:credit_card:][Electrokit_Sensors] |
|Digital temperature and humidity sensor DHT11, 49:- | [:credit_card:][Electrokit_DHT] |

[Electrokit_LoPy]: https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/
[Electrokit_Sensors]: https://www.electrokit.com/produkt/sensor-kit-26-moduler/
[Electrokit_DHT]: https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/
[Electrokit_Battery]: https://www.electrokit.com/produkt/batteri-lipo-3-7v-4400mah/

*Note : prices are from 29/07-2021
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

## :anchor: Platform

## :mag_right: The code
As mentioned earlier complete code is available in repository. 

## :helicopter: Transmitting the data / connectivity

## Presenting the data

## Finalizing the design



