from django.db import models

class Datos_profesionales(models.Model):
    id_profesional = models.IntegerField
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    cuit = models.CharField(max_length=10)
    razon_social = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=60)
    # Create your models here.
    """def __str__(self):
        return f"Bienvenido {self.nombre}, {self.apellido} \n Razón Social: {self.razon_social} \n ID profesional {self.id_profesional} \n"
    
    def muestrainfo(self):
        mensaje = f"Profesional:  {self.nombre} {self.apellido} \n ID Cliente {self.id_profesional} \n enviamos su factura de compra a: {self.mail}"
        print(mensaje)"""

class Horarios_profesionales(models.Model):
    id_profesional = models.IntegerField
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.CharField(max_length=10)
    hora_fin = models.CharField(max_length=10)
       
#    # Create your models here.
#    def __str__(self):
#       return f"Horarios {self.id_profesional}, \n Atiende los días {self.dia_semana} Desde: {self.hora_inicio} Hasta: {self.hora_fin} \n"
#    
#    def muestrainfo(self):
#        mensaje = f"Horarios {self.id_profesional}, \n Atiende los días {self.dia_semana} Desde: {self.hora_inicio} Hasta: {self.hora_fin} \n"
#        print(mensaje)