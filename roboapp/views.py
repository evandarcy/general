from django.shortcuts import render
from django.http import HttpResponse
from .models import mqttbroker
# Create your views here.

def arena(request):
    #return HttpResponse("Hello, world. You're at the robowars arena.")
    object1 = mqttbroker.objects.get(mqttport="32285") #Get mqtt broker details for mqttbroker object on port 32285
    user = object1.mqttuser
    password = object1.mqttpass
    host = object1.mqtthost
    port = object1.mqttport #Set 'port' equal to the mqttport value of the object
    context = {'mqttport': port,
               'mqttpass': password,
               'mqtthost': host,
               'mqttuser': user,} #Dictionary to map "mqttport" to the corresponding variable
    return render(request, 'arena.html', context)
