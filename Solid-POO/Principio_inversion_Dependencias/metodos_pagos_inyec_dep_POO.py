from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod 
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    
    def pay(self,amount):
        print(f'Pago con CreditCard por ${amount}')

class PaypalPayment(PaymentMethod):
    
    def pay(self,amount):
        print(f'Pago con Paypal por ${amount}')

class BankTranferPayment(PaymentMethod):
    def pay(self,amount):
        print(f'Pago con TransferBank ${amount}')

class GestorPayment:
    
    def __init__(self,paymentmethod: PaymentMethod):
        self.paymentmethod=paymentmethod
    
    def pay(self,amount):
        return self.paymentmethod.pay(amount)

#Casos de uso

creditcard=CreditCardPayment()
gestorcard=GestorPayment(creditcard)
gestorcard.pay(1000)

banktransfer=BankTranferPayment()
gestorbanktranfer=GestorPayment(banktransfer)
gestorbanktranfer.pay(2000)