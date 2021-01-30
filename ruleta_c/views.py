from django.shortcuts import render
from .models import Consultes, Respostes, Bases, Solucions
import random

def index(request):
    numero = random.randint(1,35)
    consulta = Consultes.objects.filter(codi=numero) 
    return render(request, 'ruleta_c/index.html',{'consulta':consulta})


def today_special(request):
    numero = random.randint(1,35)
    consulta = Consultes.objects.filter(codi=numero) 
    return render(request, 'ruleta_c/today_special.html',{'consulta':consulta})

def menu(request):
    numero = random.randint(1,35)
    consulta = Consultes.objects.filter(codi=numero) 
    return render(request, 'ruleta_c/menu.html',{'consulta':consulta})

def contact(request):
    numero = random.randint(1,35)
    consulta = Consultes.objects.filter(codi=numero) 
    return render(request, 'ruleta_c/contact.html',{'consulta':consulta})
