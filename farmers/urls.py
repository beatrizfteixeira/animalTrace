from django.urls import path
from . import views
from .views import recebe_coordenadas

urlpatterns = [
    path('mapa', views.mapa, name='mapa'),
    path('', views.login , name='login'),
    path('signup', views.signup, name='signup'),
    path('coordenadas/', recebe_coordenadas, name='coordenadas')
]
