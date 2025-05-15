from abc import ABC,abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self,mensaje:str,receptor:str):
        pass
    
class EmailSender(MessageSender):
    def send(self,mensaje:str,receptor:str):
        print(f'Enviando email: {mensaje} para {receptor}')

class SMSSender(MessageSender):
    def send(self,mensaje:str,receptor:str):
        print(f'Enviando SMS: {mensaje} para {receptor}')

class WhatsAppSender(MessageSender):
    def send(self,mensaje:str,receptor:str):
        print(f'enviando mensaje por WhatsApp: {mensaje} para {receptor}')

class GestorMensajes:
    def __init__(self,sender:MessageSender):
        self.sender=sender
    
    def send(self,mensaje:str,receptor:str):
        self.sender.send(mensaje,receptor)

#ejemplos de uso
email=EmailSender()
gestor=GestorMensajes(email)
gestor.send('Hola como estas', "Alfredo")

        
    