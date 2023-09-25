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
	
	html_1 = open("C:/Users/cti0716/Python/PreEntrega3_Mariana_Torres/POINT/POINT/plantillas/principal.html")
	plantilla = Template(html_1.read())
	html_1.close()
	miContexto_1 = Context()
	documento_1 = plantilla.render(miContexto_1)
	return HttpResponse(documento_1)


