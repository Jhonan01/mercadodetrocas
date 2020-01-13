from django.db import models

class Chat(models.Model):

    id_usuario_lancador = models.IntegerField(null=True)
    id_usuario_receptor = models.IntegerField(null=True)
    chat_text = models.TextField(max_length=5000, null=True)
    proposta_aceita = models.DateTimeField(auto_now_add=True)
    endereco_url = models.TextField(max_length=300, null=True)


