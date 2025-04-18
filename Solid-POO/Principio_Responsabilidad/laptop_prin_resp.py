class Procesador:
    
    def getProcesador(self):
        return 'Procesador 2.4Ghz'
    
class Disco:
    def getDisco(self):    
        return 'SSDD 500Gb'
    
class Laptop:
    
    def __init__(self,marca,pulgadas,precio,procesador,disco):
        self._marca=marca
        self._pulgadas=pulgadas
        self._precio=precio
        self._procesador=procesador
        self._disco=disco
    
    def getMarca(self):
        return self._marca
    
    def getPulgadas(self):
        return self._pulgadas
    
    def getPrecio(self):
        return self._precio
    
    def getProc(self):
        return self._procesador.getProcesador()
    
    def getDisc(self):
        return self._disco.getDisco()
    
class ImpresionLaptop:
    def __init__(self,laptop):
        self._laptop=laptop
    
    def impresionInfo(self):
        print(
            f'Marca: {self._laptop.getMarca()} Pulgadas: {self._laptop.getPulgadas()} Procesador: {self._laptop.getProc()} Disco: {self._laptop.getDisc()}'
            )

if __name__=='__main__':
    procesador=Procesador()
    disco=Disco()
    laptop=Laptop(marca='Lenovo',pulgadas='14',precio=1200,procesador=procesador,disco=disco)
    impresion=ImpresionLaptop(laptop=laptop)
    impresion.impresionInfo()
    
    
        