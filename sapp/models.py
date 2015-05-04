from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Konnect Integrate class that holds all integrations
class KIntegrate(models.Model):
    user = models.ForeignKey(User)
    number = models.BigIntegerField()
    integration_type = models.CharField(max_length = 50) 
    app_url = models.URLField()
    app_key = models.CharField(max_length = 500)


    def __unicode__(self):
       return str(self.number)



