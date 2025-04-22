def valida_positivo(func):
    def wraper(self,cantidad):
        if cantidad<0:
            raise ValueError('la cantidad debe ser positiva')
        return func(self,cantidad)
    return wraper

class CuentaBancaria:
    def __init__(self,titular) -> None:
        self._saldo=0
        self.titular=titular
    
    @valida_positivo
    def depositar(self,cantidad):
        self._saldo+=cantidad
    
    @valida_positivo
    def retirar(self,cantidad):
        if cantidad<=self._saldo:
            self._saldo-=cantidad
        else:
            print('Fondos insuficientes.')
    def consultar_saldo(self):
        return self._saldo

cuenta1=CuentaBancaria('Alfredo')
cuenta1.depositar(50)
print(cuenta1.consultar_saldo())
cuenta1.retirar(30)
print(cuenta1.consultar_saldo())

cuenta2=CuentaBancaria('Jose')
cuenta2.retirar(100) 
print(cuenta2.consultar_saldo())  