class MetodoPagoBase:
    def procesar_pago(self):
        pass
    
class MetodoPagoAutomatico(MetodoPagoBase):
    def procesar_pago(self,cantidad):
        pass

class MetodoPagoManual(MetodoPagoBase):
    
    def procesar_pago(self,cantidad):
        pass
#Pagos automaticos  
class TarjetaCredito(MetodoPagoAutomatico):
    def __init__(self,numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta
    
    def procesar_pago(self,monto):
        print(f'Procesando pago automatico de {monto} con tarjeta de credito {self.numero_tarjeta}')

class Paypal(MetodoPagoAutomatico):
    def __init__ (self,email):
        self.email=email
    
    def procesar_pago(self,monto):
        print(f'Procesando pago automatico de {monto} con Paypal {self.email}')
        
class Efectivo(MetodoPagoAutomatico):
    def __init__(self,cantidad):
        self.cantidad=cantidad
    
    def procesar_pago(self,monto):
        print(f'Procesando pago automatico de {monto} en efectivo {self.cantidad}')

class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self,direccion):
        self.direccion=direccion

    def procesar_pago(self,monto):
        print(f'Procesando pago automatico de {monto} con Bitcoin a la direccion {self.direccion}')
#Pagos manuales
class PagoCheque(MetodoPagoManual):
    def __init__(self,numero_cheque):
        self.numero_cheque=numero_cheque
    
    def procesar_cheque(self,monto):
        print(f'Procesando pago manual de {monto} con cheque {self.numero_cheque}')

def realizar_pago_automatico(metodo_pago:MetodoPagoAutomatico, cantidad):
    metodo_pago.procesar_pago(cantidad)

def realizar_pago_manual(metodo_pago:MetodoPagoManual, cantidad):
    metodo_pago.procesar_cheque(cantidad)

tarjetacredito=TarjetaCredito('1234-5678-9012-3456')
paypal=Paypal('ventas@d-globalcom.com')
efectivo=Efectivo(1000)
pagobitcoin=PagoBitcoin('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
pago_cheque=PagoCheque('123456')

print('--- Formas de Pago ---')
realizar_pago_manual(pago_cheque, 1000)
realizar_pago_automatico(tarjetacredito, 1000)

