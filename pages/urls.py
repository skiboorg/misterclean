from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

   path('', views.index, name='index'),
   path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
   path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
   path('posts/', views.allPosts, name='allposts'),
   path('posts/<slug>/', views.showPost, name='showpost'),
   path('about/', views.about, name='about'),
   path('policy/', views.policy, name='policy'),
   path('contacts/', views.contacts, name='contacts'),
   path('service/', views.services, name='services'),
   path('service/<slug>/', views.service, name='service'),
   path('robots.txt', views.robots, name='robots'),



]
