# Tutorial How to build a portable weather station with Pycom LoPy4
#### By Rikard Johansson, rj222pj
###### Tags: `Weather Station, IoT, LNU, LoPy4, Pycom`

- Table of Content
[ToC]

## :memo: Summarized project overview

This project describes how to easily create a sensor that monitors the air quality and temperature of your home. This involves some light tinkering and just a pinch of programming. Following this guide will probably take about 2-3 hours but someone with experience could complete the project in under an hour. 

Tutorial describes how to create an IoT package which measures humidity and temperature at given location. Project includes basic programming, wiring and data transportation setup. An approximation for completing project would be 3 hours, some variance depending on previous experience and pre-installed programs.

## :page_with_curl: Why this project
There are a couple of reasons for why this became the chosen project, recently the home-thermometer broke. With this summers hot temperatures and no temperature measurement it became the obvious choice. Main purpose of project was learning basics of IoT : how data goes from measured to visualized.
Future plans involves installation of CO2 and air pressure sensors, which would give the weather station possibility to monitor:
- Temperature
- Humidity
- Air pressure
- CO2 concentration

## :microscope: Bill of Materials

| Material            | Where to buy            |
| -----------------   |:----------------------- |
|LoPy4 and sensors bundle, 949:- | [:link:][Electrokit_LoPy]|
|Battery LiPo 3.7V 4400mAh, 249:- | [:link:][Electrokit_Battery]|
|Choose one below|
|Sensor kit – 25 modules, 299:- | [:link:][Electrokit_Sensors]
|Digital temperature and humidity sensor DHT11, 49:- |[:link:][Electrokit_DHT]

[Electrokit_LoPy]:https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/
[Electrokit_Sensors]:https://www.electrokit.com/produkt/sensor-kit-26-moduler/
[Electrokit_DHT]:https://www.electrokit.com/en/product/digital-temperature-and-humidity-sensor-dht11/
[Electrokit_Battery]:https://www.electrokit.com/produkt/batteri-lipo-3-7v-4400mah/

LoPy4 board with its ease of use of LoRaWAN makes it a good choice for this type of project.

## :computer: Computer setup

