from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('neigh/', views.neigh, name='neigh'),
    path('neidetails/<int:neighbourhood_id>/', views.neidetails, name='neidetails'),
    path('business/', views.business, name='business'),
    path('post', views.post, name='post'),
    # re_path(r'^search/', views.search, name='search')

    re_path(r'^search/$', views.search_results, name='search'),
    re_path(r'^searchn/$', views.search, name='searchn'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)