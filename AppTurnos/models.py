from django.db import models
import datetime

class Datos_profesionales(models.Model):
    id_profesional = models.AutoField(primary_key=True)
    nombre = models.CharField(default="",max_length=60)
    apellido = models.CharField(default="",max_length=60)
    mail = models.CharField(default="",max_length=60)
    cuit = models.CharField(default="",max_length=10)
    razon_social = models.CharField(default="",max_length=60)
    especialidad = models.CharField(default="",max_length=60)

class Horarios_profesionales(models.Model):
    id_profesional = models.ForeignKey
    dia_semana = models.CharField(default="",max_length=10)
    hora_inicio = models.CharField(default="",max_length=10)
    hora_fin = models.CharField(default="",max_length=10)

class Meses(models.Model):
    periodo = models.CharField(default="202301", max_length=10)
    id_profesional = models.ForeignKey
    fecha = models.DateField(default=datetime.date.today)
    hora =models.DateTimeField(default=datetime.datetime.now) 

class Pacientes(models.Model):
    id_pacientes = models.AutoField(primary_key=True)
    nombre = models.CharField(default="",max_length=60)
    apellido = models.CharField(default="",max_length=60)
    obra_social = models.CharField(default="",max_length=60)

