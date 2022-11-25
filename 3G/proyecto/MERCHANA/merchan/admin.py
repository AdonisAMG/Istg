from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Hospital)
admin.site.register(Sucursal)
admin.site.register(Producto)
admin.site.register(Cita_medica)
admin.site.register(Cita_medica_tratamiento)
