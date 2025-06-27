from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Marks = models.IntegerField()
    Location = models.CharField(max_length=20)
    Join_Date = models.DateField()



