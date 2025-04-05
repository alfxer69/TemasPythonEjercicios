class Vehiculo:
    #abstrahemos los atributos y metodos de un vehiculo 
    #para crear una clase base
    
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0
        self.encendido = False

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")
    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} está encendido.")
    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        print(f"{self.marca} {self.modelo} está apagado.")
    def acelerar(self,incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"{self.marca} {self.modelo} ha acelerado a {self.velocidad} km/h.")
    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad -decremento>=0:
                self.velocidad -= decremento
                print(f"{self.marca} {self.modelo} ha frenado a {self.velocidad} km/h.")
            else:
                self.velocidad = 0
                print(f"{self.marca} {self.modelo} ha detenido.")
        else:
            print(f"{self.marca} {self.modelo} está apagado, encienda el vehiculo. No se puede frenar.")
            
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2= Vehiculo("Honda", "Civic", 2019)
vehiculo3=Vehiculo("Ford", "Mustang", 2021)
vehiculo4=Vehiculo("Chevrolet", "Camaro", 2022)

vehiculo1.mostrar_info()
vehiculo2.mostrar_info()
print()
vehiculo1.encender()
vehiculo1.acelerar(20)
vehiculo1.frenar(10)
vehiculo1.frenar(10)
print()
vehiculo2.encender()
vehiculo2.acelerar(30)
vehiculo2.frenar(20)
vehiculo2.frenar(20)
print()
vehiculo3.encender()
vehiculo3.acelerar(50)
vehiculo3.frenar(40)
vehiculo3.frenar(20)        
print()
