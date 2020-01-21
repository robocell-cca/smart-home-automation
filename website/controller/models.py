from django.db import models


class Location(models.Model):
    """
    All the locations known to the system
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    """
    All the devices known to the system
    """
    name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 related_name='devices',
                                 related_query_name='device')
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    """
    State v/s time logs for all devices
    """
    device = models.ForeignKey(Device,
                               on_delete=models.CASCADE,
                               related_name='logs',
                               related_query_name='log')
    datetime = models.DateTimeField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.device.name + ' @ ' + str(self.datetime)


class Sensor(models.Model):
    """
    All the sensors known to the system
    """
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE,
                                 related_name='sensors',
                                 related_query_name='sensor')
    units = models.CharField(max_length=100)
    part_id = models.CharField(max_length=100)
    reference_value = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class SensorLog(models.Model):
    """
    Sensor values v/s Time logs
    """
    sensor = models.ForeignKey(Sensor,
                               on_delete=models.CASCADE,
                               related_name='logs',
                               related_query_name='log')
    datetime = models.DateTimeField()
    value = models.DecimalField(decimal_places=2,
                                max_digits=100)

    def __str__(self):
        return self.sensor.name + ' @ ' + str(self.datetime)
