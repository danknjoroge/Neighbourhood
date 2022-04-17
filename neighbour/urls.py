from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    # path('search/', views.search, name='search'),
    path('business/', views.business, name='business'),
    path('post', views.post, name='post'),
    # re_path(r'^search/', views.search, name='search')

    re_path(r'^search/$', views.search_results, name='search'),

]