from abc import ABC,abstractmethod

class Manejadorpedidos(ABC):
    pass

class pedidoparallevar(Manejadorpedidos):
    def procesar_pedido(self,detalles):
        print(f'Procesando pedido para llevar: {detalles}')

class pedidolocal(Manejadorpedidos):
    def procesar_pedido(self,detalles):
        print(f'Procesando pedido local: {detalles}')

class pedidodelivery(Manejadorpedidos):
    def procesar_pedido(self,detalles):
        print(f'Procesando pedido delivery: {detalles}')

class Restaurante():
    def __init__(self,nombre)->None:
        self.nombre=nombre
        self.manejadores_pedido=[]
    
    def registrar_pedidos(self,pedido):
        self.manejadores_pedido.append(pedido)
    
    def realizar_pedido(self,detalles):
        for pedido in self.manejadores_pedido:
            return pedido.procesar_pedido(detalles)

restaurante=Restaurante('El Gran Ristorant')
restaurante.registrar_pedidos(pedidoparallevar())
restaurante.realizar_pedido('Tallarines al pesto')