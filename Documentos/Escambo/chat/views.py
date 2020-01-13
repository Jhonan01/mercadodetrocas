# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from contas.models import *

def index(request):

    nome_usuario = Usuario.objects.filter(id = request.session['sessionid'])

    return render(request, 'chat/index.html', { 'nome_usuario':nome_usuario })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def nome(request):

    nome = request.session['sessionid']

    return render(request, nome)