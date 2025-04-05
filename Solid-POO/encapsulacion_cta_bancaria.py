class Cuentabancaria:
    def __init__(self,numero_cuenta, saldo):
        self._numero_cuenta=numero_cuenta #atributo protegido
        self.__saldo=saldo #atributo privado
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        self.__saldo +=monto
            
    def retirar(self,monto):
        if self.__saldo>=monto:
            self.__saldo-=monto
        else:
            print('No hay suficiente saldo para retirar')


cuenta=Cuentabancaria(12345,1000)
print(cuenta._numero_cuenta) #Acceso al atributo protegido
print(cuenta.get_saldo()) #Acceso al atributo privado

valor=cuenta.get_saldo()
print(valor) #Acceso al atributo privado

cuenta.depositar(500)
print(cuenta.get_saldo()) #Acceso al atributo privado
cuenta.retirar(200)
print(cuenta.get_saldo()) #Acceso al atributo privado
    
