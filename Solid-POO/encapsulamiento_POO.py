#Encapsulamiento de un atributo de instancia
# Atributo privado: se accede solo dentro de la clase
# Atributo protegido: se accede dentro de la clase y sus subclases
# Atributo público: se accede desde cualquier parte del programa

#Atributo privado
#class Ejemplo:
#    def __init__(self):
#        self.__atributo_privado = 20
#    
#    def get_atributo_privado(self):
#        print(self.__atributo_privado*2)
#
#valor=Ejemplo()
#print(valor.get_atributo_privado())

# Atributo protegido
class Ejemplo:  
    def __init__(self):
        self._atributo_protegido=20

    def get_atributo_protegido(self):
        print(self._atributo_protegido)

valor=Ejemplo()
print(valor._atributo_protegido)
valor.get_atributo_protegido()

