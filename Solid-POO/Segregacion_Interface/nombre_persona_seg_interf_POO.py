from typing import Protocol

class HasName(Protocol):
    """Protocolo para objetos que tienen un nombre"""
    @property
    def name(self) -> str:
        """Devuelve el nombre del objeto"""
        ...

class Person:
    """Clase que representa a una persona"""
    def __init__(self,name:str,lastname:str)->None:
        self._name=name
        self._lastname=lastname
    
    @property
    def name(self)->None:
        return self._name+' '+self._lastname

def process_name(person:HasName)->None:
    """Funcion generica que acepta cualquier objeto que cumpla con el protocolo HasName"""
    return f'Hola {person.name}'

person=Person('Juan','Muñoz')
print(process_name(person)) #deberia imprimir 'Juan'

person2=Person('Pedro','Gonzalez')
print(process_name(person2)) #deberia imprimir 'Pedro'


