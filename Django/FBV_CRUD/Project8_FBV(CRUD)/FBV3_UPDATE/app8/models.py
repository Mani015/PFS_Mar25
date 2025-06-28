from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    EFname = models.CharField(max_length=20)
    ELname = models.CharField(max_length=20)
    ESalary = models.IntegerField()

