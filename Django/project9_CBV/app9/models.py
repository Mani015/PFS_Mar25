from django.db import models

# Create your models here.

class Voter(models.Model):
    VoterId = models.IntegerField()
    VoterName = models.CharField(max_length=20)
    VoterAge = models.IntegerField()
    VoterAddress = models.CharField(max_length=30)
