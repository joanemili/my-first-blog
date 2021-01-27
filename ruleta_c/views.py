from django.shortcuts import render
from .models import Consultes, Respostes, Bases, Solucions
import random

def query_roulette(request):
    #rang = xrange(10)
    numero = random.randint(1,10)
    consulta = Consultes.objects.filter(codi=numero) 
    return render(request, 'ruleta_c/query_roulette.html',{'consulta':consulta})
