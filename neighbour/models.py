import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    image = models.ImageField(upload_to = 'neighbourhood/', default='default.png')
    neighbourhood_name = models.CharField(max_length=288)
    location = models.CharField(max_length=288)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location

    def save_neighbours(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        neighbourhood = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhood


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    your_id = models.IntegerField()
    neighbourhood_name = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    profile_picture = models.ImageField(default='default.png', upload_to = 'profile/')
    bio = models.TextField( default="Bio")

    def __str__(self):
        return self.name

    def save_userprofile(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


class Business(models.Model):
    name = models.CharField(max_length=277)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_name = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business


class Post(models.Model):
    title = models.CharField(max_length=122)
    image = models.ImageField(default='default.png', upload_to = 'posts/')
    description = models.TextField()
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on= models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()
        return self.title






