class Animales():
    def speak():
        raise NotImplementedError('Subclase debe ser implementada en este metodo')

class Dog(Animales):
    def speak(self):
        return print('Woau Woau!')

class Cat(Animales):
    def speak(self):
        return print('Miau Miau!')

class Vaca(Animales):
    def speak(self):
        return print('Muu Muu!')

class Loro(Animales):
    def speak(self):
        return print('Eee Eee!')

class Mono(Animales):
    def speak(self):
        return print('UUaa UUaa')


mimono=Mono()
mimono.speak()
miloro=Loro()
miloro.speak()
print('\n')

animales=[Dog,Cat,Vaca,Loro,Mono]

for animal in animales:
    mianimal=animal()
    mianimal.speak()