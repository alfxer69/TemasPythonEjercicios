#Ejercicio 1
#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del 
#alumno.Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
#nota y si ha aprobado o no.

class Estudiante:
    numero_estudiantes = 0 #atributo de clase
    #constructor    
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        Estudiante.numero_estudiantes+=1 #incrementa el contador de estudiantes
    
    def imprimir (self):
        print(f'El nombre del estudiante es {self.nombre} y su nota es {self.nota}')
    
    def nota_resultado(self):
        if self.nota>=6:
            print(f'El estudiante  {self.nombre} ha aprobado con una nota de {self.nota}')
        else:
            print(f'El estudiante  {self.nombre} ha desaprobado con una nota de {self.nota}')

estudiante1=Estudiante('Juan Altamirano',8)
estudiante2=Estudiante('Pedro Asca',4)
estudiante3=Estudiante('Luis Rodriguez',9)

estudiante1.imprimir()
estudiante1.nota_resultado()
estudiante2.imprimir()
estudiante2.nota_resultado()
estudiante3.imprimir()
estudiante3.nota_resultado()    
print()
print((f'La cantidad de estudiantes es: {Estudiante.numero_estudiantes}'))