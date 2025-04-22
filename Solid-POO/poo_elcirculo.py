import math

class Circulo:
    def __init__(self,radio) -> None:
        self.radio=radio
    
    def calcular_area(self):
        resultado=math.pi*(self.radio**2)
        return resultado

circulo1=Circulo(5)
print(f'El area del circulo es: {circulo1.calcular_area():.2f}')
