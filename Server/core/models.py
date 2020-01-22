from django.db import models

# Create your models here.
from Server.users.models import User


class Device(models.Model):
    name = models.TextField()
    password = models.TextField()
    lat = models.FloatField()
    log = models.FloatField()


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.TextField()
    begin_hours = models.DateField()
    end_hours = models.DateField()
    lat = models.FloatField()
    log = models.FloatField()
    ratio = models.FloatField()


