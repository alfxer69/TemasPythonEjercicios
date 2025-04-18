class Dormitorios:
    
    def getDorm(self):
        return 'Tiene 3 dormitorios'

class Departamento:
     
    def __init__(self,ubicacion,piso,dormitorios):
        self._ubicacion=ubicacion
        self._piso=piso
        self._dormitorios=dormitorios
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getPiso(self):
        return self._piso
    
    def getDormitorios(self):
        return self._dormitorios.getDorm()
    
class ImpresionCasa:
    
    def __init__(self,casas):
        self._casas=casas
    
    def printInfo(self):
        print(
                f'Ubicación: {self._casas.getUbicacion()} Piso: {self._casas.getPiso()} Dormitorios: {self._casas.getDormitorios()}'
              )

if __name__=='__main__':
    dormitorio=Dormitorios()
    departamento=Departamento(ubicacion='Miraflores',piso=3,dormitorios=dormitorio)
    impresion=ImpresionCasa(casas=departamento)
    impresion.printInfo()
    