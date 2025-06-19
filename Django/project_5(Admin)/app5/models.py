from django.db import models
# Create your models here.
class Student(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Marks = models.FloatField()
    Location = models.CharField(max_length=20)



