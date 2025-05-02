class Figuras:
    def calcular_area(self):
        pass

class Rectangulo(Figuras):
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    
    def calcular_area(self):
        print(f'El area del Rectangulo es: {self.largo*self.ancho}')

class Cuadrado(Figuras):
    def __init__(self,lado):
        self.lado=lado
    
    def calcular_area(self):
        print(f'El area del cuadrado es: {self.lado*self.lado}')

def calcular_area_figura(figura:Figuras):
    figura.calcular_area()
    
rectagulo=Rectangulo(5,10)
calcular_area_figura(rectagulo)    

cuadrado=Cuadrado(5)
calcular_area_figura(cuadrado)