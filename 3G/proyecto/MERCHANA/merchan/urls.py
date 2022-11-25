from django.urls import path
from . import views
from .views import *
from django.conf import settings

urlpatterns = [
    path('', views.publico, name='publico'),
    path('Inicio', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    # llamar a las vistas de clases
    path('Cita Medica/',cita_medica.as_view(),name='cita_medica'),
    path('Crear Cita/',citaguardar.as_view(),name='citaguardar'),
    path('Modificar Cita/<int:pk>',citamodificar.as_view(),name='citamodificar'),
    path('Borrar Cita/<int:pk>', citaborrar.as_view(),name='citaborrar'),

    path('Tratamiento/',cita_medica_tratamiento.as_view(),name='cita_medica_tratamiento'),
    path('Crear Tratamiento/',tratamientoguardar.as_view(),name='tratamientoguardar'),
    path('Modificar Tratamiento/<int:pk>',tratamientomodificar.as_view(),name='tratamientomodificar'),
    path('Borrar Tratamiento/<int:pk>',tratamientoborrar.as_view(),name='tratamientoborrar'),

    path('Hospital/',hospital.as_view(),name='hospital'),
    path('Crear Hospital/', hospitalguardar.as_view(),name='hospitalguardar'),
    path('Modificar Hospital/<int:pk>', hospitalmodificar.as_view(),name='hospitalmodificar'),
    path('Borrar Hospital/<int:pk>', hospitalborrar.as_view(),name='hospitalborrar'),

    path('Sucursal/',sucursal.as_view(),name='sucursal'),
    path('Crear Sucursal/',sucursalguardar.as_view(),name='sucursalguardar'),
    path('Modificar Sucursal/<int:pk>',sucursalmodificar.as_view(),name='sucursalmodificar'),
    path('Borrar Sucursal/<int:pk>', sucursalborrar.as_view(),name='sucursalborrar'),

    path('Paciente/',paciente.as_view(),name='paciente'),
    path('Crear Paciente/',pacienteguardar.as_view(),name='pacienteguardar'),
    path('Modificar Paciente/<int:pk>',pacientemodificar.as_view(),name='pacientemodificar'),
    path('Borrar Paciente/<int:pk>',pacienteborrar.as_view(),name='pacienteborrar'),

    path('Doctor/',doctor.as_view(),name='doctor'),
    path('Crear Doctor/',doctorguardar.as_view(),name='doctorguardar'),
    path('Modificar Doctor/<int:pk>',doctormodificar.as_view(),name='doctormodificar'),
    path('Borror Doctor/<int:pk>', doctorborrar.as_view(),name='doctorborrar'),

    path('Producto/',producto.as_view(),name='producto'),
    path('Crear Producto/',productoguardar.as_view(),name='productoguardar'),
    path('Modificar Producto/<int:pk>',productomodificar.as_view(),name='productomodificar'),
    path('Borrar Producto/<int:pk>',producoborrar.as_view(),name='productoborrar'),
    
]
