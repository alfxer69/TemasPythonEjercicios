from typing import Protocol

class PaymentMethod(Protocol):
    """Protolocolos para objetos que pueden realizar pagos"""
    
    def process_payment(self,amount:float)->bool:
        """Realiza el pago y devuelve True se el pago es exitoso"""
        ...
    
    def process_get_receipt(self)->str:
        """Devuelve el recibo de pago"""
        ...    

class CreditCard:
    """Clase que representa una tarjeta de credito"""
    
    def __init__(self,card_number:str,expiry:str):
        self.card_number=card_number
        self.expiry=expiry
    
    def process_payment(self,amount:float)->bool:
        """Procesa el pago con tarjeta de credito"""
        print(f'Pagando {self.card_number[-8:]} and {self.expiry} por ${amount}')
        return True
    
    def process_get_receipt(self)->str:
        """Devuelve el recibo de pago"""
        return f'Recibo de pago con tarjeta {self.card_number[-8:]}'

class Paypal:
    """Clase que representa una cuenta de Paypal"""
    
    def __init__(self,email:str):
        self.email=email
    
    def process_payment(self,amount:float)-> bool:
        """Proceso de pago con Paypal"""
        print(f'Pagando el ${amount} desde la cuenta de paypal {self.email}')
        return True
    
    def process_get_receipt(self)->str:
        """Devuelve el recibo de pago"""
        return f'Recibo depago con Paypal {self.email}'

def process_payment(payment_method:PaymentMethod,amount:float)->None:
    """Funcion generica que acepta cualquier objeto que cumpla con el protocolo """
    if payment_method.process_payment(amount):
        print('Pago Exitoso')
        print(payment_method.process_get_receipt())
    else:
        print('Pago Fallido')

card=CreditCard('1234-5678-9012-3456','12/25')
process_payment(card,100.0) #deberia imprimir 'Pago Exitoso' y el recibo de pago

paypal=Paypal('alfxer69@yahoo.com')
process_payment(paypal,150)   