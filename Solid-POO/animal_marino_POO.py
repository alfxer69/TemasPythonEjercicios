#Ejercicio 6
#Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, 
#soy un animal marino!». Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar 
#por «Hola soy un Pulpo!». Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo
#nuevo llamado mensaje y que muestre ese mesjae como parámetro.

class Marino:
    def hablar(self):
        print('Hola, soy un animal Marino!')

class Pulpo(Marino):
    def hablar(self):
        print('Hola soy un pulpo!')

class Foca(Marino):
    def __init__(self,mensaje):
        self.mensaje=mensaje
        
    def hablar(self):
        print(f'{self.mensaje}')


mi_marino=Marino()
mi_pulpo=Pulpo()

mi_marino.hablar()
mi_pulpo.hablar()

mi_foca=Foca('Hola soy una Foca!')
mi_foca.hablar()