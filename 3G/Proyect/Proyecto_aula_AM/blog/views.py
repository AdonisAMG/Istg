from django.shortcuts import render
from .models import portafolio
from .models import inicio
from .models import producto


# Create your views here.
def blog (request):
    select=portafolio.objects.all()
    return render(request,'blog.html',{"Enviablog":select})

def proyecto(request):
    select=inicio.objects.all()
    return render(request,'inicio.html',{"Enviai":select})

def nuestros_productos(request):
    select=producto.objects.all()
    return render(request,'nuestros_productos.html',{"Enviap":select})

def quienes_somos(request):
    return render(request,'quienes_somos.html')

def contactanos(request):
    return render(request,'contactos.html')

def QUIENES__SOMOS(request):
    return render(request,'QUIENES SOMOS.html')
