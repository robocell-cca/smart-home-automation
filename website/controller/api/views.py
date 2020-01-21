from datetime import datetime
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DeviceSerializer, LocationSerializer
from .serializers import DeviceLogSerializer, SensorLogSerializer
from .serializers import SensorSerializer
from ..models import Device, Location, DeviceLog, Sensor, SensorLog

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    lookup_field = 'name'
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['GET'])
    def setstate(self, request, state, *args, **kwargs):
        device = self.get_object()
        target_state = state

        if device.state == target_state:
            serialized = DeviceSerializer(device)
            return Response(serialized.data)

        device.state = target_state
        device.save()
        devicelog = DeviceLog(device=device,
                              state=target_state,
                              datetime=datetime.now())
        devicelog.save()

        serialized = DeviceSerializer(device)
        return Response(serialized.data)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    lookup_field = 'name'
    serializer_class = LocationSerializer


class LocationDevicesViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(location__name=self.kwargs['name'])


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    lookup_field = 'name'
    serializer_class = DeviceLogSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    lookup_field = 'name'
    serializer_class = SensorSerializer

    @action(detail=True, methods=['POST'])
    def addlog(self, request, *args, **kwargs):
        sensor = self.get_object()
        target_value = request.data['value']
        sensorlog = SensorLog(sensor=sensor, datetime=datetime.now(),
                              value=target_value)
        sensorlog.save()

        serialized = SensorLogSerializer(sensorlog)

        def recompute_states(sensorlog, sensor):
            refer = sensor.reference_value

            devices = sensor.location.devices.filter(type='electrical')
            if(sensorlog.value > refer):
                for dev in devices:

                    if dev.state == '1':
                        continue
                    dev.state = '1'
                    dev.save()
                    devicelog = DeviceLog(device=dev,
                                          state='1',
                                          datetime=datetime.now())
                    devicelog.save()
            elif(sensorlog.value < refer):
                for dev in devices:

                    if dev.state == '0':
                        continue
                    dev.state = '0'
                    dev.save()
                    devicelog = DeviceLog(device=dev,
                                          state='0',
                                          datetime=datetime.now())
                    devicelog.save()

        recompute_states(sensorlog, sensor)
        return Response(serialized.data)


class SensorLogViewSet(viewsets.ModelViewSet):
    queryset = SensorLog.objects.all()
    lookup_field = 'name'
    serializer_class = SensorLogSerializer
