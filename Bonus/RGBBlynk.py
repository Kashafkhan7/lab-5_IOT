import network
import BlynkLib
from machine import Pin
import time
from neopixel import NeoPixel




wifi = network.WLAN(network.STA_IF)

ssid = 'Ibrahim(4G)'
password = '47224723'

wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Connected to Wi-Fi:", wifi.ifconfig())

blynk = BlynkLib.Blynk('fvuM0JJfgx_OIU3wLcfCN_cnBuytB1oC')

pin = Pin(48, Pin.OUT)   
led = NeoPixel(pin, 1)

@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected!")



@blynk.on('V1')  # RED LED
def red_led(value):
    if int(value[0]) == 1:
        led[0] = (255, 0, 0)  # Green
    else:
        led[0] = (0, 0, 0)  # Turn off LED
    led.write()	
        
@blynk.on('V2')  # Green LED
def green_led(value):
    if int(value[0]) == 1:
        led[0] = (0, 255, 0)  # Red
    else:
        led[0] = (0, 0, 0)  # Turn off LED
    led.write()
    
@blynk.on('V3')  # Blue LED
def blue_led(value):
    if int(value[0]) == 1:
        led[0] = (0, 0, 255)  # Blue
    else:
        led[0] = (0, 0, 0)  # Turn off LED
    led.write()
    

    
        
while True:
    blynk.run()
 
    time.sleep(0.1)