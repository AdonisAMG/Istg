from django import forms
from .models import *

class cita_formulario(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['doctor','paciente','motivo','hospital','sucursal']

class tratamiento_formulario(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['paciente','producto','cantidad','tratamiento']

class hospital_formulario(forms.ModelForm):
    class Meta:
        model= Hospital
        fields=['nombre','ubicacion','doctor','nmr_telefono','paciente','estado']

class sucursal_formulario(forms.ModelForm):
    class Meta:
        model= Sucursal
        fields=['nombre','ubicacion','doctor','nmr_telefono','paciente','estado']

class paciente_formulario(forms.ModelForm):
    class Meta:
        model= Paciente
        fields=['nombres','apellidos','direccion','nmr_telefono','imagen']

class doctor_formulario(forms.ModelForm):
    class Meta:
        model= Doctor
        fields=['nombresd','apellidosd','nmr_telefonod','imagend']

class producto_formulario(forms.ModelForm):
    class Meta:
        model= Producto
        fields=['nombre','precio','imagen']
