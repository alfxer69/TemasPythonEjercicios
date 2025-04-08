#Ejercicio 5
#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden
#de Fabrica, las cuales son Moto y Carro.Crear métodos que muestren la cantidad de llantas, color y precio de ambos 
#transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

class Fabrica:
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio
    

class Moto(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')    

class Carro(Fabrica):
       
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')
        
class Camioneta(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')

class Bicicleta(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')

class Scooter(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')

class Avion(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')   

class Autobus(Fabrica):
    
    def mostrar_atributos(self):
        print(f'Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio} dolares')
        
    
mi_moto=Moto(2,'Rojo',1500)
mi_carro=Carro(4,'Azul',20000)
mi_scooter=Scooter(2,'Verde',500)
mi_bicicleta=Bicicleta(2,'Amarillo',200)
mi_avion=Avion(16,'Blanco',5000000)
mi_autobus=Autobus(6,'Gris',80000)

print('Atributos de Vehiculos:')
mi_moto.mostrar_atributos()
mi_carro.mostrar_atributos()
mi_scooter.mostrar_atributos()
mi_bicicleta.mostrar_atributos()
mi_avion.mostrar_atributos()
mi_autobus.mostrar_atributos()



    
        
