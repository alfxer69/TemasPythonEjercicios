class Perro:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
        self.buddy=None
    
    def ladrar(self):
        print(f'el perro {self.nombre} esta ladrando!')
    
    def info_perro(self):
        print(self.nombre+' tiene '+str(self.edad) +' años de edad')
    
    def cumple(self):
        self.edad+=1
    
    def setBuddy(self,buddy):
        self.buddy=buddy
        buddy.buddy=self #establece relacion reciproca
    
    def __str__(self) -> str:
        if self.buddy:
            return f'{self.nombre} es amigo de {self.buddy.nombre}'
        return f'{self.nombre} no tiene amigos'
    
miperro=Perro('Dolar',3)
print(f'Mi perro {miperro.nombre} tiene {miperro.edad} años de edad')

print(miperro.ladrar())

ozzy=Perro('ozzy',4)
skippy=Perro('Skyppy',12)
filou=Perro('filou',8)

ozzy.info_perro()
skippy.info_perro()
filou.info_perro()

ozzy.cumple()
print(ozzy.edad)

ozzy=Perro('ozzy',2)
filou=Perro('firou',8)

#establecer relacion de amistad
filou.setBuddy(ozzy)

print(ozzy.buddy.nombre)
print(ozzy.buddy.edad)

ozzy.buddy.info_perro()