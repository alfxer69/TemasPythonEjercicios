class Coche:
    def __init__(self,marca,modelo) -> None:
        self.marca=marca
        self.modelo=modelo
        self.velocidad=0
    
    def acelerar(self,incremento):
        self.velocidad += incremento
        print(f'El coche ha acelerado a {self.velocidad} km/h.')
    
    def frenar(self,decremento):
        self.velocidad-=decremento
        print(f'El coche ha frenado a {self.velocidad} km/h.')
    
#Crear un objeto de clase coche

coche1=Coche('Toyota','Hi-Lux')
coche1.acelerar(50)
coche1.frenar(20)