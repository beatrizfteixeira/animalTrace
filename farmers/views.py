from django.shortcuts import render
from project import settings

def mapa(request):
    context = {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'mapa.html', context)
