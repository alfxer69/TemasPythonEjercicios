from typing import Protocol

class IDepositar(Protocol):
    def depositar(self,monto:float)->None:
        ...
class IRetirar(Protocol):
    def retirar(self,monto:float)->None:
        ...
class ITransferir(Protocol):
    def transferir(self,monto:float)->None:
        ...
class IConsultar(Protocol):
    def consultar(self)->float:
        ...
class CuentaAhorros(IDepositar, IRetirar,IConsultar):
    def __init__(self, saldo:float)->None:
        self.saldo=saldo
    def depositar(self,monto:float)->None:
        print(f"Se ha depositado {monto} a la cuenta de ahorros")
        self.saldo+=monto
    def retirar(self,monto:float)->None:
        print(f"Se ha retirado {monto} soles de la cuenta de ahorros")
        if self.saldo>=monto:
            self.saldo-=monto
        else:
            print("No hay suficiente saldo")
    def consultar(self)->float:
        print(f'El saldo actual es de {self.saldo} soles')
class CuentaCorriente(IDepositar, IRetirar, ITransferir, IConsultar):
    def __init__(self,monto:float)->None:
        self.saldo=monto
    def depositar(self,monto:float)->None:
        print(f"Se ha depositado {monto} soles a la cuenta corriente")
        self.saldo+=monto
    def retirar(self,monto:float)->None:
        print(f"Se ha retirado {monto} soles de la cuenta corriente")
        if self.saldo>=monto:
            self.saldo-=monto
        else:
            print("No hay suficiente saldo")
    def transferir(self,monto:float,cuenta:str)->None:
        print(f"Se ha transferido {monto} soles de la cuenta corriente a la cuenta {cuenta}")
        if self.saldo>=monto:
            self.saldo-=monto
        else:
            print("No hay suficiente saldo")
    def consultar(self)->float:
        print(f'El saldo actual es de {self.saldo} soles')

def realizar_pago(cuenta:ITransferir,monto:float)->None:
    cuenta.transferir(monto)
   
    
cuentabancaria=CuentaCorriente(1000)
cuentabancaria.transferir(100,'123agjhgjg')



