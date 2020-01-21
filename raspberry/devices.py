#sudo idle to control GPIO pins
# pin 7 11 13 are used to control leds

import RPi.GPIO as GPIO
from requests import get
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
while True:
    r =get('http://192.168.0.6:8000/manage/api/devices/')

    count=0
    led=[7,11,13]
    print led[0]
    def ledon(pin):
        #code to turn the led on
        GPIO.output(pin,True)
        

    def ledoff(pin):
        #code to turn the led off
        GPIO.output(pin,False)

    for d in r.json():
        if d["state"] == '0':
            ledoff(led[count])
            print("led",count,"off")
        else:
            ledon(led[count])
            print("led",count,"on")
        count+=1
    time.sleep(1)
