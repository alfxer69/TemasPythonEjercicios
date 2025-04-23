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
        self.items=[]
        self.quantities=[]
        self.prices=[]
        self.status='open'
    
    def add_item(self,name:str,quantity:int,price:float)->None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
class PaymentProcess:
    def pay(self,ordendepagoservicio:OrdendePagoServicio,security_code:str,payment_type:str):
        if payment_type=='debit':
            print(f'Processing Debit payment type')
            print(f'Verifyng security code {security_code}')
            ordendepagoservicio.status='paid'
            print(f'El Servicio esta: {ordendepagoservicio.status}')
        elif payment_type=='credit':
            print('Processing Credit payment type')
            print(f'Verifyng security code {security_code}')
            ordendepagoservicio.status='paid'
            print(f'El Servicio esta: {ordendepagoservicio.status}')
        elif payment_type=='cash':
            print('Processing Cash payment type')
            print(f'Verifyng security code {security_code}')
            ordendepagoservicio.status='paid'
            print(f'El Servicio esta: {ordendepagoservicio.status}')
        else:
            raise Exception(f'Unknown payment type {payment_type}')

class CalculatorProcess:
    def total_price(self,ordendepagoservicio:OrdendePagoServicio):
        total=0
        for quantity,price in zip(ordendepagoservicio.quantities,ordendepagoservicio.prices):
            total+=price*quantity
        return total

taller=Taller('Zentrum Audi')
print(f'Taller {taller.nombre}')
taller.registrar_servicios(ServiciodeMantenimiento())
taller.realizar_servicio('Cambio de Filtro')

orden=OrdendePagoServicio()
orden.add_item('Aceites',3,20.40)
orden.add_item('Bujias',4,20.50)
orden.add_item('Mano de Obra',1,100)
orden.add_item('Escaneo',1,50)
paymentprocess=PaymentProcess()
paymentprocess.pay(orden,'12345','debit')
total_pay=CalculatorProcess()
print(f'El pago total es: {total_pay.total_price(orden)} soles')
