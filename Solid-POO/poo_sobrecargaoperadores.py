class Punto:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __add__(self,otro):
        return Punto(self.x+otro.x,self.y+otro.y)
    
    def __str__(self):
        return f'Punto({self.x},{self.y})'
    
p1=Punto(1,2)
p2=Punto(3,4)
p3=p1+p2
print(p3)    