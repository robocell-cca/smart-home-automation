import  RPi.GPIO as GPIO
import time

class HC-SR04:

    def __init__(self, name, pins, setup=True):
        self.name = name
        self.pins = pins

        if setup:
            self.setup()

    def setup(self):
        # Do any kind of setup that might be needed
        print('Setting up the connections for HC_SR04: {}...'.format(self.name))

        GPIO.setmode(GPIO.BCM)
        self.trig=self.pins(0)
        self.echo=self.pins(1)
        #GPIO.setwarnings(False)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def read(self):
        # Read the sensor value here
        print('{}: Reading sensor value...'.format(self.name))
        
        GPIO.output(self.trig,1)
        time.sleep(0.0001)
        GPIO.output(self.trig,0)

        while GPIO.input(self.echo)==0:
	        start=time.time()
        while GPIO.input(self.echo)==1:
	        end=time.time()
        ttime=end-start

        #cm:
        distance=ttime/0.000058
        GPIO.cleanup()
        return distance

