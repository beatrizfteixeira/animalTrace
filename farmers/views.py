from django.http import JsonResponse
from django.shortcuts import render
from project import settings
from .models import Animal
from .models import Coordenada

import pyrebase

config ={
    "apiKey": "AIzaSyC0xzTA44qdc1hZg8HwiEDt-l7CT24DxJ8",
    "authDomain": "animaltrace-60936.firebaseapp.com",
    "databaseURL": "https://animaltrace-60936-default-rtdb.firebaseio.com",
    "projectId": "animaltrace-60936",
    "storageBucket": "animaltrace-60936.appspot.com",
    "messagingSenderId": "275508046720",
    "appId": "1:275508046720:web:0bf7473cc6cfdfd69d6f65"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
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

def animal(request):
    # Supondo que você tenha o endereço MAC do animal que deseja exibir
    mac_address = "48:E7:29:CB:0B:D4"

    # Consulta o banco de dados para obter a instância do Animal pelo endereço MAC
    animal_instance, created = Animal.objects.get_or_create(mac=mac_address)

    # Atualiza a latitude e a longitude com os dados do Firebase
    animal_instance.latitude = database.child(mac_address).child("latitude").get().val()
    animal_instance.longitude = database.child(mac_address).child("longitude").get().val()
    
    # Salva as alterações no banco de dados
    animal_instance.save()

    # Passa as informações para o template
    return render(request, 'animal.html', {
        "nome":animal_instance.nome,
        "latitude": animal_instance.latitude,
        "longitude": animal_instance.longitude
    })

def recebe_coordenadas(request):
    if request.method == 'POST':        
        Coordenada.objects.all().delete()
        json_data = json.loads(request.body.decode('utf-8'))
        for data in json_data:
            latitude = data['latitude']
            longitude = data['longitude']
            Coordenada.objects.create(latitude=latitude, longitude=longitude)
        return JsonResponse({'sucesso': json_data}, status=200)  

    return JsonResponse({'error': 'erro'}, status=500)

def obter_coordenadas(request):
    if request.method == 'GET':  
        coordenadas = Coordenada.objects.all().values()  # Converte as coordenadas em um dicionário
        return JsonResponse(list(coordenadas), safe=False)

def mapa_controle(request):
    # Obtenha as latitudes e longitudes do banco de dados ou de onde você as armazenou
    coordenadas = [{
                        'lat': -21.225307757471317,
                        'lng': -44.979793524328606
                    },
                    {
                        'lat': -21.225442771375494,
                        'lng': -44.97981229979171
                    },
                    {
                        'lat': -21.225450272144315,
                        'lng': -44.97961113411559
                    },
                    {
                        'lat': -21.225312757988497,
                        'lng': -44.979584312025445
                    }]

    # Passe as coordenadas para o template
    coordenadas_json = json.dumps(coordenadas)

    return render(request, 'mapa_controle.html', {'coordenadas_json': coordenadas_json})