from django.db import models



class Lances(models.Model):

    id_usuario_ofertas_recebida = models.IntegerField(null=True)
    id_usuario_ofertas_enviada = models.IntegerField(null=True)
    id_item_oferta_recebida = models.IntegerField(null=True)
    id_item_oferta_enviada = models.IntegerField(null=True)
    data_da_oferta = models.DateTimeField(auto_now_add=True)
