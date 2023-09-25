from django.db import models

class Datos_profesionales(models.Model):
    def __init__(self, id_profesional, nombre, apellido, mail, cuit, razon_social, especialidad):
        self.id_profesional = id_profesional
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.cuit = cuit
        self.razon_social = razon_social
        self.especialidad = especialidad
    # Create your models here.
    def __str__(self):
        return f"Bienvenido {self.nombre}, {self.apellido} \n Razón Social: {self.razon_social} \n ID profesional {self.id_profesional} \n"
    
    def muestrainfo(self):
        mensaje = f"Profesional:  {self.nombre} {self.apellido} \n ID Cliente {self.id_profesional} \n enviamos su factura de compra a: {self.mail}"
        print(mensaje)

#class Horarios_profesionales(models.Model):
#    def __init__(self, id_profesional, dia_semana, hora_inicio, hora_fin):
#        self.id_profesional = id_profesional
#        self.dia_semana = dia_semana
#        self.hora_inicio = hora_inicio
#        self.hora_fin = hora_fin
        
#    # Create your models here.
#    def __str__(self):
#       return f"Horarios {self.id_profesional}, \n Atiende los días {self.dia_semana} Desde: {self.hora_inicio} Hasta: {self.hora_fin} \n"
#    
#    def muestrainfo(self):
#        mensaje = f"Horarios {self.id_profesional}, \n Atiende los días {self.dia_semana} Desde: {self.hora_inicio} Hasta: {self.hora_fin} \n"
#        print(mensaje)