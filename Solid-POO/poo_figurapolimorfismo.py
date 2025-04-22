import math

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self,radio) -> None:
        self.radio=radio
    
    def area(self):
        return math.pi*self.radio**2
    
    def __str__(self) -> str:
        return f'El area del circulo con radio {self.radio} es {self.area():.2f}'

class Rectangulo(Figura):
    def __init__(self,base,altura) -> None:
        self.base=base 
        self.altura=altura 
    
    def area(self):
        return self.base*self.altura
    
    def __str__(self) -> str:
        return f'El area del Rectangulo con radio {self.base} y atura {self.altura} es {self.area():.2f}'

circulo1=Circulo(5)
print(circulo1)

rectangulo1=Rectangulo(12,15)
print(rectangulo1)

circulo2=Circulo(6)
print(circulo2)