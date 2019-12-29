from django.forms import ModelForm
from .models import Lances

class Incluir_lancesForm(ModelForm):
    class Meta:
        model = Lances

        fields = ['id_usuario_ofertas_recebida', 'id_usuario_ofertas_enviada', 'id_item_oferta_recebida', 'id_item_oferta_enviada']