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
    def fliy(self)->None: