from django.shortcuts import render
from passlib.hash import pbkdf2_sha256
from typing import Any
from index.models import *
from lances.models import *
from itens.models import *
from contas.models import *

def index(request):

    if(type((request.session.session_key)) == type('chave')):

        nome_usuario = Usuario.objects.filter(id=request.session['sessionid'])

        if(request.GET):

            checar_url = len(Chat.objects.all())+1

            concatenar_url = 'http://127.0.0.1:8000/chat/'+str(checar_url)

            chat_update = Chat(

                id_usuario_lancador = request.GET['id_usuario_lancador'],
                id_usuario_receptor = request.session['sessionid'],
                chat_text = ' ',
                endereco_url = concatenar_url,
                id_usuario_item_lancador = request.GET['id_usuario_item_lancador'],
                id_usuario_item_receptor = request.GET['id_item_receptor'],
                titulo_1 = request.GET['titulo1'],
                titulo_2 = request.GET['titulo2'],
                descricao_1 = request.GET['descricao1'],
                descricao_2 = request.GET['descricao2'],
                imagem1_1 = request.GET['imagem11'],
                imagem2_1=request.GET['imagem21'],
                imagem3_1=request.GET['imagem31'],
                imagem4_1=request.GET['imagem41'],
                imagem5_1=request.GET['imagem51'],
                imagem1_2=request.GET['imagem12'],
                imagem2_2=request.GET['imagem22'],
                imagem3_2=request.GET['imagem32'],
                imagem4_2=request.GET['imagem42'],
                imagem5_2=request.GET['imagem52'],
                visualizado_1=request.GET['visualizado1'],
                visualizado_2=request.GET['visualizado2'],
                categorias_1=request.GET['categorias1'],
                categorias_2=request.GET['categorias2'],
                latitude_1=request.GET['latitude1'],
                latitude_2=request.GET['latitude2'],
                longitude_1=request.GET['longitude1'],
                longitude_2=request.GET['longitude2'],


            )

            chat_update.save()

        inf_chat_lances = []

        meus_contados_chat_receptado = Chat.objects.filter(id_usuario_receptor = request.session['sessionid'])
        meus_contados_chat_lancador = Chat.objects.filter(id_usuario_lancador=request.session['sessionid'])


        for i in meus_contados_chat_receptado:

            inf_chat_lances.append(i)

        for a in meus_contados_chat_lancador:

            inf_chat_lances.append(a)


        return render(request, 'index.html', { 'inf_chat_lances':inf_chat_lances })

    else:

        return render(request, 'index.html')


def login(request):
    return render(request, 'blocos/login.html')


def buscando(request):
    return render(request, 'buscando/buscando.html')

def buscar(request):

    data = []


    buscar = Incluir_item.objects.all()


    if (type((request.session.session_key)) == type('chave')):


        mudar_para_maiuscula = request.GET['pesquisa'].upper()

        meus_itens = Incluir_item.objects.filter(id_usuario_item_id=request.session['sessionid'])

        meus_lances = Lances.objects.filter(id_usuario_ofertas_enviada=request.session['sessionid'])


        for r in buscar:
            for z in meus_itens:
                if (z.id == r.id):
                    r.titulo = 'krfnrkjnvhjdijcukjjyjdyfjfyhf'

        for obj in buscar:
            contar = 0
            for i in mudar_para_maiuscula.split(' '):
                for objS in obj.titulo.split(' '):
                    if (objS == i):
                        contar = contar + 1

            if (contar > 0):
                obj.peso = contar
                data.append(obj)

        for i in meus_lances:

            for a in range(len(data) - 1, -1, -1):

                if(data[a].id == i.id_item_oferta_recebida):

                    del(data[a])




        data.sort(key=lambda x: x.peso, reverse=True)

        return render(request, 'buscar/buscar.html', {'dic': data})
    else:

        mudar_para_maiuscula = request.GET['pesquisa'].upper()

        for obj in buscar:
            contar = 0
            for i in mudar_para_maiuscula.split(' '):
                for objS in obj.titulo.split(' '):
                    if (objS == i):
                        contar = contar + 1

            if (contar > 0):
                obj.peso = contar
                data.append(obj)

        data.sort(key=lambda x: x.peso, reverse=True)

        return render(request, 'buscar/buscar.html', {'dic': data})

