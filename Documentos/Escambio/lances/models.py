from django.db import models



class Lances(models.Model):

    id_usuario_ofertas_recebida = models.IntegerField(null=True)
    id_usuario_ofertas_enviada = models.IntegerField(null=True)
    id_item_oferta_recebida = models.IntegerField(null=True)
    id_item_oferta_enviada = models.IntegerField(null=True)
    data_da_oferta = models.DateTimeField(auto_now_add=True)
    titulo_1 = models.CharField(max_length=30, null=True)
    descricao_1 = models.TextField(max_length=200, null=True)
    imagem1_1 = models.ImageField(max_length=30, null=True)
    imagem2_1 = models.ImageField(max_length=30, null=True)
    imagem3_1 = models.ImageField(max_length=30, null=True)
    imagem4_1 = models.ImageField(max_length=30, null=True)
    imagem5_1 = models.ImageField(max_length=30, null=True)
    visualizado_1 = models.IntegerField(null=True, default=0)
    categorias_1 = models.CharField(max_length=50, null=True)
    latitude_1 = models.FloatField(null=True)
    longitude_1 = models.FloatField(null=True)
    titulo_2 = models.CharField(max_length=30, null=True)
    descricao_2 = models.TextField(max_length=200, null=True)
    imagem1_2 = models.CharField(max_length=30, null=True)
    imagem2_2 = models.CharField(max_length=30, null=True)
    imagem3_2 = models.CharField(max_length=30, null=True)
    imagem4_2 = models.CharField(max_length=30, null=True)
    imagem5_2 = models.CharField(max_length=30, null=True)
    visualizado_2 = models.IntegerField(null=True, default=0)
    categorias_2 = models.CharField(max_length=50, null=True)
    latitude_2 = models.FloatField(null=True)
    longitude_2 = models.FloatField(null=True)
