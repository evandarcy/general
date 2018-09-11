from django.contrib import admin
from .models import mqttbroker
from .models import robot
from .models import battle, Competition, UserProfile


# Register your models here.

# Display data in mqtt class
admin.site.register(mqttbroker)

class RobotAdmin(admin.ModelAdmin):
    list_display = ['robotname', 'mqttuser', 'mqttpass', 'broker', 'user']
admin.site.register(robot, RobotAdmin)
admin.site.register(battle)
admin.site.register(UserProfile)
admin.site.register(Competition)
