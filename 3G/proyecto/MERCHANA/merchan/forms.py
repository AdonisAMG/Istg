from django import forms
from .models import *

class citaformulario(forms.ModelForm):
    class Meta:
        model = Cita_medica
        fields = ['doctor','paciente','motivo','hospital','sucursal']

class tratamientoformulario(forms.ModelForm):
    class Meta:
        model = Cita_medica_tratamiento
        fields = ['paciente','producto','cantidad','tratamiento']

class hospitalformulario(forms.ModelForm):
    class Meta:
        model= Hospital
        fields=['nombre','ubicacion','doctor','nmr_telefono','paciente','estado']

class sucursalformulario(forms.ModelForm):
    class Meta:
        model= Sucursal
        fields=['nombre','ubicacion','doctor','nmr_telefono','paciente','estado']

class pacienteformulario(forms.ModelForm):
    class Meta:
        model= Paciente
        fields=['nombres','apellidos','direccion','nmr_telefono','imagen']

class doctorformulario(forms.ModelForm):
    class Meta:
        model= Doctor
        fields=['nombresd','apellidosd','nmr_telefonod','imagend']

class productoformulario(forms.ModelForm):
    class Meta:
        model= Producto
        fields=['nombre','precio','imagen']

class usuarioform(forms.Form):
     username=forms.CharField(label="usuario",required=True,max_length=15)
     password=forms.CharField(label="clave",required=True,max_length=10)