class Persona:
    def __init__(self,nombre:str)->None:
        self.nombre=nombre #atributo publico

    @property
    def nombre(self):
        """Getter:obtiene el valor"""
        return self._nombre.title()
    
    @nombre.setter
    def nombre(self,valor:str)->None:
        """Modifica el valor"""
        if not valor.strip():
            raise ValueError('El nombre no puede estar vacio')
        self._nombre=valor
    
    @nombre.deleter
    def nombre(self)->None:
        """Elimina el valor"""
        print('Eliminando nombre...')
        del self._nombre

p=Persona('maria')
print(p.nombre)

p.nombre='JUAN'
print(p.nombre) 

del p.nombre #elimina el atributo nombre
