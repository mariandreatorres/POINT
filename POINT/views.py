from django.template import Template, Context
from django.http import HttpResponse
from django.contrib import admin
from datetime import datetime


def saludar(request):
	return HttpResponse("Hola Django - Coder")

def hoy(request):
	fecha = datetime.now()
	return HttpResponse(f"Hoy es {fecha}.") 

def pantalla_1(request):  ###prueba
	nombre_p = "Mariana"
	apellido_p = "Torres"
	fecha_nac_p = "27/09/1971"
	especialidad_p = "Ortodoncista"
	
	diccionario = {"nombre_prof":nombre_p, "apellido_prof":apellido_p, "fecha_nac_prof":fecha_nac_p, 
					"especialidad_prof": especialidad_p}
	
	html_1 = open("C:/Users/cti0716/Python/PreEntrega3_Mariana_Torres/POINT/POINT/plantillas/principal.html")
	plantilla = Template(html_1.read())
	html_1.close()
	miContexto_1 = Context()
	documento_1 = plantilla.render(miContexto_1)
	return HttpResponse(documento_1)

class Cliente:

    def __init__(self, id_cliente, nombre, apellido, mail, cuit, razon_social, gerencia_asignada):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.cuit = cuit
        self.razon_social = razon_social
        self.gerencia_asignada = gerencia_asignada
    
    

