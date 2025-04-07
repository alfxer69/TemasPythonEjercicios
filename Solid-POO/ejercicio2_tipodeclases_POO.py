#metodos de instancia
class Clase:
    def metodo(self,arg1,arg2):
        return 'Metodo Normal',self

mi_clase=Clase()
print(mi_clase.metodo('a','b'))

#metodos de clase
class Clase:
    @classmethod
    def metodo(cls):
        return 'Metodo de Clase',cls

mi_clase=Clase()
print(mi_clase.metodo())
#Por lo tanto, los métodos de clase:
#No pueden acceder a los atributos de la instancia.
#Pero si pueden modificar los atributos de la clase.

#metodos estaticos
class Clase:
    @staticmethod
    def metodoestatico():
        return 'Metodo Estatico'

mi_clase=Clase()
print(Clase.metodoestatico())
print(mi_clase.metodoestatico())

#no aceptan como parámetro ni la instancia ni la clase. 
#Es por ello por lo que no pueden modificar el estado ni de la clase ni de la instancia. 
#Pero por supuesto pueden aceptar parámetros de entrada.
