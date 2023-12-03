from django.db import models

class Coordenada(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
