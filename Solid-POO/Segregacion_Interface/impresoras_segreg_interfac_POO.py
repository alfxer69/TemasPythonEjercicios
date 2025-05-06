from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
class Escaner(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass
class Fax(ABC):
    @abstractmethod
    def enviar_fax(self, documento):
        pass

class Impresora_antigua(Impresora):
    def imprimir(self,documento):
        print(f'Imprimiendo {documento}')

class Impresora_moderna(Impresora, Escaner, Fax):
    def imprimir(self, documento):
        print(f'Imprimiendo {documento}')
    
    def escanear(self, documento):
        print(f'Escaneando {documento}')
    
    def enviar_fax(self, documento):
        print(f'Enviando fax de {documento}')


def dispositivo_impresora(impresora:Impresora,documento:str)->None:
    """Funcion que recibe un objeto de tipo Impresora y un documento"""
    impresora.enviar_fax(documento)


fax=Impresora_moderna()
dispositivo_impresora(fax,'documento1.pdf')

