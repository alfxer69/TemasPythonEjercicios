from abc import ABC, abstractmethod

#definir la ABSTRACCION del servicio de almacenamieneto de productos

class AlmacenamientoProductos(ABC):
    @abstractmethod
    def agregar_producto(self,nombre:str,cantidad:int):
        pass
    @abstractmethod
    def obtener_stock(self,nombre:str)-> int:
        pass
    
    @abstractmethod
    def eliminar_stock(self,nombre:str,cantidad:int):
        pass

#implementacion del servicio de almacenamiento de productos en un inventario
#METODO DE BAJO NIVEL --> detallado
class MemoriaAlmacenamientoProductos(AlmacenamientoProductos):
    def __init__(self):
        self.inventario = {}
    
    def agregar_producto(self,nombre:str,cantidad:int):
        if nombre in self.inventario:
            self.inventario[nombre]+=cantidad
        else:
            self.inventario[nombre]=cantidad
            
    def obtener_stock(self, nombre:str)-> int:
        return self.inventario.get(nombre,0)
    
    def eliminar_stock(self,nombre:str,cantidad:int):
        if nombre in self.inventario:
            if self.inventario[nombre]>=cantidad:
                self.inventario[nombre]-=cantidad
            else:
                print(f'No hay suficiente stock de {nombre} solo eliminamos {cantidad-self.inventario[nombre]} unidades stock cero')
                self.inventario[nombre]=0
        else:
            print(f'No existe el producto {nombre} en el inventario')
        
#METODO DE ALTO NIVEL --- logica de negocios

class GestorProductos:
    def __init__(self,almacenamiento:AlmacenamientoProductos):
        self.almacenamiento=almacenamiento
    
    def agregar_producto(self,nombre:str,cantidad:int):
        self.almacenamiento.agregar_producto(nombre,cantidad)
        print(f'Producto {nombre} agregado al inventario con cantidad {cantidad} unidades')
    
    def obtener_stock(self,nombre:str):
        stock=self.almacenamiento.obtener_stock(nombre)
        print(f'Stock de {nombre} : {stock}')
        return stock
    
    def eliminar_stock(self,nombre:str,cantidad:int):
        self.almacenamiento.eliminar_stock(nombre,cantidad)
        print(f'Se eliminaron {cantidad} unidades de {nombre} del inventario')
        
#Ejemplo de uso
memoriaproductos=MemoriaAlmacenamientoProductos()
gestor=GestorProductos(memoriaproductos)
gestor.agregar_producto('Pantalones',15)
print('----')
gestor.agregar_producto('Camisas',10)
gestor.obtener_stock('Pantalones')
gestor.obtener_stock('Camisas')
gestor.eliminar_stock('Pantalones',25)
gestor.obtener_stock('Pantalones')

