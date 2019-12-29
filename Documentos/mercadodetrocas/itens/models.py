from django.db import models
from contas.models import Usuario

class Incluir_item(models.Model):

    catEscolhas = (

        ('Tecnologia' , 'Tecnologia'),
        ('Automóvel', 'Automóvel'),
        ('Mobiliarios', 'Mobiliarios'),
        ('Imovel', 'Imovel'),
        ('Animais', 'Animais'),
        ('Beleza', 'Beleza'),
        ('Moda', 'Moda'),
        ('Esporte', 'Esporte'),
        ('Brinquedo', 'Brinquedo'),
        ('Jóias e relógios', 'Jóias e relógios'),
        ('Ferramentas e Indústria', 'Ferramentas e Indústria'),
        ('Supermercado', 'Supermercado'),

    )

    titulo = models.CharField(max_length=30)
    descricao = models.TextField(max_length=200)
    id_usuario_item_id = models.IntegerField(null = True)
    dataConta = models.DateTimeField(auto_now_add=True)
    imagem1 = models.ImageField(upload_to='static/img/produtos/')
    imagem2 = models.ImageField(upload_to='static/img/produtos/')
    imagem3 = models.ImageField(upload_to='static/img/produtos/')
    imagem4 = models.ImageField(upload_to='static/img/produtos/')
    imagem5 = models.ImageField(upload_to='static/img/produtos/')
    visualizado = models.IntegerField(null=True, default=0)
    categorias = models.CharField(max_length=50, null=True, choices=catEscolhas)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
