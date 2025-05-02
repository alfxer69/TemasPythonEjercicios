class Vehiculos:
    def desarrollar_velocidad(self):
        pass

class VehiculosMotorizados(Vehiculos):
    def desarrollar_velocidad(self):
        pass

class VehiculosNoMotorizados(Vehiculos):
    def desarrollar_velocidad(self):
        pass

#Vehiculos motorizados
class Automovil(VehiculosMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'El automovil de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')

class Bus(VehiculosMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'El bus de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')

class Camion(VehiculosMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'El camion de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')

class Motocicleta(VehiculosMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'La motocicleta de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')

#Vehiculos no motorizados
class Bicicleta(VehiculosNoMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'La bicicleta de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')   

class Patineta(VehiculosNoMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'La patineta de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')

class AutoElectrico(VehiculosMotorizados):
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def desarrollar_velocidad(self,velocidad):
        print(f'El auto electrico de marca {self.marca} con modelo {self.modelo} desarrolla la velocidad de {velocidad} km/h')


def realizar_automovil_con_motor(automovil:VehiculosMotorizados, velocidad):
    automovil.desarrollar_velocidad(velocidad)

def realizar_automovil_sin_motor(automovil:VehiculosNoMotorizados, velocidad):
    automovil.desarrollar_velocidad(velocidad)


automovil=Automovil('Toyota','Corolla')
patineta=Patineta('Xiaomi','M365')

realizar_automovil_con_motor(automovil, 180)
realizar_automovil_sin_motor(patineta, 20)