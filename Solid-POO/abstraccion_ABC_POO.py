#La Clase Base Abstracta (ABC) nos permite definir un modelo para otras clases. Este modelo garantiza que cualquier
#clase que se derive de la clase base abstracta (ABC) implemente ciertos métodos proporcionando una interfaz coherente.
#A continuación se muestra el código de ejemplo de definición de la interfaz estándar de la clase base abstracta en
#Python:
    
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
#Aplicación de la ley
#Cuando una clase hereda de una clase base abstracta (ABC), debe implementar todos los métodos abstractos.
#Si no lo hace, Python lanzará un TypeError. Este es el ejemplo de la implementación forzada de la clase 
#base abstracta en Python:

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    
    def perimetro(self):
        return 2*(self.width*self.height)

class Circle(Shape):
    def __init__(self,radio):
        self.radio=radio
        
    def area(self):
        import math
        return math.pi*self.radio**2
    
    def perimetro(self):
        import math
        return 2*math.pi*self.radio
    
class Square(Shape):
    def __init__(self,lado):
        self.lado=lado
    
    def area(self):
        return self.lado**2
    
    def perimetro(self):
        return 2*self.lado   
    

rect=Rectangle(4,8)
circ=Circle(5)
squa=Square(7)

print('-'*50)
print(f'El area del rectangulo es: {rect.area()} y su perimetro es: {rect.perimetro()}')
print('-'*50)
print(f'El area del Circulo es: {circ.area():.2f} y su perimetro es: {circ.perimetro():.2f}')
print('-'*50)
print(f'El area del Cuadrado es: {squa.area()} y su perimetro es: {squa.perimetro()}')
    
    
    



