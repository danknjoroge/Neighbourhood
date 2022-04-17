from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length=288)
    location = models.CharField(max_length=288)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_posted = models.DateTimeField(auto_now_add=True)

    def save_neighbours(self):
        self.save()
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    your_id = models.IntegerField()
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    profile_picture = models.ImageField(default='default.png')
    bio = models.TextField( default="Bio")

    def save_userprofile(self):
        self.save()
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=277)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def save_business(self):
        self.save()
        return self.name


    def search_by_name(self, search_term):
        





