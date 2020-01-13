from django.shortcuts import render
from .form import UsuarioForm
from django.contrib.auth import authenticate
from contas.models import *
from .cad_lat_long import Local
from opencage.geocoder import OpenCageGeocode

from passlib.hash import pbkdf2_sha256

global armLat
global armLong

from .models import Usuario


def cadastro(request):

    data = {}

    form = UsuarioForm(request.GET or None)

    data['form'] = form
    if request.GET:
        '''
        local = (request.GET['pais'] , "," , request.GET['estado'] , ","  , request.GET['cidade'] , ","  , request.GET['endereco'])

        localT = ""
        for i in range(7):

            localT += local[i]
        key = '6940adf71cd14d6697323d05946d7388'

        geocoder = OpenCageGeocode(key)

        query = localT

        result = geocoder.geocode(query)

        armLat = result[0]['geometry']['lat']
        armLong = result[0]['geometry']['lng']


        geoForm = form.save(commit=False)

        geoForm.latitude = armLat
        geoForm.longitude = armLong
        geoForm.save() 
        '''

        formUpdate = form.save(commit=False)

        formUpdate.senha = pbkdf2_sha256.hash(request.GET['senha'])
        formUpdate.save()
        #form.save()
        
        return cadastro_enviado(request)

    return render(request, 'blocos/login.html', data)

def cadastro_enviado(request):

        return render(request, 'blocos/login.html')



def login(request):

    return render(request, 'login/login.html')

def login_efetuado(request):

    if (request.method == 'GET'):

        buscar = Usuario.objects.all()


        for i in buscar:
            if(request.GET['email'] == i.email):
                if(pbkdf2_sha256.verify(request.GET['senha'], i.senha) == True):


                    request.session['sessionid'] = i.id
                    nome_logado = {}
                    nome_logado['logado'] = i.nome
                    nome_logado['email'] = i.email

                    return render(request, 'blocos/login_efetuado.html', nome_logado)


    return render(request, 'blocos/login.html')