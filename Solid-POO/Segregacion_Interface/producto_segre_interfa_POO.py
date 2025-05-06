class Producto:
    def __init__(self,precio:float)->None:
        self.precio=precio #atributo publico
    
    @property
    def precio(self):
        """Getter para el atributo precio"""
        return self._precio
    
    @precio.setter
    def precio(self,valor:float)->None:
        """Setter para el atributo precio"""
        if valor<0:
            raise ValueError('El precio no puede ser negativo')
        else:
            self._precio=valor

producto=Producto(100)
print(producto.precio) #deberia imprimir 100