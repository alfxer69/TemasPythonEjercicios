from abc import ABC, abstractmethod

#abstraccion para el servicio de notificacion
class Notificador(ABC):
    
    @abstractmethod
    def enviar(self,mensaje:str):
        pass
    @abstractmethod
    def recepcion(self,enviado: bool):
        pass
    
    def notificador_de_recepcion(self):
        pass

#implementacion del servicio de notificacion para Email
class EmailNotificador(Notificador):
    
    def enviar(self,mensaje:str):
        print(f'Enviando email: {mensaje}')
        return True #simulando que el email fue enviado con exito
    def recepcion(self, enviado: bool):
        if enviado:
            print('Email enviado con exito')
        else:
            print('Error al enviar el email')
    
    def notificador_de_recepcion(self,receptor:str):
        print(f'Notificacion de recpcion de email a {receptor}: Su mensaje a sido recibido')
#implementacion del serivicio de notificacion para SMS
class SMSNotificador(Notificador):
    
    def enviar(self,mensaje:str):
        print(f'Enviando SMS: {mensaje}')
    
    def recepcion(self, enviado: bool):
        if enviado:
            print('SMS enviado con exito')
        else:
            print('Error al enviar el SMS')
    
    def notificador_de_recepcion(self,receptor:str):
        print(f'Notificacion de recpcion de SMS a {receptor}: Su mensaje a sido recibido')

#implementacion del serivio de notificacion para WhatsApp
class WhatsAppNoficador(Notificador):

    def enviar(self,mensaje:str):
        print(f'Enviando mensaje por WhasApp: {mensaje}')

    def recepcion(self, enviado: bool):
        if enviado:
            print('Mensaje de WhatsApp enviado con exito')
        else:
            print('Error al enviar el mensaje de WhatsApp')
    
    def notificador_de_recepcion(self,receptor:str):
        print(f'Notificacion de recpcion de WhatsApp a {receptor}: Su mensaje a sido recibido')  
    

#Clase o modulo de Alto Nivel que maneja la logica de los negocios
class App:
    def __init__(self,notificador:Notificador):
        self.notificador=notificador
    
    def enviar_notificacion(self,mensaje:str):
        self.notificador.enviar(mensaje)
        print('Notificacion enviada con exito')
    
    def recepcion(self,enviado: bool):
        self.notificador.recepcion(enviado)
        
    
    def notificador_de_recepcion(self,receptor:str):
        self.notificador.notificador_de_recepcion(receptor)
        
    
 
#Ejemplo de uso
emailnotificador=EmailNotificador()
app=App(emailnotificador)
app.enviar_notificacion('Hola, este es un mensaje de prueba')
app.recepcion(True)
app.notificador_de_recepcion('Alfredo')


whatsapp=WhatsAppNoficador()
app=App(whatsapp)
app.enviar_notificacion('Hola, este es un mensaje de prueba por WhatsApp')


sms=SMSNotificador()
app=App(sms)    
app.enviar_notificacion('Hola, este es un mensaje de prueba por SMS')    