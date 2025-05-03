from abc import ABC, abstractmethod

class IAutomovilEncendido(ABC):
    
    @abstractmethod
    def encender_contacto(self):
        pass
    
    def apagar_contacto(self):
        pass

class IAutomovilDireccion(ABC):    
    
    @abstractmethod
    def acelerar(self, velocidad):
        pass
            
    def frenar(self):
        pass
    
    def girar(self, direccion):
        pass

class IAutomovilLuces(ABC):
    
    @abstractmethod
    def encender_luces(self):
        pass
    
    def apagar_luces(self):
        pass
    
    def encender_luces_altas(self):
        pass
    
    def encender_radio(self):
        pass
    
    def apagar_radio(self):
        pass
        
class IAutomovilTemperatura(ABC):
    @abstractmethod
    def verificar_temperatura(self,temperatura):
        pass

class AutomovilGasolinero(IAutomovilEncendido, IAutomovilLuces, IAutomovilTemperatura, IAutomovilDireccion):
    def encender_contacto(self):
        print("Encendiendo motor de gasolina...")
    
    def apagar_contacto(self):
        print("Apagando motor de gasolina...")
    
    def acelerar(self, velocidad):
        print(f"Acelerando a {velocidad} km/h...")
    
    def frenar(self):
        print("Frenando...")
    
    def girar(self, direccion):
        print(f"Girando a la {direccion}...")
    
    def encender_luces(self):
        print("Encendiendo luces...")
    def apagar_luces(self):
        print("Apagando luces...")
    def encender_luces_altas(self):
        print("Encendiendo luces altas...")
    def encender_radio(self):
        print("Encendiendo radio...")
    def apagar_radio(self):
        print("Apagando radio...")
    def verificar_temperatura(self, temperatura):
        if temperatura >= 70:
            print("Temperatura alta, encendiendo ventilador...")
        else:
            print("Temperatura normal.")

class AutomovilElectrico(IAutomovilEncendido, IAutomovilLuces, IAutomovilDireccion):

    def encender_contacto(self):
        print("Encendiendo motor electrico...")
    def apagar_contacto(self):
        print("Apagando motor electrico...")
    def acelerar(self, velocidad):
        print(f"Acelerando a {velocidad} km/h...")
    def frenar(self):
        print("Frenando...")
    def girar(self, direccion):
        print(f"Girando a la {direccion}...")
    def encender_luces(self):
        print("Encendiendo luces...")
    def apagar_luces(self):
        print("Apagando luces...")
    def encender_luces_altas(self):
        print("Encendiendo luces altas...")
    def encender_radio(self):
        print("Encendiendo radio...")
    def apagar_radio(self):
        print("Apagando radio...")
        
autoelectrico=AutomovilElectrico()
autoelectrico.encender_contacto()
autoelectrico.apagar_contacto()
autoelectrico.acelerar(100)
autoelectrico.frenar()
autoelectrico.girar("derecha")

automovilgasolinero=AutomovilGasolinero()
automovilgasolinero.encender_contacto()
automovilgasolinero.apagar_contacto()   
automovilgasolinero.acelerar(100)
automovilgasolinero.frenar()
automovilgasolinero.girar("izquierda")