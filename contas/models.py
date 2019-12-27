from django.db import models
from .cad_lat_long import Local

class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    pais = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    endereco = models.CharField(max_length=70, null=True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    dataConta = models.DateTimeField(auto_now_add=True)
