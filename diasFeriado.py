import calendar
from time import strptime
import holidays
from  datetime import date
from datetime import timedelta
import datetime
from dateutil.relativedelta import relativedelta as rd, FR
from FeriadosEcuador import *
from funcionesNecesarias import *
#---------------------------------------------------------------
#                 Asignación de fechas  
#---------------------------------------------------------------
def comprobarFecha(fechaIngreso):
    '''
    Funcion que me permite ingresar una fecha y determinar la fecha ingresada es un día festivo
    o si está registrandose un fin de semana, y asignarle una fecha nueva al día laboral más cercano
    para poder así en otra función usar la nueva fecha para poder asignarle un turno  
    ---------------------
    Uso de la clase Ecuador , para determinar si el día ingresa consta en las fechas
    de los feriados Ecuatorianos y feriados de la provincia de Santo Domingo
        Parametros:
            fechaIngreso (str): fecha que se desea verificar        
    '''
    feriadosEcuador=Ecuador()
    #Convetir fecha obtenida a un formato dia/mes/año para poder hacer los cálculos entre fechas
    fechaIngresoConvetida=datetime.datetime.strptime(fechaIngreso, "%d/%m/%Y")
    if fechaIngresoConvetida in feriadosEcuador:
        '''
        Si la fecha ingresada consta en los feriados Ecuatorianos, entonces calculamos
        si el día pertenece a un fin de semana o no, y asignamos una nueva fecha
        o si cae un lunes la fecha será la misma, si cae un marte, miercoles, jueves, se le asignará al día siguiente
        porque si lo aproximamos un día anterior, la persona no podrá asignarle un turno. 
        '''
        #============================================#
        #             Dia festivo
        #============================================#
        if fechaIngresoConvetida.weekday()==5:
            #Para sabados
            fechaNueva=fechaIngresoConvetida+timedelta(days=2)            
        else:
            #Para Domingos
            if fechaIngresoConvetida.weekday()==6:
                print("La fecha ingresada es un domingo")
                fechaNueva=fechaIngresoConvetida+timedelta(days=1)                
            else:                
                #Para lunes
                if fechaIngresoConvetida.weekday()==0:
                    fechaNueva=fechaIngresoConvetida+timedelta(days=1)  
                else:
                    #Para martes
                    if fechaIngresoConvetida.weekday()==1:                    
                        fechaNueva=fechaIngresoConvetida+timedelta(days=1)
                    else:
                        #Para miércoles
                        if fechaIngresoConvetida.weekday()==2:                        
                            fechaNueva=fechaIngresoConvetida+timedelta(days=1)
                        else:
                            #Para jueves
                            if fechaIngresoConvetida.weekday()==3:                                
                                fechaNueva=fechaIngresoConvetida+timedelta(days=1)
                            else:
                                #Para viernes
                                if fechaIngresoConvetida.weekday()==4:                                    
                                    fechaNueva=fechaIngresoConvetida+timedelta(days=3)
    else:
        #============================================#
        #              Dias Normales
        #============================================#
        if fechaIngresoConvetida.weekday()==5:
            #Para sabados
            fechaNueva=fechaIngresoConvetida+timedelta(days=2)            
        else:
            #Para Domingos
            if fechaIngresoConvetida.weekday()==6:
                fechaNueva=fechaIngresoConvetida+timedelta(days=1)                
            else:
                #Para lunes
                if fechaIngresoConvetida.weekday()==0:                    
                    fechaNueva=fechaIngresoConvetida+timedelta(days=0)  
                else:
                    #Para martes
                    if fechaIngresoConvetida.weekday()==1:
                        fechaNueva=fechaIngresoConvetida+timedelta(days=0)
                    else:
                        #Para miércoles
                        if fechaIngresoConvetida.weekday()==2:
                            fechaNueva=fechaIngresoConvetida+timedelta(days=0)
                        else:
                            #Para jueves
                            if fechaIngresoConvetida.weekday()==3:                                
                                fechaNueva=fechaIngresoConvetida+timedelta(days=0)
                            else:
                                #Para Viernes
                                if fechaIngresoConvetida.weekday()==4:                                
                                    fechaNueva=fechaIngresoConvetida+timedelta(days=0)
    '''
    Retornamos solo la fecha nueva, pa que si cumple alguna de las condiciones establecidas
    la nueva fecha será la que usaremos para asignarle un turno desde otra clase a nuestro cliente
    '''
    return fechaNueva        

