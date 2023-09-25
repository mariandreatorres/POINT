from django.db import models

class Datos_profesionales:

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