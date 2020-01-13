from django.shortcuts import render
from passlib.hash import pbkdf2_sha256
from typing import Any
from index.models import *

from itens.models import *

def index(request):

    if(type((request.session.session_key)) == type('chave')):

        nome_usuario = Usuario.objects.filter(id=request.session['sessionid'])

        if(request.GET):

            checar_url = len(Chat.objects.all())

            concatenar_url = 'http://127.0.0.1:8000/chat/'+str(checar_url)

            chat_update = Chat(

                id_usuario_lancador = request.GET['id_usuario_lancador'],
                id_usuario_receptor = request.session['sessionid'],
                chat_text = ' ',
                endereco_url = concatenar_url


            )

            chat_update.save()


        return render(request, 'index.html', { 'nome_usuario':nome_usuario })

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

