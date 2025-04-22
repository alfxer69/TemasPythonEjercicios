import random
from datetime import datetime
from dateutil.relativedelta import relativedelta



def nombre_cliente():
    nombre_clte='Alfredo'
    apellido_clte='Muñoz'
    nombre_completo=f'{nombre_clte}  {apellido_clte}'
    return nombre_completo

def fecha_de_expiracion():
    fecha_de_creacion=datetime.now()
    f_expiracion=fecha_de_creacion+relativedelta(years=2)
    f_expiracion=f_expiracion.strftime('%m-%Y')
    return f_expiracion

def clave_cvv():
    cvv=random.randint(100,999)
    cvv=str(cvv)
    cvv_encrip='*'*3
    return cvv_encrip


class Cuenta_Bancaria:
    def __init__(self,numero_cta,saldo=0) -> None:
        self.saldo=saldo
        self.numero_cta=numero_cta
    
    def creacion_numero_cta(self,nro_cta):
        cuenta_encriptada='*'*6+nro_cta[-4:]
        return cuenta_encriptada

    def Deposito(self,monto):
        if monto>0:
            self.saldo+=monto
        else:
            print('No se puede adicionar un monto negativo')
    
    def Retiro(self,monto):
        if 0<monto and monto<=self.saldo:
            self.saldo-=monto
        else:
            print('No hay suficiente saldo para retirar')
    
    def Ver_Saldo(self):
        cuenta=self.creacion_numero_cta(nro_cta)
        print(f'El saldo de la cuenta {cuenta} es {self.saldo} soles')
    
    def Informacion_Cta(self):
        print('\n')
        print('El numero de cta es: ',self.creacion_numero_cta(nro_cta))
        print('Nombre del cliente: ',nombre_cliente())
        print('Fecha de expiración de la tarjeta: ',fecha_de_expiracion())
        print('El CVV de la tarjeta: ',clave_cvv())
    
        
nro_cta=random.randint(1000000000,9999999999)
nro_cta=str(nro_cta)        
        
cuenta=Cuenta_Bancaria(nro_cta,0)
cuenta.Deposito(100)
cuenta.Ver_Saldo()
cuenta.Deposito(400)
cuenta.Ver_Saldo()
cuenta.Retiro(200)
cuenta.Ver_Saldo()
cuenta.Informacion_Cta()