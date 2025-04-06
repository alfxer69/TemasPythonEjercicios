class Figura:
    def area(self):
        pass
    
class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    
    def area(self):
        return 3.14*self.radio**2
    
class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado
    
    def area(self):
        return self.lado**2

def calcular_area(figura):
    return figura.area()


circulo=Circulo(5)
cuadrado=Cuadrado(4)

print(f'El area del circulo es:{calcular_area(circulo)}')
print(f'Elarea del cuadrado es: {calcular_area(cuadrado)}')