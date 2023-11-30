from django.urls import path
from . import views

urlpatterns = [
    path('mapa', views.mapa, name='ver google maps')
]
