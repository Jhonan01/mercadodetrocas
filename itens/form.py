from django.forms import ModelForm
from .models import Incluir_item

class Incluir_itemForm(ModelForm):
    class Meta:
        model = Incluir_item

        fields = ['titulo', 'descricao', 'imagem1', 'imagem2', 'imagem3', 'imagem4', 'imagem5', 'categorias']

