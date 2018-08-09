from django.db import models

# Create your models here.
class mqttbroker(models.Model):
    # Fields
    mqttuser = models.CharField(max_length=20, help_text='Enter field documentation')
    mqttpass = models.CharField(max_length=20, help_text='Enter field documentation')
    mqtthost = models.CharField(max_length=20, help_text='Enter field documentation')
    mqttport = models.CharField(max_length=20, help_text='Enter field documentation')
    def __str__(self):
        return self.mqtthost + " - " +self.mqttuser
