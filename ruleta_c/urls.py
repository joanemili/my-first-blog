from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_roulette, name='query_roulette'),

]