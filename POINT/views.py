from django.template import Template, Context, loader
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from datetime import datetime
from AppTurnos.models import Datos_profesionales, Horarios_profesionales, Meses, Pacientes

def inicio(request):
	return HttpResponse("Esta es la vista de bienvenida")

def profesionales(request):  ###prueba
	valor_1 = Datos_profesionales (nombre="Mariana", 
		 apellido ="Torres",
    	 mail = "mariandreatorres@gmail.com",
		 cuit = '27223707489',
		 razon_social ='Torres, Mariana Andrea',
		 especialidad = 'Ortodoncista')
	valor_1.save()
	return HttpResponse(f"El profesional creado es: {valor_1.nombre}, {valor_1.apellido} cuya especialidad es: {valor_1.especialidad}")	

	
	plantilla = loader.get_template("principal.html")
	documento_1 = plantilla.render(Datos_profesionales)
	return HttpResponse(documento_1)

def horarios(request):
	return HttpResponse("esta es la vista de horarios de los profesionales")

def agenda(request):
	return HttpResponse("esta es la vista de agenda de los profesionales")

def pacientes(request):
	return HttpResponse("esta es la vista de pacientes")
    

