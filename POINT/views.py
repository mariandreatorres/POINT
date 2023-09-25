from django.template import Template, Context, loader
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
	
	profesionales = {"nombre_prof":nombre_p, "apellido_prof":apellido_p, "fecha_nac_prof":fecha_nac_p, 
					"especialidad_prof": especialidad_p}
	""" version anterior
	html_1 = open("C:/Users/cti0716/Python/PreEntrega3_Mariana_Torres/POINT/POINT/plantillas/principal.html")
	plantilla = Template(html_1.read())
	html_1.close()
	miContexto_1 = Context()
	documento_1 = plantilla.render(miContexto_1)
	"""
	plantilla = loader.get_template("principal.html")
	documento_1 = plantilla.render(profesionales)
	return HttpResponse(documento_1)


    

