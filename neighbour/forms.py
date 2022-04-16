from django import forms
from .models import Neighbourhood, UserProfile


class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']





