from datetime import date
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, MO, TH, FR
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
from holidays.constants import MON, WEEKEND
from holidays.holiday_base import HolidayBase
class Ecuador(HolidayBase):
    # https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_Colombia
    country = "EC"
    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)
    def _populate(self, year):
        '''
        Fechas populares para Ecuador (Solo Fechas Nacionales), según el calendario nacional de cada año
        Y fechas festivas de cantonización y provincialización de SantoDomingo
            Parámetros: 
                year (int): año para el cual se desea obtener las fechas
            Retorno:
                (list): lista de fechas festivas
            Obtenidas del citio web:
                https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
        '''

        #==========================================
        #              Año nuevo
        #==========================================
        if self.observed and date(year, JAN, 1).weekday() in WEEKEND:
            self[date(year, JAN, 1)] = "Año Nuevo"
            pass
        else:
            self[date(year, JAN, 1)] = "Año Nuevo"
        #==========================================
        #              Día del trabajador
        #==========================================
        self[date(year, MAY, 1)] = "Día del Trabajo"
        #===============================================
        #Cantonización de la provincia de Santo Domingo
        #===============================================
        self[date(year, JUL, 3)] ="Cantonización[Santo Domingo]"
        #==================================================
        #Provincialización de la provincia de Santo Domingo
        #==================================================
        self[date(year, NOV, 6)] ="Provincialización [Santo Domingo]"
        #==================================================
        #Provincialización de la provincia de Santo Domingo
        #==================================================
        if self.observed and date(year, DEC, 24).weekday() in WEEKEND:
            pass
        else:
            self[date(year, MAY, 8)] = ("La Inmaculada Concepción" )
        #==========================================
        #              Navidad
        #==========================================
        self[date(year, DEC, 25)] = "Navidad"
        #==========================================
        #          Día de los reyes magos
        #==========================================
        name = "Día de los Reyes Magos"
        if date(year, JAN, 6).weekday() == MON or not self.observed:
            self[date(year, JAN, 6)] = name
        else:
            self[date(year, JAN, 6) + rd(weekday=MO)] = name
        #==========================================
        #             Día de San José
        #==========================================
        name = "Día de San José"
        if date(year, MAR, 19).weekday() == MON or not self.observed:
            self[date(year, MAR, 19)] = name
        else:
            self[date(year, MAR, 19) + rd(weekday=MO)] = name 
        #==========================================
        #       Día de San Pedri y San Pablo
        #==========================================
        name = "San Pedro y San Pablo"
        if date(year, JUN, 29).weekday() == MON or not self.observed:
            self[date(year, JUN, 29)] = name
        else:
            self[date(year, JUN, 29) + rd(weekday=MO)] = name  
        #==========================================
        #          La asuncion de la Virgen
        #==========================================
        name = "La Asunción de la Virgen"
        if date(year, AUG, 15).weekday() == MON or not self.observed:
            self[date(year, AUG, 15)] = name
        else:
            self[date(year, AUG, 15) + rd(weekday=MO)] = name  
        #==========================================
        #             Día de la raza
        #==========================================
        name = "Día de la Raza"
        if date(year, OCT, 12).weekday() == MON or not self.observed:
            self[date(year, OCT, 12)] = name
        else:
            self[date(year, OCT, 12) + rd(weekday=MO)] = name  

        #==========================================
        #         Día de todos los Santos
        #==========================================
        name = "Día de Todos los Santos [All Saint's Day]"
        if date(year, NOV, 1).weekday() == MON or not self.observed:
            self[date(year, NOV, 1)] = name
        else:
            self[date(year, NOV, 1) + rd(weekday=MO)] = name 

        #==========================================
        #             Jueves Santo
        #==========================================
        self[
            easter(year) + rd(weekday=TH(-1))
        ] = "Jueves Santo"

        #==========================================
        #             Viernes Santo
        #==========================================
        self[easter(year) + rd(weekday=FR(-1))] = "Viernes Santo"
        #==========================================
        #             Ascensión del señor
        #==========================================
        name = "Ascensión del señor"
        hdate = easter(year) + rd(days=+39)
        if hdate.weekday() == MON or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name 
        #==========================================
        #             Courpus Christi
        #==========================================
        name = "Corpus Christi"
        hdate = easter(year) + rd(days=+60)
        if hdate.weekday() == MON or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name 
        #==========================================
        #             Sagrado Corazón
        #==========================================
        name = "Sagrado Corazón"
        hdate = easter(year) + rd(days=+68)
        if hdate.weekday() == MON or not self.observed:
            self[hdate] = name
        else:
            self[hdate + rd(weekday=MO)] = name
class EC(Ecuador):
    pass
class EC(Ecuador):
    pass
