from typing import Protocol
from math import pi
class IArea(Protocol):
    def area(self)->float:
        ...

class Circulo(IArea):
    def __init__(self,radio:float)->None:
        self.radio=radio
    def area(self)->float:
        return pi*self.radio**2

class Cuadrado(IArea):
    def __init__(self,lado: float)->None:
        self.lado=lado
    def area(self):
        return self.lado**2
class Rectangulo(IArea):
    def __init__(self,largo:float,ancho:float)->None:
        self.largo=largo
        self.ancho=ancho
    def area(self)->float:
        return self.largo*self.ancho

class Triangulo(IArea):
    def __init__(self,base:float,altura:float)->None:
        self.base=base
        self.altura=altura
    def area(self)->float:
        return (self.base*self.altura)/2
            

circulo=Circulo(5)
print(f"El area del circulo es {circulo.area():.2f}")

triangulo=Triangulo(5,10)
print(f"El area del triangulo es {triangulo.area():.2f}")

cuadrado=Cuadrado(5)
print(f"El area del cuadrado es {cuadrado.area():.2f}")