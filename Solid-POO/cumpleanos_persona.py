#Ejercicio 2
#Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”, que aumente 
#en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”. Tendríamos que lograr ejecutar
#el siguiente código con la clase creada:

#p=Persona(«Nombre», edad)
#p.cumpleaños()
#print(f»{p.nombre} cumple {p.edad} años»)

class Persona:
    numero_personas = 0 #atributo de clase  
    #constructor
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        Persona.numero_personas+=1
    
    def cumpleaños(self):
        self.edad+=1
        print(f'{self.nombre} cumple {self.edad} años')

persona1=Persona('Juan Malmo',25)
persona2=Persona('Mariano Lopez',30)
persona3=Persona('Pedro Asca',40)

persona1.cumpleaños()
persona2.cumpleaños()
persona3.cumpleaños()
print()
print(f'la cantidad de personas consultadas es: {Persona.numero_personas}')