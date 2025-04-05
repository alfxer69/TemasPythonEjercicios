class Ejemplo:
    def __init__(self):
        self.__atributo_privado=30
    
    def getter(self):
        return self.__atributo_privado
    
    def setter(self,valor):
        if valor>0:
            self.__atributo_privado=valor
        else:
            print('El valor debe ser mayor que 0')

ejemplo=Ejemplo()
print(ejemplo.getter()) #Acceso al atributo privado
ejemplo.setter(50)  #Acceso al atributo privado
print(ejemplo.getter())
ejemplo.__atributo_privado=100 #No se puede acceder al atributo privado
print(ejemplo.getter()) #Acceso al atributo privado)