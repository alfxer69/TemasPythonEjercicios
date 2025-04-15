#Ejercicio 2 Herencia vs Composicion
class Animal:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def hacer_sonidos(self):
        pass
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def conducir(self):
        return 'Rum Rum'
#Creamos una sub clase de 2 clases
#class Persona(Vehiculo,Animal):
#    def __init__(self,nombre,marca,modelo):
#        Vehiculo.__init__(self,marca,modelo)
#        Animal.__init__(self,nombre)
    
#    def presentarse(self):
#        return f'Soy {self.nombre}, conduzco un {self.marca} {self.modelo}'
    
#    def hacer_sonidos(self):
#        return 'Soy una persona'

#persona1=Persona('Juan','Toyota','Corolla')
#print(persona1.presentarse())
#print(persona1.conducir())
#print(persona1.hacer_sonidos())

#Para poder entender usaremos las clases compuestas porque una persona puede tener un vehiculo y un animal

class Persona:
    def __init__(self,nombre,vehiculo,animal):
        self.nombre=nombre
        self.vehiculo=vehiculo
        self.animal=animal
    
    def presentarse(self):
        return f'Soy {self.nombre}, conduzco un {self.vehiculo.marca} {self.vehiculo.modelo} y mi mascota es: {self.animal.nombre}'

vehiculo1=Vehiculo('Toyota','Corolla')
animal1=Animal('Du')
persona2=Persona('Alfredo',vehiculo1,animal1)
print(persona2.presentarse())
print(persona2.vehiculo.conducir()) #usamos elatributo para usar el metodo conducir

