from django.db import models
from .cad_lat_long import Local

class Usuario(models.Model):

    nome = models.CharField(max_length=100, null=True)
    senha = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=100, null=True)
    pais = models.CharField(max_length=40, null=True)
    estado = models.CharField(max_length=40, null=True)
    cidade = models.CharField(max_length=40, null=True)
    endereco = models.CharField(max_length=70, null=True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    dataConta = models.DateTimeField(auto_now_add=True)

