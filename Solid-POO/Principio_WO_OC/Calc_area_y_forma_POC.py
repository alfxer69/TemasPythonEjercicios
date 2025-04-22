from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self,shape_type):
        self.shape_type=shape_type
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__('circle') #llama al constructor Shape como circle
        self.radius=radius
    
    def calculate_area(self):
        return pi*self.radius**2

class Rectangle(Shape):
    def __init__(self, width,height):
        super().__init__('rectangle')
        
    def calculate_area(self):
        return self.width*self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__('square')
    
    def calculate_area(self):
        return self.side**2
    
circle=Circle(4)
print(f'{circle.calculate_area():.2f} cm´2')