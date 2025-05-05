from math import pi

class Circulo:
    def __init__(self,radio:float)->None:
        self.radio=radio
    
    @property
    def area(self)->float:
        """Devuelve el area del circulo"""
        return pi*self.radio**2
    
    def perimetro(self)->float:
        """Devuelve el perimetro del circulo"""
        return 2*pi*self.radio

circulo=Circulo(5)
print(f'Area: {circulo.area:.2f}')