from django.shortcuts import render

def query_roulette(request):
    return render(request, 'ruleta_c/query_roulette.html',{})
