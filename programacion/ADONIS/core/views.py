from .models import *
from .forms import matricula_formulario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class matricula_lista(ListView):
    model = MATRICULA
    paginate_by = 10
    template_name = 'matricula.html'

class matricula_guardar(CreateView):
    model = MATRICULA
    form_class = matricula_formulario
    template_name = 'matricula_guardar.html'
    def get_success_url(self):
        return reverse_lazy('matricula_lista')

class matricula_modificar(UpdateView):
    model = MATRICULA
    form_class = matricula_formulario
    template_name = 'matricula_modificar.html'
    def get_success_url(self):
        return reverse_lazy('matricula_lista')

class matricula_eliminar(DeleteView):
    model = MATRICULA
    template_name = 'matricula_eliminar.html'
    success_url = reverse_lazy('matricula_lista')
