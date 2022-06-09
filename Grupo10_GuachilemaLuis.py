from asyncio import as_completed
from clasesNecesarias import *
class ClasePrincipal():
    '''
    Clase principal, que tendrá como métodos menúPrincipal y menúPaciente 
    '''
    def menuPrincipal():
        '''
        Método que muestra el menú principal
        '''
        print("-----------------------------------------------------")
        print("|       Universidad de  las Fuerzas Armadas           |")
        print("|         Luis Eduardo Guachilema Sánchez             |")
        print("|                Sistema  de turnos                   |")
        print("-----------------------------------------------------")
        print("| Presione 1)                                Paciente|")
        print("| Presione 2)                                  Doctor|")
        print("| Presione 3)                                  Salir |")
        print("|----------------------------------------------------|")
        try:
            '''
            Se valida que el usuario ingrese una opción válida
            '''
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                ClasePrincipal.menuPaciente()
            elif opcion == 2:
                print("-----------------------------------------------------")
                print("|                    DOCTOR                        |")
                print("-----------------------------------------------------")
            elif opcion == 3:
                print("-----------------------------------------------------")
                print("|            Gracias por su visita                   |")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("|              No existe esta opción                  |")
                print("|     Lo redireccionaremos al menú [Principal]        |")
                print("-----------------------------------------------------")
                print ("                       |")
                print ("                       |")
                print ("                       |")
                print ("                       |")
                print ("                       V")
                ClasePrincipal.menuPrincipal()
        except ValueError:
            '''
            Se valida que el usuario ingrese solo números
            '''
            print("|---------------------------------------")
            print("| No puede ingresar letras o caracteres |")
            print("|---------------------------------------")
            ClasePrincipal.menuPrincipal()
    def menuPaciente():
        '''
        Método que muestra el menú paciente
        '''
        print("-----------------------------------------------------")
        print("|            Bienvenido turnos Pacientes             |")
        print("|   Elija el área en el que va a revervar su turno   |")
        print("-----------------------------------------------------")
        print("| Presione 1)                             Ginecología|")
        print("| Presione 2)                               Ortopedia|")
        print("| Presione 3)                                 Vacunas|")
        print("| Presione 4)                                   Salir|")
        print("|----------------------------------------------------|")
        try:
            opcionPaciente = int(input("Ingrese una opcion: "))
            if opcionPaciente == 1:
                print("-----------------------------------------------------")
                print("|              Turnos [Ginecología]                   |")
                print("-----------------------------------------------------")
                crearnuevopaciente()
            elif opcionPaciente == 2:
                print("-----------------------------------------------------")
                print("|                    Ortopedia                        |")
                print("-----------------------------------------------------")
            elif opcionPaciente == 3:
                print("-----------------------------------------------------")
                print("|                    Vacunas                          |")
                print("-----------------------------------------------------")
            elif opcionPaciente == 4:
                print("-----------------------------------------------------")
                print("|             Gracias por su visita                   |")
                print("-----------------------------------------------------")
            else:
                print("-----------------------------------------------------")
                print("|              No existe esta opción                  |")
                print("|   Lo redireccionaremos al menú [Turnos Pacientes]   |")
                print("-----------------------------------------------------")
                print ("                       |")
                print ("                       |")
                print ("                       |")
                print ("                       |")
                print ("                       V")
                ClasePrincipal.menuPaciente()
        except ValueError:
            print("|---------------------------------------")
            print("| No puede ingresar letras o caracteres |")
            print("|---------------------------------------")
            ClasePrincipal.menuPaciente()   
ClasePrincipal.menuPrincipal()
