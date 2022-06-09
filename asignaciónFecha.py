from diasFeriado import *
from funcionesNecesarias import *

fechaTurno=comprobarFecha(fechaActual)
Turnos=["0","0","0","0","0","0","0"]
def asignarTurno(fecha):
    Turnos.insert(0,str(fecha))
asignarTurno(fechaTurno)
for i in Turnos:
    print("Posicion:",i)
