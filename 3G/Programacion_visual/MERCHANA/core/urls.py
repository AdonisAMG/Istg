from django.urls import path
from . import views
from .views import noticiasListview,noticiasGuardarCreateView,noticiasModificarUpdateview,noticiasBorrarDeleteview
from django.conf import settings


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('noticias', views.noticias, name='noticias'),

    path('deportes', views.deportes, name='deportes'),

    path('farandula', views.farandula, name='farandula'),

    path('email',views.email,name='email'),

    path('contacto',views.contacto,name='contacto'),

    path('noticiasAgregar/', views.addnoticias, name='noticiasAgregar'),

    path('noticiasmodificar/<int:id>', views.addmodificar, name='noticiasmodificar'),

    path('noticiaeliminar/<int:id>',views.eliminarnoticia,name='noticiaeliminar'),

    path('login/', views.login, name='login'),

    # llamar a las vistas de clases
    path('noticiasListview/',noticiasListview.as_view(),name='noticiasListview'),

    path('noticiasCreateview/',noticiasGuardarCreateView.as_view(),name='noticiasCreateview'),

    path('noticiasUpdateView/<int:pk>',noticiasModificarUpdateview.as_view(),name='noticiasUpdateView'),

    path('noticiasDeleteview/<int:pk>',noticiasBorrarDeleteview.as_view(),name='noticiasDeleteview'),






    #herencias
    path('inicioH',views.inicioH, name='inicioH'),

    path('deportesH', views.deportesH, name='deportesH'),

    path('farandulaH', views.farandulaH, name='farandulaH'),

    path('noticiasH', views.noticiasH, name='noticiasH'),

]