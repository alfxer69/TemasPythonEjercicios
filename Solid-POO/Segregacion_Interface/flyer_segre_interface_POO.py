from typing import Protocol

class Flyer(Protocol):
    """Protocolo para objetos que pueden ser voladores"""
    
    def fly(self)->None:
        """Realiza la accion de volar"""
        ...

class Bird:
    """Clase que representa un pajaro"""
    def __init__(self,name:str)->None:
        self.name=name
    def fly(self)->None:
        print(f'{self.name} esta volando!')

class Airplane:
    """Clase que representa un avion"""
    def __init__(self,name:str)->None:
        self.name=name
    def fly(self)->None:
        print(f'{self.name} esta volando!')

class Helicopter:
    """Clase que representa un helicoptero"""
    def __init__(self,name:str)->None:
        self.name=name
    def fly(self)->None:
        print(f'{self.name} esta volando!')
class Drone:
    """Clase que representa a un drone"""
    def __init__(self,name:str)->None:
        self.name=name
    def fly(self)->None:
        print(f'{self.name} esta volando!')

def process_fliyer(fliyer:Flyer)->None:
    """Funcion generica que acepta que cualquier objeto que cumpla con el protocolo flyer"""
    fliyer.fly()

bird=Bird('Condor')
process_fliyer(bird)

drone=Drone('DJI')
process_fliyer(drone)

airplane=Airplane('Boeing 747')
process_fliyer(airplane)

helicopter=Helicopter('Apache')
process_fliyer(helicopter)

