#-------------------------------------------------------------
#                    CLASE PADRE
#-------------------------------------------------------------
from sympy import integer_nthroot
class Trabajador:
    def __init__(self, nombre, edad):
        self.atributo1=nombre
        self.atributo2=edad
#-------------------------------------------------------------
#           CLASE HIJA INGENIERO  EN SISTEMAS
#-------------------------------------------------------------
class IngSistemas(Trabajador):
    def perfil(self, lenguaje, experiencia, area ):
        self.atributo3=lenguaje
        self.atributo4=experiencia
        self.atributo5=area
#-------------------------------------------------------------
#            CLASE HIJA-DISEÑADOR GRÁFICO
#-------------------------------------------------------------
class diseñadorGrafico(Trabajador):
    def perfil(self, software, aplicadosA):
        self.atributo3=software
        self.atributo4=aplicadosA
#-------------------------------------------------------------------------
#             INSTACIAMOS LAS CLASES
#-------------------------------------------------------------------------
trabajadorNuevo=IngSistemas(str(input("Ingrese el nombre del ingeniero: ")),int(input("Ingrese la edad del ingeniero: ")))
trabajadorNuevo.perfil(str(input("Ingrese el lenguaje que maneja: ")),int(input("Ingrese la experiencia del ingeniero: ")),str(input("Ingrese el area de trabajo: ")))
print("El ingeniero es: ", trabajadorNuevo.atributo1, "y tiene", trabajadorNuevo.atributo2, "años de edad", "y maneja el lenguaje:", trabajadorNuevo.atributo3, "y tiene", trabajadorNuevo.atributo4, "años de experiencia en el area de:", trabajadorNuevo.atributo5)