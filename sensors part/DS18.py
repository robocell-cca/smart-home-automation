import time
from w1thermsensor import W1ThermSensor

class DS18:

    def __init__(self, name, pins, setup=True):
        self.name = name
        self.pins = pins
        if setup:
            self.setup()

    def setup(self):
        # Do any kind of setup that might be needed
        print('Setting up the connections for temp_sensor DS18 : {}...'.format(self.name))
        self.sensor = W1ThermSensor()


    def read(self):
        # Read the sensor value here
        print('{}: Reading sensor value...'.format(self.name))
        temperature = self.sensor.get_temperature()
        time.sleep(1)
        return temperature