from typing import Protocol

class SupportsAdd(Protocol):
    """Protocolo para objetos que pueden ser sumados"""
    
    def __add__(self, other: 'SupportsAdd') -> 'SupportsAdd':
        """Realiza la suma de dos objetos"""
        ...
def double(valor:SupportsAdd)->SupportsAdd:
    """Devuelve el doble del valor"""
    return valor + valor

def triple(valor: SupportsAdd)->SupportsAdd:
    """Devuelve el triple del valor"""
    return valor + valor + valor

print(double(5))    #deberia imprimir 10
print(triple('a')) #deberia imprimir 'aaa'
