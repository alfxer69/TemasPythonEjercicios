class Productos:
    def __init__(self,nombre,precio) -> None:
        self.nombre=nombre
        self.precio=precio

class Store:
    def __init__(self) -> None:
        self.productos=[]
    
    def adicionar_productos(self,producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(f'Nombre del producto: {producto.nombre} y su precio es {producto.precio} soles')

miproducto1=Productos('detergente',10)
miproducto2=Productos('frejoles',15)
miproducto3=Productos('lejia',13)
miproducto4=Productos('botella de agua',5)
miproducto5=Productos('cocacola',6)
miproducto6=Productos('vino blanco',35)
miproducto7=Productos('vino tinto',40)
miproducto8=Productos('lentejas',14)

productos=[miproducto1,miproducto2,miproducto3,miproducto4,miproducto5,miproducto6,miproducto7,miproducto8]

mistore=Store()
for producto in productos:
    mistore.adicionar_productos(producto)

mistore.mostrar_productos()

