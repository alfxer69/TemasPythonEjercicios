from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangulo(Forma):
    def __init__(self,base,altura) -> None:
        self.base=base
        self.altura=altura
        
    def area(self):
        return (self.base*self.altura)/2

class Rectangulo(Forma):
    def __init__(self,largo,ancho) -> None:
        self.largo=largo
        self.ancho=ancho
        
    def area(self):
        return self.ancho*self.largo
    
mitriangulo=Triangulo(12,18)
print('El area del triangulo',mitriangulo.area())
print('\n')
mirectangulo=Rectangulo(14,18)
print('El area del rectangulo es: ',mirectangulo.area())

