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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, blank=True, null=True, on_delete=models.CASCADE, default=1)
    class Meta:
        verbose_name = 'robot'
        verbose_name_plural = 'robots'

    def __str__(self):
        return self.robotname

class mqttbroker(models.Model):
    # Fields
    mqttbroker= models.CharField(max_length=20,help_text='Enter field documentation')
    mqtthost = models.CharField(max_length=20, help_text='Enter field documentation')
    mqttport = models.CharField(max_length=20, help_text='Enter field documentation')
    apikey = models.CharField(max_length=40,default="0",help_text='Enter field documentation')

    def __str__(self):
        return self.mqttbroker
