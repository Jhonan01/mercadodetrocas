from django.shortcuts import render
from .form import Incluir_itemForm
import base64
from contas.views import *
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def incluir_item(request):

    data = {}

    form = Incluir_itemForm(request.POST or None, request.FILES or None)

    data['form'] = form

    erros = " "

    if request.POST:

        formUpdate = form.save(commit=False)

        name = request.FILES['imagem1'].name
        name2 = request.FILES['imagem2'].name
        name3 = request.FILES['imagem3'].name
        name4 = request.FILES['imagem4'].name
        name5 = request.FILES['imagem5'].name

        imageName = name.split('.')
        imageName2 = name2.split('.')
        imageName3 = name3.split('.')
        imageName4 = name4.split('.')
        imageName5 = name5.split('.')

        if(len(imageName) > 2 or len(imageName2) > 2 or len(imageName3) > 2 or len(imageName4) > 2 or len(imageName5) > 2):

            erros = "Caracter indesejavel"

            return render(request, 'incluir_item/incluir_item.html', data, erros)

        #imageName[0] = base64.b64encode(request.FILES['imagem1'].name.encode())
        #imageName2[0] = base64.b64encode(request.FILES['imagem2'].name.encode())
        #imageName3[0] = base64.b64encode(request.FILES['imagem3'].name.encode())
        #imageName4[0] = base64.b64encode(request.FILES['imagem4'].name.encode())
        #imageName5[0] = base64.b64encode(request.FILES['imagem5'].name.encode())

        if(imageName[1] == "jpeg" or imageName[1] == "png" or imageName[1] == "gif" or imageName[1] == "jpg" and imageName2[1] == "jpeg" or imageName2[1] == "png" or imageName2[1] == "gif" or imageName2[1] == "jpg" and imageName3[1] == "jpeg" or imageName3[1] == "png" or imageName3[1] == "gif" or imageName3[1] == "jpg" and imageName4[1] == "jpeg" or imageName4[1] == "png" or imageName4[1] == "gif" or imageName4[1] == "jpg" and imageName5[1] == "jpeg" or imageName5[1] == "png" or imageName5[1] == "gif" or imageName5[1] == "jpg"):

            #formUpdate.imagem1 = str(imageName[0]) + "." + str(imageName[1])
            #formUpdate.imagem2 = str(imageName2[0]) + "." + str(imageName2[1])
            #formUpdate.imagem3 = str(imageName3[0]) + "." + str(imageName3[1])
            #formUpdate.imagem4 = str(imageName4[0]) + "." + str(imageName4[1])
            #formUpdate.imagem5 = str(imageName5[0]) + "." + str(imageName5[1])


            try:
                formUpdate.latitude = Usuario.objects.get(id=request.session['sessionid']).latitude
                formUpdate.longitude = Usuario.objects.get(id=request.session['sessionid']).longitude

            except MyModel.DoesNotExist:

                pass

            formUpdate.id_usuario_item_id = request.session['sessionid']

            formUpdate.save()

            return render(request, 'incluir_item/item_enviado.html')
        else:

            return render(request, 'incluir_item/incluir_item.html', data, erros)

    return render(request, 'incluir_item/incluir_item.html', data, erros)


def item_enviado(request):

    return render(request, "incluir_item/item_enviado.html")