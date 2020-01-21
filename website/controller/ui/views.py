from django.shortcuts import render
from django.http import HttpResponse

from ..models import Device, DeviceLog
from datetime import datetime

def index(request):
    return (HttpResponse('This will contain UI for controlling all the appliances'))

def set_state(request):

    device_name = request.GET.get('device')
    target_state = request.GET.get('state')

    device = Device.objects.get(name=device_name)

    if device.latest_state.state == target_state:
        return HttpResponse(device_name + " is already " + target_state)

    device.state = target_state
    device.save()
    devicelog = DeviceLog(device=device, state=target_state, datetime=datetime.now())
    devicelog.save()

    return HttpResponse(device_name + " set to " + target_state)

def get_state(request):

    device_name = request.GET.get('device')

    device = Device.objects.get(name=device_name)

    return (HttpResponse(device.state))