import random

class AD123:

    def __init__(self, name, pins, setup=True):
        self.name = name
        self.pins = pins

        if setup:
            self.setup()

    def setup(self):
        # Do any kind of setup that might be needed
        print('Setting up the connections for AD123: {}...'.format(self.name))

    def read(self):
        # Read the sensor value here
        print('{}: Reading sensor value...'.format(self.name))
        value = random.randint(0, 10)
        return value

