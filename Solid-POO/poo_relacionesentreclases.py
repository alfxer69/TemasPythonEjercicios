class Profesor:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        self.alumnos=[]
    
    def mostrar_profesor(self):
        return f'El profesor es: {self.nombre}'
    
    def agregar_estudiante(self,estudiante):
        self.estudiante=estudiante
        self.alumnos.append(estudiante)
    
    def mostrar_estudiantes(self):
        for self.estudiante in self.alumnos:
            print(f'Estudiante: {self.estudiante} de profesor {self.nombre}')

profesor1=Profesor('Jorge Castillo')
print(profesor1.mostrar_profesor())
profesor1.agregar_estudiante('Alberto Jimenez')
profesor1.agregar_estudiante('Jorge Marquez')
profesor1.mostrar_estudiantes()
            