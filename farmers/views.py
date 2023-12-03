from django.shortcuts import render
from project import settings
from .models import Animal

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

