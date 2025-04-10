#Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se encuentra 
#cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá realizar los siguientes 
#movimientos:
#Avanzar hacia adelante (A)
#Retroceder (R)
#Avanzar hacia la izquierda (I) o hacia la derecha (D)
#El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método, posicion_actual(), 
#que indicará su posición en las coordenadas X e Y. Al crear el robot este se inicializará a las coordenadas (0,0).

class Robot:
    def __init__(self):
        self.X=0
        self.Y=0
        
    
    def mueve(self,orden):
        if orden.upper()=='A':
            self.Y+=1
        elif orden.upper()=='R':
            self.Y-=1
        elif orden.upper()=='I':
            self.X-=1
        elif orden.upper()=='D':
            self.X+=1
        else:
            print('Se a introducido una orden erronea o se sale del programa')
            
    def posicion_actual(self):
        print(f'La posición es: {self.X} , {self.Y}')

mi_robot=Robot()
orden='A'
while orden!='fin':
    orden=input('Ingresar la orden al Robot: (A:adelante,R:retroceder,D:derecha,I:izquierda,fin:terminar) ')
    mi_robot.mueve(orden)
    mi_robot.posicion_actual()
        
        

        