from django.db import models
from django.urls import reverse

# Create your models here.

class Voter(models.Model):
    VoterId = models.IntegerField()
    VoterName = models.CharField(max_length=20)
    VoterAge = models.IntegerField()
    VoterAddress = models.CharField(max_length=30)

    #define a get_absolute_url method on the Model.

    def get_absolute_url(self):
        return reverse('vote1',args={self.pk})

