import time
import binascii
import pycom
import socket

from network import LoRa
from keys import APP_KEY, DEV_EUI, APP2_KEY, APP2_EUI

#Function to convert rgb-color to hex
def rgb_to_hex(red, green, blue):
    return '%02x%02x%02x' % (red, green, blue)

#Creates LoRa-object, note EU 868 frequency
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

#Short sleep supporting ctrl-c cancellation
time.sleep(5)

#Keys for joining helium or other chosen LoRa-Network
dev_eui = binascii.unhexlify(DEV_EUI)
app_eui = binascii.unhexlify(APP2_EUI)
app_key = binascii.unhexlify(APP2_KEY)


#Attempts to join LoRa network with earlier provided credencials
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#counter = 0 #Counter can be used for comparing different networks time to join

# Remains in while-loop until network has joined
while not lora.has_joined():
    time.sleep(10)
    print('Not connected to Network')

    #print(counter) #Uncomment if need to see amount of triers
    #counter = counter + 1 #


    for i in range(256):
        color = rgb_to_hex(i,i,i)
        pycom.rgbled(256-int(color,16))
    time.sleep(0.005)

print('Connected to Network')
