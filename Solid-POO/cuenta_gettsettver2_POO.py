#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de 
#la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación
#que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

#Un constructor.
#Los setters y getters para el nuevo atributo.
#En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear 
#un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en 
#caso contrario. Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.

class Cuenta:
    def __init__(self,titular='',cantidad=0.0):
        self.titular=titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad=cantidad
    
    def mostrar_cuenta(self):
        print(f'Titular: {self.titular} Cantidad: {self.cantidad}')
    
    def depositar(self,deposito):
        if deposito>0:
            self.cantidad+=deposito
        else:
            print('Error al ingresar el deposito')
        
    def retirar(self,retiro):
        if retiro>0:
            self.__cantidad-=retiro
        else:
            print('Error al realizar el retiro')
            
    def esTitularValido(self,edad):
        if edad>=18 and edad<=25:
            return True
        else:
            return False
        

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,bonificacion):
        super().__init__(titular,cantidad)
        self.__bonificacion=bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion
    
    def mostrar_cuenta_joven(self):
        print(f'Titular: {self.titular} Cantidad: {self.cantidad} Bonificacion: {(self.__bonificacion/100.0)*self.cantidad}')
        
    def retirar_cuenta_joven(self,retiro,edad):
        if retiro>0 and self.esTitularValido(edad)==True:
            self._Cuenta__cantidad-=retiro
        else:
            print('Error al realizar el retiro o no esta dentro de la edad')

cuentajoven1=CuentaJoven('Alfredo Muñoz',2000,10)
cuentajoven1.mostrar_cuenta_joven()
cuentajoven1.retirar_cuenta_joven(500,23)
cuentajoven1.mostrar_cuenta_joven()
cuentajoven1.depositar(300)
cuentajoven1.mostrar_cuenta_joven()    