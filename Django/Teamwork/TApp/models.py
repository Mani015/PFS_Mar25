from django.db import models

class Student(models.Model):
    Fname = models.CharField(max_length=35)
    Lname = models.CharField(max_length=43)
    RollNo = models.IntegerField()
    Age = models.IntegerField()
    Grade = models.FloatField()

# Create your models here.
