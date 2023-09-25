from django.contrib import admin
from django.urls import path, include
from django.db import models
from AppTurnos.views import *

urlpatterns =[
path('admin/', admin.site.urls),
path("AppTurnos/", include("AppTurnos.urls")),
#path('profesionales/', Datos_profesionales),
#path('horarios/', Horarios_profesionales),
#path('agenda/', Meses),
#path('pacientes/', Pacientes),
]