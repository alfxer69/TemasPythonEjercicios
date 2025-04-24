from abc import ABC,abstractmethod

class ruidoManager:
    @abstractmethod
    def action(self):
        pass

class Perro(ruidoManager):
    def action(self,animal):
        return f'{animal.name} dice guao guao'

class Gato(ruidoManager):
    def action(self,animal):
        return f'{animal.name} dice miau'

class Gallina(ruidoManager):
    def action(self,animal):
        return f'{animal.name} dice kikiriki'

class Chancho(ruidoManager):
    def action(self,animal):
        return f'{animal.name} dice pig pig'

class Loro(ruidoManager):
    def action(self,animal):
        return f'{animal.name} puede hablar'

class Cocodrilo(ruidoManager):
    def action(self,animal):
        return f'{self.animal} no dice nada'

class Animal:
    def __init__(self,name,type_animal,ruidoManager):
        self.name=name
        self.type_animal=type_animal
        self.ruidoManager=ruidoManager
    
    def action(self):
        return self.ruidoManager.action(self)
    
class Zoo:
    
    def __init__(self)->None:
        self.animals=[]
    
    def add_animales(self,animal):
        self.animals.append(animal)
    
    def action_animals(self):
        for animal in self.animals:
            print(f'{animal.action()} y es {animal.type_animal}' )

zoo=Zoo()
animal1=Animal('perro','mamifero',Perro())
animal2=Animal('gato','mamifero',Gato())
animal3=Animal('loro','ave',Gallina())

zoo.add_animales(animal1)
zoo.add_animales(animal2)
zoo.add_animales(animal3)

zoo.action_animals()

        
    
        
