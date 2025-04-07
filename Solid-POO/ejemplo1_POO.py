#creando una clase vacia
class Perro:
    #atributos de la clase
    especie='mamifero'
    def __init__(self,nombre,raza):
        #asignamos atributos al objeto
        self.nombre=nombre
        self.raza=raza
        print(f'El perro que es  se llama {self.nombre} y es de raza {self.raza}')
    def ladrar(self):
        print(f'Mi perro {self.nombre} ladra guau guau')
    
    def correr(self,pasos):
        print(f'Mi perro {self.nombre} corre {pasos} pasos')

#creamos un objeto de la clase Perro
mi_perro=Perro('Firulais','Labrador')
#print(type(mi_perro))
print(f'{mi_perro.nombre} es un {mi_perro.especie}')
mi_perro.ladrar()
mi_perro.correr(10)
