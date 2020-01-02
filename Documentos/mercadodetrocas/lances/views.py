from django.shortcuts import render
from lances.views import *
from lances.form import *
from itens.models import *
from lances.models import *


def lances(request):

    lancesTudo = []

    lances_enviados = Lances.objects.filter(id_usuario_ofertas_enviada = request.session['sessionid'])

    for i in lances_enviados:
        itens_enviados = Incluir_item.objects.filter(id = i.id_item_oferta_enviada)
        itens_recebidos = Incluir_item.objects.filter(id = i.id_item_oferta_recebida)


        lances = {

            "itens_enviados": itens_enviados,
            "itens_recebidos": itens_recebidos,

        }

        lancesTudo.append(lances)

        print(lances)


    return render(request, 'lances/lances.html', lances)


def lance_enviado(request):

    data = {}

    form = Incluir_lancesForm(request.POST or None)

    data['form'] = form

    formUpdate = form.save(commit=False)

    formUpdate.id_usuario_ofertas_recebida = request.GET['id_usuario_alvo']
    formUpdate.id_item_oferta_recebida = request.GET['id_item_alvo']
    formUpdate.id_usuario_ofertas_enviada = request.session['sessionid']
    formUpdate.id_item_oferta_enviada = request.GET['id_item_meu']

    formUpdate.save()

    return render(request, 'lances/lance_enviado.html')


def meus_itens(request):

    buscar = Incluir_item.objects.filter(id_usuario_item_id=request.session['sessionid'])

    meus_itens = {'buscar': buscar, 'inf1':request.GET['id_usuario_alvo'], 'inf2':request.GET['id_item_alvo'] }

    return render(request, 'lances/meus_itens.html' ,meus_itens)



