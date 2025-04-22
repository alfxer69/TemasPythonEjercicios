from abc import ABC,abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass
    
    def detener(self):
        pass
    
class Moto(Vehiculo):
    def arrancar(self):
        return 'Motor de Moto Arranca'
    
    def detener(self):
        return 'Motor de Moto Detenido'
    
class Camion(Vehiculo):
    
    def arrancar(self):
        return 'Motor de Camion Arranca'
    
    def detener(self):
        return 'Motor de Camion Detenido'

mimoto=Moto()
print(mimoto.arrancar())
print(mimoto.detener())
print('\n')
micamion=Camion()
print(micamion.arrancar())
print(micamion.detener())
    