from AD123 import AD123
from DS18 import DS18
from HC-SR04 import HC-SR04
from sensormanager import SensorManager
import schedule, time


sensors = [
    SensorManager(sensorinstance=AD123(name='AD123-bedroom',
                                       pins=(1,2)),
                  url='domain:port/endpoint',
                  timeperiod=2),
    
    SensorManager(sensorinstance=DS18(name='DS18-room1',
                                       pins=(7)),
                  url='domain:port/endpoint',
                  timeperiod=5),
    
    SensorManager(sensorinstance=HC-SR04(name='HCSR04-room1',
                                       pins=(23,24)),
                  url='domain:port/endpoint',
                  timeperiod=5),
    
    # More sensors initialized here
]
for sensor in sensors:
    schedule.every(sensor.timeperiod).seconds.do(sensor.run)

while 1:
    schedule.run_pending()
    time.sleep(1)
    