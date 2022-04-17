from django.shortcuts import redirect, render
from neighbour.models import Neighbourhood, UserProfile
from .forms import NeighbourhoodForm, ProfileForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    current_user = request.user
    form = NeighbourhoodForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.admin = current_user
            post.save()
        return redirect('home')
        
    else:
        form = NeighbourhoodForm()
        neighbour = Neighbourhood.objects.all()
    return render(request, 'home.html', { "form": form, "neighbour": neighbour})


def profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            profile= form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
        profile= UserProfile.objects.all()

    return render(request, 'profile.html', {'form': form, 'profile': profile})


def search(request):
    pass




