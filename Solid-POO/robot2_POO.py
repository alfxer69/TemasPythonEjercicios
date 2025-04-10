#Mejora el ejercicio anterior de forma que el robot pueda recibir una secuencia de movimientos.
#Por ejemplo: mueve("AADDADIR"). También deberá tener otros dos métodos: uno que devuelva todas
#las órdenes recibidas y otro capaz de listar los movimientos necesarios para volver a la 
#posición inicial (0,0).


import sys
sys.path.insert(0, r'C:\Users\Usuario\Desktop\TemasPythonEjercicios\Solid-POO')
from robot_POO import Robot

class RobotMejorado(Robot):
    def mueven(self,movimientos):
        self.historial_movimientos.append(movimientos)
        for movimiento in movimientos.upper():
            self.mueve(movimiento)
        
    def movimiento_total(self):
        return ''.join(self.historial_movimientos)
    
    def punto_inicial(self):
        robot_move=[]
        #Eje X
        if self.X>0:
            robot_move.extend(['I']*self.X)
        elif self.X<0:
            robot_move.extend(['D']*abs(self.X))
        #Eje Y
        if self.Y>0:
            robot_move.extend(['R']*self.Y)
        elif self.Y<0:
            robot_move.extend(['A']*abs(self.Y))
        print(''.join(robot_move))    

mi_robot=RobotMejorado()
movimientos=input('Ingresar la orden al Robot: (A:adelante,R:retroceder,D:derecha,I:izquierda,fin:terminar) ')
mi_robot.mueven(movimientos)
mi_robot.posicion_actual()
print(mi_robot.movimiento_total())
mi_robot.punto_inicial()
  
        