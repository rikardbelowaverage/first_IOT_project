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

    #>hB refers to datatypes of variables temperature and humidity
    #*100 gives possibility of decimals without using float
    payload = struct.pack('>hB', int(temperature * 100), int(humidity))
    s.send(payload)

    print('sent temperature:', temperature)
    print('sent humidity:', humidity)
    
    #LED-indication that data has been sent
    pycom.rgbled(0x00ff00) 
    #How long time LED should be active
    time.sleep(1)
    #Turns off LED
    pycom.heartbeat(False) 

    ms_to_minutes = 1000*60
    snooze_timer = 15

    lora.nvram_save()
    machine.deepsleep(ms_to_minutes*snooze_timer)
