from django.contrib import admin
from .models import Neighbourhood, Business, Post, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Post)