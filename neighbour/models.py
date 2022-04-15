from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=288)
    location = models.CharField(max_length=288)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE )

class User(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(max_length=8)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()







