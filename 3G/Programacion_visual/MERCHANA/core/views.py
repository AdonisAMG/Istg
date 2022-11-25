from django.shortcuts import render, redirect
from .models import portafolio
from .models import noticiasM
from .models import inicioM
from .forms import Contactform,noticiasformulario,usuarioform
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def inicio(request):
    objCondatos=inicioM.objects.all()
    return render(request,'inicio.html',{'Enviainicio':objCondatos})

def deportes(request):
    return render(request,'deportes.html')

def farandula(request):
    return render(request,'farandula.html')

def email(request):
    return render(request,'email.html')


#------------herencia---------------

def inicioH(request):
    return render(request,'herencia/inicioH.html')

def noticiasH(request):
    return render(request,'herencia/noticiasH.html')

def deportesH(request):
    return render(request,'herencia/deportesH.html')

def farandulaH(request):
    return render(request,'herencia/farandulaH.html')


def blog (request):
    select=portafolio.objects.all()
    return render(request,'blog.html',{"Enviablog":select})

#------------------------------------------------------
def contacto(request):
    objcontacto=Contactform()
    print("Valida post")
    if request.method=="POST":
        objcontacto=Contactform(request.POST)
        print("carga datos post")
        if objcontacto.is_valid():
            print(objcontacto)
    return render(request,'contacto.html',{"forms":objcontacto})



# Create your views here.
def noticias(request):
    objCondatos=noticiasM.objects.all()
    if request.method=="POST":
        titulo=request.POST.get('titulo')
        if titulo=='':
           print("Espacio en Blanco")
        else:
            print("Debe realizar la busqueda por el titulo")
            objCondatos=noticiasM.objects.filter(titulo=titulo)
    return render(request,'noticias.html',{'Enviablog':objCondatos})


def addnoticias(request):
    #creamos un formulario vacio
    form= noticiasformulario()
    #Comprobamos si se ha enviado el formulario
    if request.method=="POST":
        #Añadir los datos recibidos del formulario
        form=noticiasformulario(request.POST,request.FILES)
        #Si el formulario es valido
        if form.is_valid():
            # guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia=form.save(commit=False)
            #Podemos guardarla cuando queramos
            instancia.save()
            #Luego de Grabar redireccionamos a la lista
            return redirect('/')
    print("Presiono Guardar")
    #si llegamos al final renderisamos el formulario
    return render(request,'noticiasAgregar.html',{'form':form})

def addmodificar(request,id):
    instancia=noticiasM.objects.get(id=id)
    #creamos un formulario vacio
    form= noticiasformulario(instance=instancia)
    #Comprobamos si se ha enviado el formulario
    if request.method=="POST":
        #Añadir los datos recibidos del formulario
        form=noticiasformulario(request.POST,instance=instancia)
        #Si el formulario es valido
        if form.is_valid():
            # guardamos el formulario pero sin confirmarlo, asi conseguiremos una instancia para manejarla
            instancia=form.save(commit=False)
            #Podemos guardarla cuando queramos
            instancia.save()
            #Luego de Grabar redireccionamos a la lista
            return redirect('/')
    print("Presiono Modificar")
    #si llegamos al final renderisamos el formulario
    return render(request,'noticiasModificar.html',{'form':form})


def eliminarnoticia(request,id):
    instancia=noticiasM.objects.get(id=id)
    instancia.delete()
    return redirect('/')


def login(request):
    #creamos el formulario de autentificacion vacio
    form=usuarioform()
    if request.method=="POST":
        #Añadimos los datos recibidos al formulario
        form=usuarioform(request.POST)
        if form.is_valid():
            #Recuperamos las credenciales validadas
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                return redirect("noticias")
    return render(request,'login.html', {'form': form})


#------Vistas basadas en clases----------

class noticiasListview(ListView):
    model = noticiasM
    paginate_by = 10
    template_name = 'noticiasvistaclase.html'

class noticiasGuardarCreateView(CreateView):
    model = noticiasM
    form_class = noticiasformulario
    template_name ='noticiasGuardarClase.html'
    def get_success_url(self):
        return reverse_lazy('noticiasListview')

class noticiasModificarUpdateview(UpdateView):
    model = noticiasM
    form_class = noticiasformulario
    template_name = 'noticiasModificarClase.html'
    def get_success_url(self):
        return reverse_lazy('noticiasListview')

class noticiasBorrarDeleteview(DeleteView):
    model = noticiasM
    template_name = 'noticiasEliminarClase.html'
    success_url = reverse_lazy('noticiasListview')
