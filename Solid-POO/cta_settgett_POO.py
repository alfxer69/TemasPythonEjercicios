#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
#y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
#Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
#directamente, sólo ingresando o retirando dinero. 
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

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

cuenta1=Cuenta('Alfredo Muñoz',2000)
cuenta1.mostrar_cuenta()
cuenta1.depositar(500)
cuenta1.mostrar_cuenta()
cuenta1.retirar(200)
cuenta1.mostrar_cuenta()