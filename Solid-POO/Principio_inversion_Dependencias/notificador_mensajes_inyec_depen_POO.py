from abc import ABC, abstractmethod

#abstraccion para el servicio de notificacion
class Notificador(ABC):
    
    @abstractmethod
    def enviar(self,mensaje:str):
        pass

#implementacion del servicio de notificacion para Email
class EmailNotificador(Notificador):
    
    def enviar(self,mensaje:str):
        print(f'Enviando email: {mensaje}')

#implementacion del serivicio de notificacion para SMS
class SMSNotificador(Notificador):
    
    def enviar(self,mensaje:str):
        print(f'Enviando SMS: {mensaje}')

#implementacion del serivio de notificacion para WhatsApp
class WhatsAppNoficador(Notificador):
    
    def enviar(self,mensaje:str):
        print(f'Enviando mensaje por WhasApp: {mensaje}')

#Clase o modulo de Alto Nivel que maneja la logica de los negocios

class App:
    def __init__(self,notificador:Notificador):
        self.notificador=notificador
    
    def enviar_notificacion(self,mensaje:str):
        self.notificador.enviar(mensaje)
        print('Notificacion enviada con exito')

#Ejemplo de uso
emailnotificador=EmailNotificador()
app=App(emailnotificador)
app.enviar_notificacion('Hola, este es un mensaje de prueba')

whatsapp=WhatsAppNoficador()
app=App(whatsapp)
app.enviar_notificacion('Hola, este es un mensaje de prueba por WhatsApp')

sms=SMSNotificador()
app=App(sms)    
app.enviar_notificacion('Hola, este es un mensaje de prueba por SMS')    