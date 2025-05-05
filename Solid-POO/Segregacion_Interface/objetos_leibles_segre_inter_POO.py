from typing import Protocol, runtime_checkable

#definimos un protocolo para objetos que pueden ser leidos
@runtime_checkable
class Readable(Protocol):
    def read(self,size:int=-1)->str:
        """Lee y devuelve datos en cadena"""
        ...

#Clase que cumple con elProtocolo(si heredar explicitamente)
class StringReader:
    def __init__(self, contenido: str) -> None:
        self.contenido = contenido
        self.position = 0

    def read(self, size: int = -1) -> str:
        """Funcion para leer el contenido"""
        if size==-1:
            result=self.contenido[self.position:]
            self.position=len(self.contenido)
            return result
        else:
            result=self.contenido[self.position:self.position+size]
            self.position+=size
            return result

#Clase que no cumple con elprotocolo(no tiene read)
class BynaryStream:
    def read_bytes(self,size:int)->bytes:
        """Lee y devuelve bytes"""
        return b'datos-binarios'

#Funacion generica que acepta cualquier Readable
def process_readable(source: Readable) -> None:
    """Procesa un objeto que cumple con el protocolo Readable"""
    if isinstance(source,Readable):
        print(f'leyendo: {source.read(50)}')
    else:
        print('El objeto no es leible')

#Ejemplo de uso
reader=StringReader('Hola, mundo estamos mejorando todo este tema!')
process_readable(reader) #deberia funcionar

stream=BynaryStream()
process_readable(stream) #no deberia funcionar


        