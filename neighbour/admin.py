from django.contrib import admin
from .models import Neighbourhood, Business, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Neighbourhood)