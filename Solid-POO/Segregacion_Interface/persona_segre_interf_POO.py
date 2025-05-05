class Persona:
    def __init__(self,nombre:str)->None:
        self._nombre=nombre #atributo protegidos

    @property
    def nombre(self):
        """Getter para el atributo nombre"""
        return self._nombre

p=Persona('Juan')
print(p.nombre) #deberia imprimir 'Juan'