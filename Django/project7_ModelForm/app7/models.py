from django.db import models

# Create your models here.

class VehicleParking(models.Model):
    VehicleNum = models.CharField(max_length=20)
    VehicleName = models.CharField(max_length=20)
    VehicleWheels = models.IntegerField()
    VehicleToken = models.IntegerField()





