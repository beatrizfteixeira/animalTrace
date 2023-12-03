from django.http import JsonResponse
from django.shortcuts import render
from project import settings
import json

def mapa(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'mapa.html', context)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def recebe_coordenadas(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'sucesso': data}, status=200)
    return JsonResponse({'error': 'erro'}, status=500)