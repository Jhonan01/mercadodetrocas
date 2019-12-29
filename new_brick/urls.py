"""new_brick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import cadastro, cadastro_enviado, login_efetuado
from itens.views import incluir_item, item_enviado
from index.views import index, buscando, buscar
<<<<<<< HEAD
from django.conf.urls.static import static

=======
>>>>>>> 5a63809f2124d34cb4528cd7a3cfc8b2fdfce612

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro),
    path('cadastro_enviado/', cadastro_enviado),
    path('incluir_item/', incluir_item),
    path('item_enviado/', item_enviado),
    path('login/', cadastro),
    path('', index),
    path('buscando/', buscando),
    path('login_efetuado/', login_efetuado),
<<<<<<< HEAD
    path('buscar/', buscar),


=======
    path('buscar/', buscar)
>>>>>>> 5a63809f2124d34cb4528cd7a3cfc8b2fdfce612
]
