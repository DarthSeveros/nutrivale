import calendar
from datetime import datetime

class Semana():
    def __init__(self, dias, ano, mes):
        self.dias = dias
        self.mes = mes
        self.ano = ano

def fillCalendarBlanks(date = datetime.now()):
    calendar.setfirstweekday(calendar.MONDAY)
    mycalendar = calendar.monthcalendar(date.year, date.month)
    if date.month == 1:
        previousweek = calendar.monthcalendar(date.year - 1, 12)[-1]
    else:
        previousweek = calendar.monthcalendar(date.year, date.month-1)[-1]
    i = 0
    while 0 in mycalendar[0]:
        mycalendar[0][i] = previousweek[i]
        i += 1

    if date.month == 12:
        nextweek = calendar.monthcalendar(date.year + 1, 1)[0]
    else:
        nextweek = calendar.monthcalendar(date.year, date.month + 1)[0]
    nextweek = list(filter((0).__ne__, nextweek))
    nextweek.reverse()
    i = 6
    j = 0
    while 0 in mycalendar[-1]:
        mycalendar[-1][i] = nextweek[j]
        j += 1
        i -= 1

    return mycalendar

def getIndexSemana(date = datetime.now()):
    calendar.setfirstweekday(calendar.MONDAY)
    mycalendar = calendar.monthcalendar(date.year, date.month)
    numero_semana = None
    for semana in mycalendar:
        if date.day in semana:
            numero_semana = mycalendar.index(semana)
    
    return numero_semana

def getSemana(date = datetime.now()):
    calendar.setfirstweekday(calendar.MONDAY)
    calendario = setMonthDates(date)
    calendario = fillMonthDatesBlank(calendario, date)
    index_semana = getIndexSemana(date)
    return calendario[index_semana]

def fillMonthDatesBlank(calendario, date=datetime.now()):
    calendar.setfirstweekday(calendar.MONDAY)
    mycalendar = calendario
    if date.month == 1:
        ano_previousweek = date.year - 1
        mes_previousweek = 12
        previousweek = calendar.monthcalendar(ano_previousweek, mes_previousweek)[-1]
    else:
        ano_previousweek = date.year
        mes_previousweek = date.month - 1
        previousweek = calendar.monthcalendar(ano_previousweek, mes_previousweek)[-1]
    i = 0
    while 0 in mycalendar[0]:
        mycalendar[0][i] = datetime(ano_previousweek, mes_previousweek, previousweek[i]) 
        i += 1

    if date.month == 12:
        nextweek = calendar.monthcalendar(date.year + 1, 1)[0]
    else:
        nextweek = calendar.monthcalendar(date.year, date.month + 1)[0]
    nextweek = list(filter((0).__ne__, nextweek))
    nextweek.reverse()
    i = 6
    j = 0
    while 0 in mycalendar[-1]:
        mycalendar[-1][i] = nextweek[j]
        j += 1
        i -= 1

    return mycalendar

def setMonthDates(date = datetime.now()):
    calendar.setfirstweekday(calendar.MONDAY)
    mycalendar = calendar.monthcalendar(date.year, date.month)
    i = 0
    for semana in mycalendar:
        semana = list(map(lambda x: 0 if x == 0 else datetime(date.year,date.month,x), semana))
        mycalendar[i] = semana
        i += 1
    return mycalendar

    