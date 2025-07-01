from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    Pname = models.CharField(max_length=30)
    Pprice = models.IntegerField()
    Pcolor = models.CharField(max_length=40)
    Quantity = models.IntegerField()

    #No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.

    def get_absolute_url(self):
        return reverse('pro1',args={self.pk})






# django.core.exceptions.ImproperlyConfigured: No URL to redirect to.  Either provide a url or define a get_a
# bsolute_url method on the Model.




