class Motor:
    def inicio(self):
        pass
    def detener(self):
        pass

class MotorElectrico(Motor):
    pass

class MotorV8(Motor):
    pass

class Auto:
    clase_motor=Motor
    
    def __init__(self):
        self.motor=self.clase_motor()
    
    def inicio(self):
        print(
            f'Arrancando {self.motor.__class__.__name__} para el auto {self.__class__.__name__}'
            )
        self.motor.inicio()
    
    def detener(self):
        self.motor.detener()

class AutoCarrera(Auto):
    clase_motor=MotorV8

class AutoCiudad(Auto):
    clase_motor=MotorElectrico

class AutoF1(AutoCarrera):
    pass

auto=Auto()
autocarrera=AutoCarrera()
autociudad=AutoCiudad()
autof1=AutoF1()
autos=[auto,autocarrera,autociudad,autof1]

for coche in autos:
    coche.inicio()


        
