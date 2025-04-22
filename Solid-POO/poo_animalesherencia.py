class Animal:
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        print('Wuao Wuao!!')

class Gato(Animal):
    def hacer_sonido(self):
        print('Miau Miau!')

miperro=Perro()
miperro.hacer_sonido()
migato=Gato()
migato.hacer_sonido()