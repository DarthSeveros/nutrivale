"""nutrivale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ingresos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),

    path('menu_paciente/', vista_paciente, name='menu_paciente'),
    path('menu_paciente/<int:ano>&<int:mes>&<int:dia>', vista_paciente, name='menu_paciente'),
    
    path('agenda/', agenda, name='agenda'),
    path('agenda/<int:ano>&<int:mes>', agenda, name='agenda'),

    path('listado_consulta/', menu_consulta, name='listado_consulta'),
    path('ingreso_consulta/', ingreso_consulta, name='ingreso_consulta'),
    path('eliminar_consulta/<int:id>', eliminar_consulta, name='eliminar_consulta'),
    path('datos_paciente/', datos_paciente, name='datos_paciente'),

    path('pacientes/', menu_paciente, name="pacientes"),
    path('ingreso_paciente/', ingreso_paciente, name='ingreso_paciente'),
    path('eliminar_paciente/<int:id>', eliminar_paciente, name="eliminar_paciente")
]
