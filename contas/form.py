from django import forms
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'senha', 'email','latitude','longitude']
    nome = forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class' : 'validade'}))
    senha = forms.CharField(label='Senha', max_length=100,widget=forms.TextInput(attrs={'class' : 'validade'}))
    email = forms.CharField(label='Email', max_length=100,widget=forms.TextInput(attrs={'class' : 'validade'}))
    latitude = forms.FloatField(label='Latitude', widget = forms.HiddenInput(), required = False)
    longitude =forms.FloatField(label='Longitude', widget = forms.HiddenInput(), required = False)