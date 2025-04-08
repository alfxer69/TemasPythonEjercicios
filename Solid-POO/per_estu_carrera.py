#Ejercicio 4
#Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”. Por tanto:
#En la clase “Persona” su método __init__() debe de estar preparado para recibir nombre y apellido.
#Además, esta clase , debe tener un método para mostrar nombre_completo() el cual debe mostrar el nombre
#acompañado del apellido.La otra clase “Estudiante”, debe de poder heredar de “Persona”, y además recibir
#los argumentos nombre y edad. También la clase “Estudiante”, recibe el valor “carrera”, y además contar 
#con un método mostrar_carrera(). Las dos clases son obligatorias.

class Persona:
    #constructor
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    
    def nombre_completo(self):
        print(f'El nombre completo es: {self.nombre} {self.apellido}')

class Estudiante(Persona):
    #constructor
    def __init__(self,nombre,apellido,edad,carrera):
        super().__init__(nombre,apellido) #Llamada al constructor de la clase padre
        self.edad=edad
        self.carrera=carrera

    def mostrar_carrera(self):
        print(f'El estudiante {self.nombre} {self.apellido} con carrera {self.carrera} y edad {self.edad} años')

class Profesor(Persona):
    #constructor
    def __init__ (self,nombre,apellido,edad,curso):
        super().__init__(nombre,apellido)
        self.edad=edad
        self.curso=curso
    
    def mostrar_curso(self):
        print(f'El profesor {self.nombre} {self.apellido} con edad de {self.edad} años enseña el curso de {self.curso}')

estudiante=Estudiante('Juan','Pérez',20,'Ingeniería')
estudiante.nombre_completo()
estudiante.mostrar_carrera()
print('-'*50)
profesor=Profesor('Ana','Gómez',35,'Matemáticas')
profesor.nombre_completo()
profesor.mostrar_curso()    