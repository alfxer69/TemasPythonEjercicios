class Vehiculos:
    def __init__(self,marca,modelo) -> None:
        self.marca=marca
        self.modelo=modelo
       
    def start(self):
        print(f'{self.marca} {self.modelo}  esta moviendose')

class Auto(Vehiculos):
    
    def __init__(self,marca,modelo,puertas,ruedas,motor,color):
        super().__init__(marca,modelo)
        self.puertas=puertas
        self.motor=motor
        self.color=color
        self.ruedas=ruedas
    
    def start(self):
        #super().start()
        print(f'{self.marca} {self.modelo} con {self.puertas} puertas motor {self.motor} cc con {self.ruedas} ruedas con color {self.color} esta lista para moverse')

class Bicicleta(Vehiculos):
    def __init__(self, marca, modelo,color,ruedas) -> None:
        super().__init__(marca, modelo)
        self.color=color
        self.ruedas=ruedas
    
    def start(self):
        print(f'{self.marca} {self.modelo} de color {self.color} de {self.ruedas} ruedas y la bicicleta esta lista para moverse')

class Motocicleta(Vehiculos):
    def __init__(self, marca, modelo,motor,color,ruedas) -> None:
        super().__init__(marca, modelo)
        self.motor=motor
        self.color=color
        self.ruedas=ruedas
        
    def start(self):
        print(f'{self.marca} {self.modelo} con  motor {self.motor} cc de {self.ruedas} ruedas y color {self.color} esta lista para moverse')

print('\n')
miauto=Auto('toyota','corolla',4,4,1.6,'gris')
mibicicleta=Bicicleta('Oxford','M3','black',2)   
mivehiculo=Vehiculos('areronave','jet')   
mimotocicleta=Motocicleta('yamaja','R3',150,'negro',2)

miauto.start()
mibicicleta.start()
mivehiculo.start()
mimotocicleta.start()
