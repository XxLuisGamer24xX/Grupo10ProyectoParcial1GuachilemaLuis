from funcionesNecesarias import *
from diasFeriado import *
pacientes=[]
listaTabla=[]
def tabla7():
    for i in range(1,4):
        respuesta=i*7
        listaTabla.append(int(respuesta))
def asignarTurno():
    tabla7()
    filename = "./RegistrosActividad/turnosPorDia.txt"
    try:
        with open(filename, "r") as f_obj:
            contenido = f_obj.read()
    except FileNotFoundError:
        print("No se encuentra el archivo")
    else:
        palabras = contenido.split()
        cantidadPacientes = len(palabras)
        print("El número de palabras es:", str(cantidadPacientes))
    for i in range(cantidadPacientes):
        if (i in listaTabla)==True:
            print("Lista Completa")
            for i in pacientes:
                print(i)
            pacientes.clear()
            print("Lista borrada")
            pacientes.append(input("Ingrese el nombre del paciente: "))
        else:
            pacientes.append(input("Ingrese el nombre del paciente: "))
def turnoConfirmado(fechaConfirmada,nombrePaciente, apellidoPaciente, edadPaciente, telefonoPaciente, direccionPaciente, emailPaciente, numeroCedulaPaciente, fecha,perfilGinecologia):
    archivoTurnoFecha=open('./RegistrosActividad/turnosPorDia.txt',"a", encoding="utf-8")
    archivoTurnoFecha.write(str(fechaConfirmada)+"\n")
    archivoTurnoFecha.close()
    archivo=open('./RegistrosGinecología/TurnosPacientesGinecología.txt',"a", encoding="utf-8")
    archivo.write("\n--------------------------------------\n")
    archivo.write("    Paciente"+"["+fechaActual+"]["+ horaActual+"]\n")
    archivo.write("--------------------------------------\n")
    archivo.write("Turno:"+str(fechaConfirmada)+"\n")
    archivo.write("Nombre:"+nombrePaciente+"\nApellido:"+apellidoPaciente+"\nEdad:"+str(edadPaciente)+"\nTelefono:"+telefonoPaciente+"\nDirección:"+direccionPaciente+"\nCorreo:"+emailPaciente+"\nCédula:"+numeroCedulaPaciente+"\nFecha Registro:"+fecha+"\nEnfermedad:"+perfilGinecologia)                
    archivo.close()
    print("-----------------------------------------------------")
    print("|             Turno confirmado exitosamente           |")
    print("|   Lo redireccionaremos al menú [Principal]          |")
    print("-----------------------------------------------------")  


    

    

