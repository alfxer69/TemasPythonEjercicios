from abc import ABC,abstractmethod

class Administradorsercicios(ABC):
    pass

class ServicioAjusteMotor:
    def procesar_servicio(self,detalle):
        return f'Se procesa Servicio de Motor: {detalle}'

class ServiciodeEngrase:
    def procesar_servicio(self,detalle):
        return f'Se procesa Servicio de Engrase {detalle}'
    
class ServiciodePintura:
    def procesar_servicio(self,detalle):
        return f'Se procesa Servicio de Pintura {detalle}'

class ServiciodeMantenimiento:
    def procesar_servicio(self,detalle):
        return f'Se procesa Servicio de Mantenimiento {detalle}'

class Taller:
    def __init__(self,nombre)->None:
        self.nombre=nombre
        self.tipos_servicios=[]
    
    def registrar_servicios(self,servicio):
        self.tipos_servicios.append(servicio)
    
    def realizar_servicio(self,detalle):
        for servicio in self.tipos_servicios:
            return print(f'{servicio.procesar_servicio(detalle)}')

class OrdendePagoServicio:
    
    def __init__(self):
        self.item=[]
        self.quantities=[]
        self.price=[]
        self.status='open'
    
    def add_item(self,name:str,quantity:int,price:float)->None:
        self.item.append(name)
        self.item.append(quantity)
        self.item.append(price)
    
class PaymentProcess:
    
    def pay(self,ordendepagoservicio=OrdendePagoServicio,security_code:str,payment_type:str):
        if payment_type=='debit':
            print(f'Processing Debit payment type')
            print(f'Verifyng security code {security_code}')
        elif payment_type=='credit':
            print('Processing Credit payment type')
            print(f'Verifyng security code {security_code}')
        elif payment_type=='cash':
            print('Processing Cash payment type')
            print(f'Verifyng security code {security_code}')
        else:
            raise Exception(f'Unknown payment type {payment_type}')

class CalculatorProcess:
    def total_price(self,ordendepagoservicio=OrdendePagoServicio):
        total=0
        for quantity,price in zip(ordendepagoservicio.quantity,ordendepagoservicio,price):
            total+=total*quantity
        return total
        
            
                
    
    

taller=Taller('Zentrum Audi')
taller.registrar_servicios(ServiciodeMantenimiento())
taller.realizar_servicio('Cambio de Filtro')

    