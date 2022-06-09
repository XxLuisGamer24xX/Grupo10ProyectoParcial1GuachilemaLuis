from funcionesNecesarias import *
class DatosPaciente:
    """ 
    Super clase creada para guardar contener los atributos como nombre, apellido, telefono....que heredaran las subclases
    """
    def __init__(self, nombrePaciente, apellidoPaciente, edadPaciente, telefonoPaciente, direccionPaciente, emailPaciente, numeroCedulaPaciente, fechaPaciente):
        self.nombreP = nombrePaciente
        self.apellidoP = apellidoPaciente
        self.edadP = edadPaciente
        self.telefonoP = telefonoPaciente
        self.direccionP = direccionPaciente
        self.emailP = emailPaciente
        self.numeroCedulaP = numeroCedulaPaciente
        self.fechaP = fechaPaciente
class pacienteGinecologia(DatosPaciente):
    def perfilPaciente(self, enfermedad):
        self.enfermedadGinelogogia = enfermedad
        self.areaGinelogogia = "Ginecología"
def crearnuevopaciente():
    """
    Funcion para crear un objeto nuevoPaciente
    """
    nombre=str(input("Ingrese su nombre:"))
    validarCacteres=validarCaracteres(nombre)
    if validarCacteres==True:
        apellido=str(input("Ingrese su apellido:"))
        validarCacteres=validarCaracteres(apellido)
        if validarCacteres==True:
            edad=str(input("Ingrese su edad:"))
            validarNumeros=validarNumero(edad)
            if validarNumeros==True:
                telefono=str(input("Ingrese su teléfono:"))
                validarNumeros=validarNumero(telefono)
                if validarNumeros==True:        
                    direccion=str(input("Ingrese su direccion:"))                    
                    email=str(input("Ingrese su email:"))
                    validarCorreo=validarEmail(email)
                    if validarCorreo==True:                        
                        numeroCedula=str(input("Ingrese su numero de cédula:"))
                        validarNumeros=validarNumero(numeroCedula)
                        if validarNumeros==True:
                            fecha=fechaActual
                            perfilGinecologia=str(input("Ingrese su enfermedad:"))
                            nuevoPaciente=pacienteGinecologia(nombre, apellido,edad , telefono,direccion , email, numeroCedula, fecha)
                            nuevoPaciente.perfilPaciente(perfilGinecologia)
                            archivo=open('./RegistrosActividad/Actividad.txt',"a", encoding="utf-8")
                            '''
                                r--->Leer fichero
                                w--->Escribir fichero
                                a--->Añadir en Ficheros existentes
                                x--->Crear fichero
                                t--->Tipo Texto
                                b--->Tipo Binario
                            '''
                            archivo.write("\n --------------------------------------\n")
                            archivo.write("    Paciente"+"["+fechaActual+"]["+ horaActual+"]\n")
                            archivo.write("--------------------------------------\n")
                            archivo.write("Nombre:"+nuevoPaciente.nombreP+"\nApellido:"+nuevoPaciente.apellidoP+"\nEdad:"+str(nuevoPaciente.edadP)+"\nTelefono:"+nuevoPaciente.telefonoP+"\nDirección:"+nuevoPaciente.direccionP+"\nCorreo:"+nuevoPaciente.emailP+"\nCédula:"+nuevoPaciente.numeroCedulaP+"\nFecha:"+nuevoPaciente.fechaP+"\nEnfermedad:"+nuevoPaciente.enfermedadGinelogogia)
                            archivo.close()
                        else:
                            print("|----------------------------------------------------|")
                            print("|  Ingrese un número de cédula válido, por favor   |")
                            print("|----------------------------------------------------|")
                            crearnuevopaciente()
                    else:
                        print("|----------------------------------------------------|")
                        print("|       Ingrese un correo válido, por favor          |")
                        print("|----------------------------------------------------|")   
                        crearnuevopaciente()                 
                else:
                    print("|----------------------------------------------------|")
                    print("|  Ingrese un número de teléfono válido, por favor   |")
                    print("|----------------------------------------------------|")
                    crearnuevopaciente()
            else:
                print("|---------------------------------------")
                print("|  Ingrese una edad válida, por favor  |")
                print("|---------------------------------------")
                crearnuevopaciente()   
        else:
            print("|---------------------------------------")
            print("|  Ingrese un apellido válido, por favor |")
            print("|---------------------------------------")
            crearnuevopaciente()   
    else:
        print("|---------------------------------------")
        print("|  Ingrese un nombre válido, por favor  |")
        print("|---------------------------------------")
        crearnuevopaciente()




        
        
       
