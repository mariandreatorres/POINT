from django.template import Template, Context, loader
from django.http import HttpResponse
from django.contrib import admin
from datetime import datetime
from AppTurnos.models import Datos_profesionales


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

	plantilla = loader.get_template("principal.html")
	documento_1 = plantilla.render(profesionales)
	return HttpResponse(documento_1)


    

