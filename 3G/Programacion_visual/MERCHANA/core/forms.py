from django import forms
from .models import noticiasM

class Contactform(forms.Form):
    name=forms.CharField(label="Nombre",required=True)
    emai=forms.EmailField(label="Email",required=True)
    contenido=forms.CharField(label="Contenido",required=True)

class noticiasformulario(forms.ModelForm):
    class Meta:
        model= noticiasM
        fields=['titulo','contenido','imagen']


class usuarioform(forms.Form):
    username=forms.CharField(label="usuario",required=True,max_length=10)
    password=forms.CharField(label="clave",required=True,max_length=10)