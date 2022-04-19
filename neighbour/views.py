from django.shortcuts import redirect, render
from neighbour.models import Neighbourhood, Post, UserProfile, Business
from .forms import BusinessForm, NeighbourhoodForm, PostForm, ProfileForm
from django.contrib.auth.decorators import login_required
from pyexpat.errors import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404



# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    neighbour = Neighbourhood.objects.all().order_by('-date_posted')
    return render(request, 'home.html', {"neighbour": neighbour})

# .order_by("-date_created")

# def profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile= form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return redirect('profile')
#     else:
#         form = ProfileForm()
#         profile= UserProfile.objects.all()

#     return render(request, 'post/profile.html', {'form': form, 'profile': profile})

# @login_required(login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('profile')

    else:
        form = ProfileForm()
        profile = UserProfile.objects.all()
        # project = Projects.objects.all()
    return render(request, 'post/profile.html', {'form': form, 'profile': profile})
    
@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    form = BusinessForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            business= form.save(commit=False)
            business.user=current_user
            business.save()
        return redirect('business')
    else:
        form= BusinessForm()
        business = Business.objects.all()
    return render(request, 'post/business.html', {'form': form, 'business': business})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        neighbourhood = Neighbourhood.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'post/search.html',{"message":message,"neighbourhood": neighbourhood})

    else:
        message = "You haven't searched for any term"
        neighbour = Neighbourhood.objects.all().order_by('-date_posted')

        return render(request, 'post/search.html',{"message":message, 'neighbour':neighbour})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.save()
        return redirect('post')
    else:
        form = PostForm()
        post = Post.objects.all()
    return render(request, 'post/post.html', {'form': form, 'post': post})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'post/sach.html',{"message":message,"business": business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'post/sach.html',{"message":message})


@login_required(login_url='/accounts/login/')
def neigh(request):
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
    return render(request, 'post/neigh.html', { "form": form, "neighbour": neighbour})



@login_required(login_url='/accounts/login/')
def neidetails(request, neighbourhood_id):
    try:
        neighbour = Neighbourhood.objects.get(id = neighbourhood_id)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'post/nei.html', {'neighbour': neighbour})

@login_required(login_url='/accounts/login/')
def delete_post(request, pk):
    post = Neighbourhood.objects.get(id=pk)
    
    if request.method == 'POST':
        try:
            post.delete()
            return redirect('home')
        except Exception:
            messages.error('Post does not exist')

    context = { 'obj':post }
    return render(request, 'delete.html', context)


