class Animal:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        
    def hablar(self):
        print('El animal hace un sonido')

class Perro(Animal):
    def hablar(self):
        print('Guauu Guauu¡')

class Gato(Animal):
    def hablar(self):
        print('Miau Miau¡')

miperro=Perro('Max')
migato=Gato('Michi')

for animal in [miperro,migato]:
    animal.hablar()
