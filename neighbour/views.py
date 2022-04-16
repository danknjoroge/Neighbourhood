from django.shortcuts import redirect, render
from neighbour.models import Neighbourhood
from .forms import NeighbourhoodForm

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






