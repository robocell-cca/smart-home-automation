from django.contrib import admin
from .models import Device, Location, DeviceLog, Sensor, SensorLog

admin.site.register(Device)
admin.site.register(Location)
admin.site.register(DeviceLog)
admin.site.register(Sensor)
admin.site.register(SensorLog)
