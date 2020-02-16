# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from contas.models import *

def index(request):


    return render(request, 'chat/index.html')

def room(request, room_name):


    if(request.GET):

        return render(request, 'chat/room.html', {

                'imagens_mostrar': request.GET,
                'room_name_json': mark_safe(json.dumps(room_name))

        })
