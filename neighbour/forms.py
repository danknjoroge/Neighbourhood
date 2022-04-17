from django import forms
from .models import Business, Neighbourhood, Post, UserProfile


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['posted_by', 'posted_on']



