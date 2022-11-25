from django.urls import path
from . import views


urlpatterns = [
    path('', views.proyecto, name='inicio'),

    path('blog', views.blog, name='blog'),

    path('Quienes somos', views.quienes_somos, name='quienes_somos'),

    path('Nuestros Productos', views.nuestros_productos, name='nuestros_productos'),

    path('Contactanos', views.contactanos, name='contactanos'),

    path('QUIENES__SOMOS', views.QUIENES__SOMOS, name='QUIENES__SOMOS'),

]