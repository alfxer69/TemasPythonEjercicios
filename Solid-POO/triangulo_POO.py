#Crea la clase Triangulo que almacene la longitud de cada uno de sus lados. Deberá contener los siguientes métodos:
#area(): devuelve el área del triángulo
#forma(): indica si se trata de un triángulo equilátero, isósceles o irregular.
#perímetro(): devuelve el perímetro del triángulo.

class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA=ladoA
        self.ladoB=ladoB
        self.ladoC=ladoC
        
    
    def area(self,altura):
        return (altura*self.ladoC)/2
    
    def forma(self):
        if self.ladoA==self.ladoB or self.ladoB==self.ladoC or self.ladoA==self.ladoC:
            print('El triangulo es isoceles')
        elif self.ladoA==self==ladoB==ladoC:
            print('El triangulo es equilatero')
        else:
            print('El triangulo es regular')
    
    def perimetro(self):
        print(f'El perimetro del triangulo es: {self.ladoA+self.ladoB+self.ladoC}')
        
mi_triangulo=Triangulo(5,8,10)
print(mi_triangulo.area(7))
mi_triangulo.forma()
mi_triangulo.perimetro()         