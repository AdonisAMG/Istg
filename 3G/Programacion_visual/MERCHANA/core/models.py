from django.db import models
# Create your models here.
class portafolio (models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="blog")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)


# Create your models here.
class noticiasM(models.Model):
    titulo=models.CharField(max_length=200,verbose_name="Titulos-99")
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="noticias")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo

class inicioM(models.Model):
    titulo=models.CharField(max_length=200,verbose_name="Titulos-99")
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="inicio")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo