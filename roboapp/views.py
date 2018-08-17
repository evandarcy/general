from django.shortcuts import render
from django.http import HttpResponse
from .models import mqttbroker
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .models import robot
import requests
# Create your views here.

def arena(request):
    # Check if the current user's username matches the 'user' field assigned to the robot objects
    # If there is a match, the user is considered to be authorized and may access the arena to control
    # robot. A unique key will be passed to the mqtt broker upon entry and will be changed after logout.
    # If the user is not authorized, they will be redirected back to the home.html page with an error message

    # current_user = request.user
    unique_key = get_random_string(length=7)
    # Get current username
    user = User.objects.get(username=request.user.username)
    userrobot = []
    user_has_robot = False

    # Create list of robots
    robot_list = robot.objects.filter()
    for i in robot_list:
        #If user linked to robot is same as user attempting access
        if i.user == user:
            print("\nRobot found for:",user,"; robot = ",i.robotname,"\n")
            # Append userrobot to correct robot
            user_has_robot = True
            userrobot.append(i) #set robot object matched to user as 'userrobot'

            # Get data relating to robot
            robotobject = robot.objects.get(robotname=userrobot[0].robotname)
            mqttuser = robotobject.mqttuser
            robotname = robotobject.robotname

            # Get data relating to broker
            brokerobject = mqttbroker.objects.get(mqttbroker=robotobject.broker) #Get mqtt broker details for mqttbroker object on port 32285
            host = brokerobject.mqtthost
            port = brokerobject.mqttport #Set 'port' equal to the mqttport value of the object
            apikey = brokerobject.apikey

            ###################
            # Update password of mqtt user in Django database with unique key
            # Then update password in cloudmqtt
            mqttpass = unique_key #set mqttpass equal to unique key
            robotobject.save() #save update to db

            url = "https://api.cloudmqtt.com/api/user/"+str(mqttuser) #cloudmqtt api update password, pass username in url
            headers= {'Content-Type': 'application/json',}
            data = '{"password":'+'"'+mqttpass+'"'+'}'
            r = requests.put(url, headers=headers, data=data, auth=('', apikey))
            print(r.content)
            ###################
            ##################

            context = {'mqttport': port,
                       'mqtthost': host,
                       'mqttuser': mqttuser,
                       'mqttpass': mqttpass,
                       'user_has_robot': user_has_robot,
                       'UUID': unique_key,} #Dictionary to map "mqttport" to the corresponding variable

            # Debug
            print(data)
            print(robotname)
            print(mqttuser)
            print(mqttpass)
            print(host)
            print(port,"\n")
            return render(request, 'arena.html', context)
        else:
            print("No Robot Found for user")

    error = "You are not authorized to access the arena at this time."
    context = {'error': error,} #Dictionary to map "mqttport" to the corresponding variable

    return render(request, 'home.html', context)
