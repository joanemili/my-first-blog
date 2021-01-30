from django.urls import path
from . import views

urlpatterns = [
    
    path('today_special/', views.today_special, name='today_special'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
]