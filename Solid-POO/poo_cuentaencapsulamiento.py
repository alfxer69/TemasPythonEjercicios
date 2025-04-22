class Cuenta_Bancaria:
    def __init__(self,saldo,cliente) -> None:
        self.saldo=0
        self.cliente=cliente
    
    def deposito(self,monto):
        self.saldo+=monto
        print(f'se deposito el monto {monto} soles el saldo actual es {self.saldo} de la cuenta del Señor {self.cliente}')
    
    def retiro(self,monto):
        if 0<monto<=self.saldo:
            self.saldo-=monto 
        print(f'se retiro el monto {monto} soles el saldo actual es {self.saldo} de la cuenta del Señor {self.cliente}')
    def monto_cuenta(self):
        return print(f'El saldo actual del señor {self.cliente} es {self.saldo} soles')
        
      
cliente1=Cuenta_Bancaria(0,'Alfredo')       
cliente1.deposito(50)
cliente1.retiro(20)
cliente1.monto_cuenta()
