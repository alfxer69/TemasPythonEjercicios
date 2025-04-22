class Estudiante:
    def __init__(self,nombre) -> None:
        self.nombre=nombre
        self.notas=[]
    
    def adicionar_notas(self,nota):
        if 0<=nota<=20:
            self.notas.append(nota)
        else:
            print('La nota esta fuera del Rango de 0 a 20')
    
    def promedio_nota(self):
        promedio=sum(self.notas)/len(self.notas)
        return promedio
    
    def __str__(self) -> str:
        mensaje=str(f'El promedio de {self.nombre} es {self.promedio_nota()}')
        return mensaje
    
estudiante1=Estudiante('Alfredo')
nota1=estudiante1.adicionar_notas(12)
nota2=estudiante1.adicionar_notas(14)
nota3=estudiante1.adicionar_notas(16)
nota4=estudiante1.adicionar_notas(10)
nota5=estudiante1.adicionar_notas(9)

print(estudiante1)
    
        