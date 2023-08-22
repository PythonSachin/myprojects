from django.db import models

# Create your models here.
class Data(models.Model):
    country = models.CharField(max_length=50)
    population = models.IntegerField();
    statescount = models.IntegerField();

