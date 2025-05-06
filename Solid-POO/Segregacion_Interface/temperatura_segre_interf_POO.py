class Temperatura:
    def __init__(self,celsius:float)->None:
        self.celsius=celsius
    
    @property
    def celsius(self):
        """Getter para el atributo celcius"""
        return self._celsius
    
    @celsius.setter 
    def celsius(self,valor:float)->None:
        """Setter para el atributo celsisus"""
        if valor<-273.15:
            raise ValueError('La temperatura no puede ser cero absoluto')
        self._celsius=valor
        
temperatura=Temperatura(25)
print(temperatura.celsius) #deberia imprimir 25        
