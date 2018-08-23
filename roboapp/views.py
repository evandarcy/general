from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import mqttbroker
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from .models import robot
from .models import battle
import requests
from django.http import JsonResponse
import paho.mqtt.publish as publish
# Create your views here.
def ajax(request, robot1_id, robot2_id):
    turn = robot2_id
    first_robot = robot1_id
    second_robot = robot2_id
    # s = request.POST.get('status')
    # print(s)
    #Get current_battle object
    current_battle = battle.objects.get(gameongoing=True)
    if current_battle.current_turn > 10:
        data = {
            'robotturn': turn
        }
        print("game over")
        message = "Game Over"
        current_battle.current_turn = 0
        current_battle.save()
        return redirect('home')

    #Increment turns value by 1 on each request
    current_battle.current_turn = current_battle.current_turn + 1
    #Save new value
    current_battle.save()
    print(current_battle.current_turn)

    # If the current turn is an even number, It is robot 2 turn
    if current_battle.current_turn % 2 == 0:
        turn = robot2_id
        publish.single("robots/health", '{"robotturn":'+'"'+robot2_id+'"'+'}', hostname="m20.cloudmqtt.com",port=11086, client_id="",auth = {'username':"uzsrcidn", 'password':"V0lGagE"})

    # If the current turn is an odd number, It is robot 1 turn
    if current_battle.current_turn % 2 != 0:
        turn = robot1_id
        publish.single("robots/health", '{"robotturn":'+'"'+robot1_id+'"'+'}', hostname="m20.cloudmqtt.com",port=11086, client_id="",auth = {'username':"uzsrcidn", 'password':"V0lGagE"})

    data = {
        'robotturn': turn
    }

    return JsonResponse(data)

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
            robotobject.mqttpass = mqttpass
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
