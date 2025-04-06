#Este es un ejemplo del uso de la herencia en POO
class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def describir(self):
        return f'Este vehiculo esde la marca {self.marca} de modelo {self.modelo}'
    
class Automovil(Vehiculo):
    def __init__(self,marca,modelo,puertas):
        super().__init__(marca,modelo) #Llamada al constructor de la clase padre
        self.puertas=puertas
   
    def describir(self):
        return f'Este automovil es de la marca {self.marca} de modelo {self.modelo} y tiene {self.puertas} puertas'
    
class Camion(Automovil):
    def __init__(self,marca,modelo,puertas,carga):
        super().__init__(marca,modelo,puertas)
        self.carga=carga
    
    def describir(self):
        return f'Este camion es de la marca {self.marca} del modelo {self.modelo} , con {self.puertas} puertras y carga {self.carga} Kg.'

vehiculo1=Automovil('Toyota','Corolla',4)
vehiculo2=Camion('Ford','F-150',2,1000)

print(vehiculo1.describir())
print(vehiculo2.describir())


