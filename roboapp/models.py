from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class robot(models.Model):
    # Fields
    robotname = models.CharField(max_length=50, default='')
    mqttuser = models.CharField(max_length=30, blank=True)
    mqttpass = models.CharField(max_length=30, blank=True)
    broker = models.ForeignKey('mqttbroker',on_delete=models.CASCADE,default=1)
    camera_ip = models.CharField(max_length=80, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, blank=True, null=True, on_delete=models.CASCADE, default=1)
    class Meta:
        verbose_name = 'robot'
        verbose_name_plural = 'robots'

    def __str__(self):
        return self.robotname

class mqttbroker(models.Model):
    # Fields
    mqttbroker = models.CharField(max_length=20,help_text='Enter field documentation')
    mqtthost = models.CharField(max_length=20, help_text='Enter field documentation')
    mqttport = models.CharField(max_length=20, help_text='Enter field documentation')
    apikey = models.CharField(max_length=40,default="0",help_text='Enter field documentation')

    def __str__(self):
        return self.mqttbroker

class battle(models.Model):
    gameongoing = models.BooleanField(default=True)
    robotturn = models.CharField(max_length=40,default=" ",help_text='Robot ID of current robot turn')
    current_turn = models.IntegerField(default=0,help_text='Turns taken so far')
    def __str__(self):
        return self.robotturn

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    robot_name = models.CharField(max_length=80)
    xp = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + " - " + str(self.robot_name)


class Competition(models.Model):
    datetime = models.DateTimeField()
    entry_cost = models.IntegerField(default=100)
    arena = models.TextField(max_length=300, null=True)
    name = models.TextField(max_length=300)
    active_players = models.IntegerField(default=0)
    player_limit = models.IntegerField(default=2)
    player_link = models.ManyToManyField(UserProfile, null=True, blank=True)
    first_place = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="user_profile1", blank=True, null=True)
    second_place = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="user_profile2", blank=True, null=True)
    third_place = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="user_profile3", blank=True, null=True)

    def __str__(self):
        return str(self.name) + " - " + str(self.active_players) + " Players - " + str(self.datetime)
