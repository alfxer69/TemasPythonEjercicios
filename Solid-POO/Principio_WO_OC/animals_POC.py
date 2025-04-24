from abc import ABC,abstractmethod

class ruidoManager:
    @abstractmethod
    def action(self):
        pass

class Perro:
    def action(self,animal):
        return f'{animal.name} dice guao guao'

class Gato:
    def action(self,animal):
        return f'{animal.name} dice miau'

class Gallina:
    def action(self,animal):
        return f'{animal.name} dice kikiriki'

class Chancho:
    def action(self,animal):
        return f'{animal.name} dice pig pig'

class Loro:
    def action(self,animal):
        return f'{animal.name} puede hablar'

class Cocodrilo:
    def action(self,animal):
        return f'{self.animal} no dice nada'

class Animal:
    def __init__(self,name,type_animal,ruidoManager):
        self.name=name
        self.type_animal=type_animal
        self.ruidoManager=ruidoManager
    
    def action(self):
        return self.ruidoManager.action(self)
    

        
