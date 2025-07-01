from django.db import models

# Create your models here.

class Product(models.Model):
    Pname = models.CharField(max_length=30)
    Pprice = models.IntegerField()
    Pcolor = models.CharField(max_length=40)
    Quantity = models.IntegerField()


