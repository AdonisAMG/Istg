from django.db import models
# Create your models here.

class ALUMNO(models.Model):
    codigoest=models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono=models.IntegerField()
    def __str__(self):
        return self.codigoest

class CARRERA(models.Model):
    codcarr=models.IntegerField(primary_key = True)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return self.codcarr

class PROFESOR(models.Model):
    codprof = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono=models.IntegerField()
    def __str__(self):
        return self.codprof

class MATRICULA(models.Model):
    codmatric = models.IntegerField(primary_key = True)
    codigoest = models.ForeignKey(ALUMNO,null=True,blank=True,on_delete=models.CASCADE)
    codcarr = models.ForeignKey(CARRERA, null=True, blank=True, on_delete=models.CASCADE)
    codprof = models.ForeignKey(PROFESOR, null=True, blank=True, on_delete=models.CASCADE)
    valorsemestre = models.IntegerField()
    def __str__(self):
        return self.codmatric

class ALUMCAR(models.Model):
    codigoest = models.ForeignKey(ALUMNO,null=True,blank=True,on_delete=models.CASCADE)
    codcarr = models.ForeignKey(CARRERA,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.codigoest

class PROFCAR (models.Model):
    codprof = models.ForeignKey(PROFESOR, null=True, blank=True, on_delete=models.CASCADE)
    codcarr = models.ForeignKey(CARRERA, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.codprof
