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
<<<<<<< HEAD
=======
    dataP2 = []
    dataP3 = []
>>>>>>> 5a63809f2124d34cb4528cd7a3cfc8b2fdfce612

    buscar = Incluir_item.objects.all()

    for obj in buscar:
        contar = 0
        for i in request.GET['pesquisa'].split(' '):
            for objS in obj.titulo.split(' '):
                if(objS == i):
                    contar = contar+1



<<<<<<< HEAD
=======


>>>>>>> 5a63809f2124d34cb4528cd7a3cfc8b2fdfce612
        if(contar > 0):
            obj.peso = contar
            data.append(obj)

    data.sort(key=lambda x:x.peso, reverse=True)

    return render(request, 'buscar/buscar.html', {'dic':data})
