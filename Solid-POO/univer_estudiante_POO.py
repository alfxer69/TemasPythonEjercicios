#Ejercicio 7
#Desarrollar un programa con tres clases:
#La primera debe ser Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). 
#La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
#Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la 
#especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad:
    def __init__(self,nombre_universidad):
        self.nombre_universidad=nombre_universidad

class Carrera(Universidad):
    def __init__(self,nombre_universidad,carrera):
        super().__init__(nombre_universidad)
        self.carrera=carrera

class Estudiante(Carrera):
    def __init__(self,nombre_universidad,nombre,carrera,edad):
        super().__init__(nombre_universidad,carrera)
        self.nombre=nombre
        self.edad=edad
    
    def mostrar_info(self):
        print(f'Nombre: {self.nombre_universidad}, Nombre Alumno: {self.nombre}, Carrera: {self.carrera}, Edad: {self.edad} años')

# Crear un objeto de la clase Estudiante
estudiante=Estudiante('UNMSM','Juan Perez','Ingeniería de Sistemas','20')

estudiante.mostrar_info()