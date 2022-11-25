from django.db import models
from .choises import *
# Create your models here.

class Doctor(models.Model):
    nombresd = models.CharField(max_length=200)
    apellidosd = models.CharField(max_length=200)
    direcciond = models.CharField(max_length=200)
    nmr_telefonod = models.IntegerField()
    imagend=models.ImageField(upload_to="merchan")
    fechacreaciond=models.DateTimeField(auto_now_add=True)
    fechamodificaciond=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombresd

class Paciente(models.Model):
    nombres=models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    nmr_telefono=models.IntegerField()
    imagen=models.ImageField(upload_to="merchan")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombres

class Hospital (models.Model):
    nombre=models.CharField(max_length=200)
    ubicacion=models.CharField(max_length=200)
    doctor=models.ForeignKey(Doctor,null=True,blank=True,on_delete=models.CASCADE)
    nmr_telefono=models.IntegerField()
    paciente=models.ForeignKey(Paciente,null=True,blank=True,on_delete=models.CASCADE)
    fechacreacion=models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=estado)
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre=models.CharField(max_length=200)
    ubicacion=models.CharField(max_length=200)
    doctor=models.ForeignKey(Doctor,null=True,blank=True,on_delete=models.CASCADE)
    nmr_telefono=models.IntegerField()
    paciente=models.ForeignKey(Paciente,null=True,blank=True,on_delete=models.CASCADE)
    fechacreacion=models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=estado)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits = 5, decimal_places = 2)
    imagen=models.ImageField(upload_to="merchan")
    fechacreacion=models.DateTimeField(auto_now_add=True)
    fechamodificacion=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Cita_medica (models.Model):
    doctor=models.ForeignKey(Doctor,null=True,blank=True,on_delete=models.CASCADE)
    paciente=models.ForeignKey(Paciente,null=True,blank=True,on_delete=models.CASCADE)
    motivo=models.CharField(max_length=200)
    hospital=models.ForeignKey(Hospital,null=True,blank=True,on_delete=models.CASCADE)
    sucursal=models.ForeignKey(Sucursal,null=True,blank=True,on_delete=models.CASCADE)


class Cita_medica_tratamiento(models.Model):
    paciente=models.ForeignKey(Paciente,null=True,blank=True,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    tratamiento=models.CharField(max_length=500)   
