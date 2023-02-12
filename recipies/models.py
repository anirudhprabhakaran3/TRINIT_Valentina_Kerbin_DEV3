from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=100)
    n = models.FloatField()
    p = models.FloatField()
    k = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    instructions = models.TextField()

    def __str__(self):
        return self.plant_name
