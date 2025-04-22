class Coche():
    def __init__(self,marca,modelo,anio) -> None:
        self.marca=marca
        self.modelo=modelo 
        self.anio=anio
    
    def mostrar_info(self):
        return print(f'la marca {self.marca} de modelo {self.modelo} es del {self.anio}')
    
    def mostrar_antiguedad(self):
        return print(f'La antiguedad del auto {self.marca} es {2024-self.anio} años')

micoche=Coche('Toyota','Corolla',2018)
micoche.mostrar_info()
micoche.mostrar_antiguedad()
print('\n')
micoche2=Coche('Nissan','Sentra',2017)
micoche2.mostrar_info()
micoche2.mostrar_antiguedad()