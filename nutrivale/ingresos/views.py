from django.shortcuts import render, redirect
from .forms import *
from .models import *
import datetime
import calendar
from .util import getSemana

MESES = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiempre",
    "Octubre",
    "Noviembre",
    "Diciembre",
)

HORAS = [
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00"
]

# Create your views here.
def menu(request):
    return render(request, "menu.html")

def setHoras(dias_semana, ano, mes):
    semana = []
    i = 0
    for dia in dias_semana:
        if i == 6 or dia < datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day+1):
            horas = []
        else:    
            consultas = Consulta.objects.filter(active=True, fecha__day=dia.day, fecha__month=mes, fecha__year=ano)
            horas = HORAS.copy()
            for consulta in consultas:
                if consulta.hora in HORAS:
                    horas.remove(consulta.hora)
        semana.append({
            'dia': dia.day,
            'ano': dia.year,
            'mes': dia.month,
            'horas': horas
        })
        i += 1
    return semana


def vista_paciente(
    request, 
    ano=datetime.datetime.now().year, 
    mes=datetime.datetime.now().month, 
    dia=datetime.datetime.now().day):

    ano_siguiente = None
    ano_anterior = None
    mes_siguiente = None 
    mes_anterior = None
    dias_semana = getSemana(datetime.datetime(ano,mes,dia))
    semana = setHoras(dias_semana, ano, mes)
    _, dias_mes = calendar.monthrange(ano, mes)
    if dia + 7 > dias_mes:
        dia_siguiente = dia + 7 - dias_mes
        if mes == 12:
            mes_siguiente = 1
            ano_siguiente = ano + 1
        else:
            mes_siguiente = mes + 1 
    else:
        dia_siguiente = dia + 7

    if dia - 7 < 1:
        if mes == 1:
            _, dias_mes_anterior = calendar.monthrange(ano - 1, 12)
            ano_anterior = ano - 1
            mes_anterior = 12
            dia_anterior = dias_mes_anterior + dia - 7
        else:
            _, dias_mes_anterior = calendar.monthrange(ano, mes - 1)
            dia_anterior = dias_mes_anterior + dia - 7
            mes_anterior = mes - 1
    else:
        dia_anterior = dia - 7

    form = FormConsultaPaciente(initial={'active': True, 'estado': "PENDIENTE"})
    if request.method == 'POST':
        form = FormConsultaPaciente(request.POST, initial={'active': True, 'estado': "PENDIENTE"})
        if form.is_valid():
            form.save()
            return redirect(menu)

    context = {
        'form': form,
        'semana': semana,
        'ano': ano,
        'ano_siguiente': ano_siguiente,
        'ano_anterior': ano_anterior,
        'mes': mes,
        'mes_siguiente': mes_siguiente,
        'mes_anterior': mes_anterior,
        'dia_siguiente': dia_siguiente,
        'dia_anterior': dia_anterior,
        'fecha': f'{MESES[mes - 1]} {ano}'
    }
    return render(request, "menu_paciente.html", context)

def calendario(ano, mes):
    calendar.setfirstweekday(calendar.MONDAY)
    mods = []
    primer_dia, dias_mes = calendar.monthrange(ano, mes)
    dia = 0
    dia_texto = ""
    consultas = []
    horas = []
    for i in range(1,43):
        if primer_dia < i and dias_mes+primer_dia >= i:
            dia += 1
            dia_texto = datetime.datetime(ano,mes,dia)
            consultas = Consulta.objects.filter(active=True, fecha__day=dia, fecha__month=mes, fecha__year=ano)
            horas = HORAS.copy()
            for consulta in consultas:
                if consulta.hora in HORAS:
                    horas.remove(consulta.hora)
        else:
            dia_texto = ""
            consultas = []
        if i % 7 == 1:
            tipo = 'start'
        elif i % 7 == 0:
            tipo = 'end'
        else:
            tipo = ''
        mods.append({
            'fecha': dia_texto,
            'tipo': tipo,
            'consultas': consultas,
            'horas': horas
        })
    return mods

def agenda(request, ano=datetime.datetime.now().year, mes=datetime.datetime.now().month):
    nombre_mes = MESES[mes - 1]
    form = FormConsulta(initial={'active': True})
    if request.method == 'POST':
        form = FormConsulta(request.POST, initial={'active': True})
        if form.is_valid():
            form.save()
            return redirect(agenda)
    if mes + 1 > 12:
        mes_siguiente = datetime.datetime(ano + 1, 1, 1)
    else:
        mes_siguiente = datetime.datetime(ano, mes + 1, 1)

    if mes - 1 < 1:
        mes_anterior = datetime.datetime(ano - 1, 12, 1)
    else:
        mes_anterior = datetime.datetime(ano, mes - 1, 1)
    mods = calendario(ano, mes)
    context = {
        'mods': mods,
        'form': form,
        'ano_mes': ano,
        'nombre_mes': nombre_mes,
        'mes_siguiente': mes_siguiente,
        'mes_anterior': mes_anterior
    }
    return render(request, "agenda.html", context)


################################################################


def ingreso_paciente(request):
    form = FormPaciente(initial={'active': True})
    if request.method == 'POST':
        form = FormPaciente(request.POST)
        if form.is_valid():
            form.save()
            return redirect(menu)
    context = {
        'form': form 
    }
    return render(request, "paciente/ingreso_paciente.html", context)

def menu_paciente(request):
    pacientes = Paciente.objects.filter(active=True)
    form = FormPaciente(initial={'active': True})
    if request.method =='POST':
        form = FormPaciente(request.POST, initial={'active': True})
        if form.is_valid():
            form.save()
            return redirect(menu_paciente)
    context = {
        'form': form,
        'items': pacientes,
    }
    return render(request, "paciente/paciente.html", context)

def eliminar_paciente(request, id):
    pacient = Paciente.objects.get(id=id)
    pacient.active = False
    pacient.save()
    return redirect(menu_paciente)

#################################################################


def datos_paciente(request):
    form = FormDatosPaciente(initial={'active':True})
    context = {
        'form': form
    }
    return render(request, "paciente/datos_paciente.html", context)


#################################################################


def ingreso_consulta(request):
    form = FormConsulta(initial={'active':True})
    if request.method == 'POST':
        form = FormConsulta(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_consulta)
    context = {
        'form': form 
    }
    return render(request, "consulta/ingreso_consulta.html", context)

def listado_consulta(request):
    consultas = Consulta.objects.filter(active=True)
    context = {
        'items': consultas
    }
    return render(request, "consulta/listado_consulta.html", context)

def eliminar_consulta(request, id):
    consulta = Consulta.objects.get(id=id)
    consulta.active = False
    consulta.save()
    return redirect(menu_consulta)

def menu_consulta(request):
    consultas = Consulta.objects.filter(active=True)
    form = FormConsulta(initial={'active': True})
    if request.method =='POST':
        form = FormConsulta(request.POST, initial={'active': True})
        if form.is_valid():
            form.save()
            return redirect(menu_consulta)
    context = {
        'form': form,
        'items': consultas
    }
    return render(request, "consulta/consulta.html", context)