"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (DeviceViewSet, LocationViewSet, SensorViewSet,
                    LocationDevicesViewSet, DeviceLogViewSet, SensorLogViewSet)

urlpatterns = [

    # Device related views
    path('devices/', DeviceViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('devices/<str:name>', DeviceViewSet.as_view(
        {
            'get': 'retrieve'
        })),
    path('devices/<str:name>/setstate/<str:state>', DeviceViewSet.as_view(
        {
            'get': 'setstate'
        })),

    # Location related views
    path('locations/', LocationViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),
    path('locations/<str:name>', LocationViewSet.as_view(
        {
            'get': 'retrieve'
        })),
    path('locations/<str:name>/devices', LocationDevicesViewSet.as_view(
        {
            'get': 'list'
        })),

    # Sensor related views
    path('sensors/', SensorViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        })),

    path('sensors/<str:name>/addlog/', SensorViewSet.as_view(
        {
            'post': 'addlog'
        
        })),

    # DeviceLog related views
    path('devicelogs/', DeviceLogViewSet.as_view(
        {
            'get': 'list',
        })),

    # SensorLog related views
    path('sensorlogs/', SensorLogViewSet.as_view(
        {
            'get': 'list',
        })),
]
