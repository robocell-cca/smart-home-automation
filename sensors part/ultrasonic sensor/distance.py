import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig=23
echo=24
#GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig,1)
time.sleep(0.0001)
GPIO.output(trig,0)

while GPIO.input(echo)==0:
	start=time.time()
while GPIO.input(echo)==1:
	end=time.time()
ttime=end-start

#cm:
distance=ttime/0.000058

print(distance) 
GPIO.cleanup()
