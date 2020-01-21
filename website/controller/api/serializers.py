from rest_framework import serializers
from ..models import Device, Location, DeviceLog, Sensor, SensorLog


class DeviceSerializer(serializers.ModelSerializer):

    location = serializers.SlugRelatedField(
        read_only=False,
        slug_field='name',
        queryset=Location.objects.all()
    )

    class Meta:
        model = Device
        fields = [
            'name',
            'state',
            'type',
            'description',
            'location'
        ]


class LocationSerializer(serializers.ModelSerializer):
    devices = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Location
        fields = [
            'name',
            'description',
            'devices'
        ]


class DeviceLogSerializer(serializers.ModelSerializer):
    device = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = DeviceLog
        fields = [
            'device',
            'datetime',
            'state',
        ]


class SensorSerializer(serializers.ModelSerializer):
    
    location = serializers.SlugRelatedField(
        read_only=False,
        slug_field='name',
        queryset=Location.objects.all()
    )

    class Meta:
        model = Sensor
        fields = [
            'name',
            'type',
            'units',
            'location',
            'reference_value'
        ]


class SensorLogSerializer(serializers.ModelSerializer):
    sensor = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = SensorLog
        fields = [
            'sensor',
            'datetime',
            'value',
        ]
        