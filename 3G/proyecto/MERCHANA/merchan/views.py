from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def publico(request):
    return render(request,'publico.html')

def inicio(request):
    return render(request,'inicio.html')

def login(request):
    form = usuarioform()
    if request.method == "POST":
        form = usuarioform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                return redirect("inicio")
    return render(request, 'login.html', {'form': form})

# ------Vistas basadas en clases----------

class cita_medica(ListView):
    model = Cita_medica
    paginate_by = 10
    template_name = 'cita_medica.html'

class citaguardar(CreateView):
    model = Cita_medica
    form_class = citaformulario
    template_name = 'citaguardar.html'
    def get_success_url(self):
        return reverse_lazy('cita_medica')

class citamodificar(UpdateView):
    model = Cita_medica
    form_class = citaformulario
    template_name = 'citaModificar.html'
    def get_success_url(self):
        return reverse_lazy('cita_medica')

class citaborrar(DeleteView):
    model = Cita_medica
    template_name = 'citaborrar.html'
    success_url = reverse_lazy('cita_medica')




class cita_medica_tratamiento(ListView):
    model = Cita_medica_tratamiento
    paginate_by = 10
    template_name = 'cita_medica_tratamiento.html'

class tratamientoguardar(CreateView):
    model = Cita_medica_tratamiento
    form_class = tratamientoformulario
    template_name = 'tratamientoguardar.html'
    def get_success_url(self):
        return reverse_lazy('cita_medica_tratamiento')

class tratamientomodificar(UpdateView):
    model = Cita_medica_tratamiento
    form_class = tratamientoformulario
    template_name = 'tratamientomodificar.html'
    def get_success_url(self):
        return reverse_lazy('cita_medica_tratamiento')

class tratamientoborrar(DeleteView):
    model = Cita_medica_tratamiento
    template_name = 'tratamientoborrar.html'
    success_url = reverse_lazy('cita_medica_tratamiento')




class hospital(ListView):
    model = Hospital
    paginate_by = 10
    template_name = 'hospital.html'

class hospitalguardar(CreateView):
    model = Hospital
    form_class = hospitalformulario
    template_name = 'hospitalguardar.html'
    def get_success_url(self):
        return reverse_lazy('hospital')

class hospitalmodificar(UpdateView):
    model = Hospital
    form_class = hospitalformulario
    template_name = 'hospitalmodificar.html'
    def get_success_url(self):
        return reverse_lazy('hospital')

class hospitalborrar(DeleteView):
    model = Hospital
    template_name = 'hospitalborrar.html'
    success_url = reverse_lazy('hospital')




class sucursal(ListView):
    model = Sucursal
    paginate_by = 10
    template_name = 'sucursal.html'

class sucursalguardar(CreateView):
    model = Sucursal
    form_class = sucursalformulario
    template_name = 'sucursalguardar.html'
    def get_success_url(self):
        return reverse_lazy('sucursal')

class sucursalmodificar(UpdateView):
    model = Sucursal
    form_class = sucursalformulario
    template_name = 'sucursalmodificar.html'
    def get_success_url(self):
        return reverse_lazy('SucursalListview')

class sucursalborrar(DeleteView):
    model = Sucursal
    template_name = 'sucursalborrar.html'
    success_url = reverse_lazy('sucursal')




class paciente(ListView):
    model = Paciente
    paginate_by = 10
    template_name = 'paciente.html'

class pacienteguardar(CreateView):
    model = Paciente
    form_class = pacienteformulario
    template_name = 'pacienteguardar.html'
    def get_success_url(self):
        return reverse_lazy('paciente')

class pacientemodificar(UpdateView):
    model = Paciente
    form_class = pacienteformulario
    template_name = 'pacientemodificar.html'
    def get_success_url(self):
        return reverse_lazy('paciente')

class pacienteborrar(DeleteView):
    model = Paciente
    template_name = 'pacienteborrar.html'
    success_url = reverse_lazy('paciente')




class doctor(ListView):
    model = Doctor
    paginate_by = 10
    template_name = 'doctor.html'

class doctorguardar(CreateView):
    model = Doctor
    form_class = doctorformulario
    template_name = 'doctorguardar.html'
    def get_success_url(self):
        return reverse_lazy('doctor')

class doctormodificar(UpdateView):
    model = Doctor
    form_class = doctorformulario
    template_name = 'doctormodificar.html'
    def get_success_url(self):
        return reverse_lazy('doctor')

class doctorborrar(DeleteView):
    model = Doctor
    template_name = 'doctorborrar.html'
    success_url = reverse_lazy('doctor')



class producto(ListView):
    model = Producto
    paginate_by = 10
    template_name = 'producto.html'

class productoguardar(CreateView):
    model = Producto
    form_class = productoformulario
    template_name = 'productoguardar.html'
    def get_success_url(self):
        return reverse_lazy('producto')

class productomodificar(UpdateView):
    model = Producto
    form_class = productoformulario
    template_name = 'productomodificar.html'
    def get_success_url(self):
        return reverse_lazy('producto')

class producoborrar(DeleteView):
    model = Producto
    template_name = 'productoborrar.html'
    success_url = reverse_lazy('producto')

