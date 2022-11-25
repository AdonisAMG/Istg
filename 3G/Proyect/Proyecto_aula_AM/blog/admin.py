from django.contrib import admin
from .models import portafolio
from .models import inicio
from .models import producto

# Register your models here.
admin.site.register(portafolio)
admin.site.register(inicio)
admin.site.register(producto)
