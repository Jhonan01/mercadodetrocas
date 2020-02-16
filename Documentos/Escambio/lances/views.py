from django.shortcuts import render
from lances.views import *
from lances.form import *
from itens.models import *
from lances.models import *


def lances(request):

    if (type((request.session.session_key)) == type('chave')):

        lances_tudo = []

        lances_enviados = Lances.objects.filter(id_usuario_ofertas_enviada = request.session['sessionid'])
        lances_recebidos = Lances.objects.filter(id_usuario_ofertas_recebida = request.session['sessionid'])


    else:
        return render(request, 'lances/lances.html', { })

    return render(request, 'lances/lances.html', {'lances_recebidos':lances_recebidos, 'lances_enviados':lances_enviados, })


def lance_enviado(request):

    data = {}

    form = Incluir_lancesForm(request.POST or None)

    data['form'] = form

    formUpdate = form.save(commit=False)

    formUpdate.id_usuario_ofertas_recebida = request.GET['id_usuario_alvo']
    formUpdate.id_item_oferta_recebida = request.GET['id_item_alvo']
    formUpdate.id_usuario_ofertas_enviada = request.session['sessionid']
    formUpdate.id_item_oferta_enviada = request.GET['id_item_meu']

    item_oferta_enviada = Incluir_item.objects.filter(id = request.GET['id_item_meu'])
    item_oferta_recebida = Incluir_item.objects.filter(id=request.GET['id_item_alvo'])

    for i in item_oferta_enviada:

        formUpdate.categorias_1 = i.categorias
        formUpdate.descricao_1 = i.descricao
        formUpdate.imagem1_1 = i.imagem1
        formUpdate.imagem2_1 = i.imagem2
        formUpdate.imagem3_1 = i.imagem3
        formUpdate.imagem4_1 = i.imagem4
        formUpdate.imagem5_1 = i.imagem5
        formUpdate.latitude_1 = i.latitude
        formUpdate.longitude_1 = i.longitude
        formUpdate.titulo_1 = i.titulo
        formUpdate.visualizado_1 = i.visualizado


    for a in item_oferta_recebida:

        formUpdate.categorias_2 = a.categorias
        formUpdate.descricao_2 = a.descricao
        formUpdate.imagem1_2 = a.imagem1
        formUpdate.imagem2_2 = a.imagem2
        formUpdate.imagem3_2 = a.imagem3
        formUpdate.imagem4_2 = a.imagem4
        formUpdate.imagem5_2 = a.imagem5
        formUpdate.latitude_2 = a.latitude
        formUpdate.longitude_2 = a.longitude
        formUpdate.titulo_2 = a.titulo
        formUpdate.visualizado_2 = a.visualizado


    formUpdate.save()

    return render(request, 'lances/lance_enviado.html')


def meus_itens(request):

    if (type((request.session.session_key)) == type('chave')):

        buscar = Incluir_item.objects.filter(id_usuario_item_id=request.session['sessionid'])

        meus_itens = {'buscar': buscar, 'inf1':request.GET['id_usuario_alvo'], 'inf2':request.GET['id_item_alvo'] }

        return render(request, 'lances/meus_itens.html' ,meus_itens)

    else:
        return render(request, 'blocos/login.html')




