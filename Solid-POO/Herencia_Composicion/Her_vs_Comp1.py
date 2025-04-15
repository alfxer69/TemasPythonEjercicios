#Ejercicio1 
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def hacer_sonidos(self):
        pass

class Conejo(Animal):
    def hacer_sonidos(self):
        return 'Hola soy un conejo'

mi_conejo=Conejo('Zanahoria')
print(mi_conejo.nombre)
print(mi_conejo.hacer_sonidos())