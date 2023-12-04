from django.urls import path

from . import views

urlpatterns = [    
    path('mapa', views.mapa, name='mapa'),
    path('login', views.login , name='login'),
    path('signup', views.signup, name='signup'),
    path('animal', views.animal, name='animal'),
    path('coordenadas/', views.recebe_coordenadas, name='coordenadas'),
    path('mapa_controle', views.mapa_controle, name='controle'),
    path('obter_coordenadas/', views.obter_coordenadas, name='obter_coordenadas')
]
