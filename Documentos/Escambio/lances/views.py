from django.shortcuts import render
from lances.views import *
from lances.form import *
from itens.models import *
from lances.models import *


def lances(request):

    if (type((request.session.session_key)) == type('chave')):

        lancesTudo = []

        id_itens_lances_enviados_objetos1 = []
        id_itens_lances_recebidos_objetos1 = []

        lances_enviados = Lances.objects.filter(id_usuario_ofertas_enviada = request.session['sessionid'])
        lances_recebidos = Lances.objects.filter(id_usuario_ofertas_recebida = request.session['sessionid'])

        for i in range(len(lances_enviados)):

            id_itens_lances_enviados_objetos1.append(Incluir_item.objects.filter(id = lances_enviados[i].id_item_oferta_enviada))
            id_itens_lances_enviados_objetos1.append(Incluir_item.objects.filter(id = lances_enviados[i].id_item_oferta_recebida))


        for a in range(len(lances_recebidos)):

            id_itens_lances_recebidos_objetos1.append(Incluir_item.objects.filter(id = lances_recebidos[a].id_item_oferta_enviada))
            id_itens_lances_recebidos_objetos1.append(Incluir_item.objects.filter(id = lances_recebidos[a].id_item_oferta_recebida))


        lancesTudo = {

            'id_itens_lances_enviados_objetos1':id_itens_lances_enviados_objetos1,
            'id_itens_lances_recebidos_objetos1':id_itens_lances_recebidos_objetos1,

        }

        tudo = []

        tudo.append(lancesTudo)

        tudo_concatenado = []

        tudo_concatenado = {

            'tudo_concatenado':tudo

        }
    else:
        return render(request, 'lances/lances.html', { })

    return render(request, 'lances/lances.html', tudo_concatenado)


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

    if (type((request.session.session_key)) == type('chave')):

        buscar = Incluir_item.objects.filter(id_usuario_item_id=request.session['sessionid'])

        meus_itens = {'buscar': buscar, 'inf1':request.GET['id_usuario_alvo'], 'inf2':request.GET['id_item_alvo'] }

        return render(request, 'lances/meus_itens.html' ,meus_itens)

    else:
        return render(request, 'blocos/login.html')




