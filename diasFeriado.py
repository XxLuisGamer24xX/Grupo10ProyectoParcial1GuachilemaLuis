#creamos un diccionario con los diás de la semena
#creamos un diccionario con los meses del año
import calendar
from time import strptime
import holidays
from  datetime import date
from datetime import timedelta
from dateutil.easter import easter
import datetime
from holidays.constants import JAN, MAY, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase
from dateutil.relativedelta import relativedelta as rd, FR
from FeriadosEcuador import *
from funcionesNecesarias import *
#---------------------------------------------------------------
#                 Asignación de fechas  
#---------------------------------------------------------------
def comprobarFecha(fechaIngreso):
    feriadosEcuador=Ecuador()
    fechaIngresoConvetida=datetime.datetime.strptime(fechaIngreso, "%d/%m/%Y")
    if fechaIngresoConvetida in feriadosEcuador:
        print("La fecha ingresada es un día festivo")
        if fechaIngresoConvetida.weekday()==5:
            print("La fecha ingresada es un sábado")
            fechaNueva=fechaIngresoConvetida+timedelta(days=-1)            
        else:
            if fechaIngresoConvetida.weekday()==6:
                print("La fecha ingresada es un domingo")
                fechaNueva=fechaIngresoConvetida+timedelta(days=1)                
            else:
                print("La fecha ingresada es un día de semana xd")
                if fechaIngresoConvetida.weekday()==0:
                    print("La fecha ingresada es un lunes")
                    fechaNueva=fechaIngresoConvetida
                else:
                    if fechaIngresoConvetida.weekday()==1:
                        print("La fecha ingresada es un martes")
                        fechaNueva=fechaIngresoConvetida+timedelta(days=-1)
                    else:
                        if fechaIngresoConvetida.weekday()==2:
                            print("La fecha ingresada es un miércoles")
                            fechaNueva=fechaIngresoConvetida+timedelta(days=-2)
                        else:
                            if fechaIngresoConvetida.weekday()==3:
                                print("La fecha ingresada es un jueves")
                                fechaNueva=fechaIngresoConvetida+timedelta(days=1)
                            else:
                                if fechaIngresoConvetida.weekday()==4:
                                    print("La fecha ingresada es un viernes")
                                    fechaNueva=fechaIngresoConvetida
    else:
        if fechaIngresoConvetida.weekday()==5:
            print("La fecha ingresada es un sábado")
            fechaNueva=fechaIngresoConvetida+timedelta(days=-1)            
        else:
            if fechaIngresoConvetida.weekday()==6:
                print("La fecha ingresada es un domingo")
                fechaNueva=fechaIngresoConvetida+timedelta(days=1)                
            else:
                print("La fecha ingresada es un día de semana")
                
    print("La nueva fecha asignada es:",fechaNueva)
#fecha=str(input("Ingrese la fecha:"))
fecha=fechaActual
""" print("---------------------------------------------------------------")
print("              FERIADOS DE ECUADOR")
print("---------------------------------------------------------------")
for feriado in Ecuador(years=2022).items():
    print(feriado) """

