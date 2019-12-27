from django.shortcuts import render
from passlib.hash import pbkdf2_sha256
from typing import Any

from itens.models import *

def index(request):

    return render(request, 'index.html')



def login(request):
    return render(request, 'blocos/login.html')


def buscando(request):
    return render(request, 'buscando/buscando.html')

def buscar(request):

    data = []

    buscar = Incluir_item.objects.all()

    for obj in buscar:
        contar = 0
        for i in request.GET['pesquisa'].split(' '):
            for objS in obj.titulo.split(' '):
                if(objS == i):
                    contar = contar+1



        if(contar > 0):
            obj.peso = contar
            data.append(obj)

    data.sort(key=lambda x:x.peso, reverse=True)

    return render(request, 'buscar/buscar.html', {'dic':data})
