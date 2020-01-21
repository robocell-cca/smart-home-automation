class SensorManager:
    
    def __init__(self, sensorinstance, url, timeperiod):
        self.sensorinstance = sensorinstance
        self.url = url
        self.timeperiod = timeperiod


    def post(self, value):
        # Post the values to the url
        print('{}: Sending the value to the server...'.format(self.sensorinstance.name))
    

    def run(self):
        self.post(self.sensorinstance.read())