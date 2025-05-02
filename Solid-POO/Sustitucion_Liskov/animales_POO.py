class Animales:
    
    def proceso_alimentacion(self):
        pass

class AnimalesVertebrados(Animales):
    
    def proceso_alimentacion(self):
        pass

class AnimalesInvertebrados(Animales):
        
    def proceso_alimentacion(self):
        pass

#Animales vertebrados
class Vaca(AnimalesVertebrados):
    
    def __init__(self,raza):
        self.raza=raza
            
    def proceso_alimentacion(self,alimento):
        print(f'La vaca de raza {self.raza} es {alimento}')

class leon(AnimalesVertebrados):
    
    def __init__(self,raza):
        self.raza=raza
        
    def proceso_alimentacion(self,alimento):
        print(f'El leon de raza {self.raza} es {alimento}')

class Gaviota(AnimalesVertebrados):
    
    def __init__(self,raza):
        self.raza=raza
        
    def proceso_alimentacion(self,alimento):
        print(f'La gaviota de raza {self.raza} es {alimento}')

#Animales invertebrados
class Araña(AnimalesInvertebrados):
    
    def __init__(self,raza):
        self.raza=raza
        
    def proceso_alimentacion(self,alimento):
        print(f'La araña de raza {self.raza} es {alimento}')

class Mariposa(AnimalesInvertebrados):
    
    def __init__(self,raza):
        self.raza=raza
        
    def proceso_alimentacion(self,alimento):
        print(f'La mariposa de raza {self.raza} es {alimento}') 

class Hormiga(AnimalesInvertebrados):
    
    def __init__(self,raza):
        self.raza=raza
                
    def proceso_alimentacion(self,alimento):
        print(f'La hormiga de raza {self.raza} es {alimento}')

def realizar_alimentacion_vertebrados(animales:AnimalesVertebrados, alimento):
    animales.proceso_alimentacion(alimento)

def realizar_alimentacion_invertebrados(animales:AnimalesInvertebrados, alimento):
    animales.proceso_alimentacion(alimento)

mariposa=Mariposa('Monarca')
realizar_alimentacion_invertebrados(mariposa,'herbivora')

vaca=Vaca('Holstein')
realizar_alimentacion_vertebrados(vaca,'herbivora')

gaviota=Gaviota('Argentea')
realizar_alimentacion_vertebrados(gaviota,'herbivora')

leon=leon('Africano')
realizar_alimentacion_vertebrados(leon,'carnivora')