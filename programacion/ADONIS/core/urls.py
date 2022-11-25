from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # llamar a las vistas de clases
    path('Cita Medica',cita_medica_lista.as_view(),name='cita_medica'),
    path('Crear Cita',citaguardar.as_view(),name='citaguardar'),
    path('Modificar Cita/<int:pk>',citamodificar.as_view(),name='citamodificar'),
    path('Borrar Cita/<int:pk>', citaeliminar.as_view(),name='citaeliminar'),

    path('Tratamiento',tratamiento_lista.as_view(),name='tratamiento'),
    path('Crear Tratamiento',tratamientoguardar.as_view(),name='tratamientoguardar'),
    path('Modificar Tratamiento/<int:pk>',tratamientomodificar.as_view(),name='tratamientomodificar'),
    path('Borrar Tratamiento/<int:pk>',tratamientoeliminar.as_view(),name='tratamientoeliminar'),

    path('Hospital',hospital_lista.as_view(),name='hospital'),
    path('Crear Hospital', hospitalguardar.as_view(),name='hospitalguardar'),
    path('Modificar Hospital/<int:pk>', hospitalmodificar.as_view(),name='hospitalmodificar'),
    path('Borrar Hospital/<int:pk>', hospitaleliminar.as_view(),name='hospitalelminar'),

    path('Sucursal',sucursal_lista.as_view(),name='sucursal'),
    path('Crear Sucursal',sucursalguardar.as_view(),name='sucursalguardar'),
    path('Modificar Sucursal/<int:pk>',sucursalmodificar.as_view(),name='sucursalmodificar'),
    path('Borrar Sucursal/<int:pk>', sucursaleliminar.as_view(),name='sucursaleliminar'),

    path('Paciente',paciente_lista.as_view(),name='paciente_lista'),
    path('Crear Paciente',pacienteguardar.as_view(),name='pacienteguardar'),
    path('Modificar Paciente/<int:pk>',pacientemodificar.as_view(),name='pacientemodificar'),
    path('Borrar Paciente/<int:pk>',pacienteeliminar.as_view(),name='pacienteeliminar'),

    path('Doctor',doctor_lista.as_view(),name='doctor'),
    path('Crear Doctor',doctorguardar.as_view(),name='doctorguardar'),
    path('Modificar Doctor/<int:pk>',doctormodificar.as_view(),name='doctormodificar'),
    path('Borror Doctor/<int:pk>', doctoreliminar.as_view(),name='doctoreliminar'),

    path('Producto',producto_lista.as_view(),name='producto'),
    path('Crear Producto',productoguardar.as_view(),name='productoguardar'),
    path('Modificar Producto/<int:pk>',productomodificar.as_view(),name='productomodificar'),
    path('Borrar Producto/<int:pk>',productoeliminar.as_view(),name='productoeliminar'),
    
]
