from django.db import models

# Create your models here.
class portafolio (models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="blog")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)

class inicio (models.Model):
    contenido=models.TextField()
    fechacreacion = models.DateTimeField(auto_now_add=True)


class producto (models.Model):
    nombre=models.CharField(max_length=100)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="blog")
