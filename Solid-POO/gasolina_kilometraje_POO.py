#Crea la clase Coche que contenga las siguientes propiedades:
#matrícula (string)
#marca (string)
#kilometros_recorridos (float)
#gasolina (float)
#La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros a conducir 
#y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. El método también restará 
#al valor de gasolina el resultado de los kilómetros multiplicado por 0.1. La clase también contendrá otro método
#llamado repostar() que recibirá como argumento los litros introducidos que deberán sumarse a la variable gasolina.
#Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la gasolina.
#En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario repostar para recorrer la cantidad indicada de 
#kilómetros".

class Coche:
    def __init__(self,matricula='BYB-363',marca='Toyota',kilometros_recorridos=0.0,gasolina=5.0):
        self.matricula=matricula
        self.marca=marca
        self.kilometros_recorridos=kilometros_recorridos
        self.gasolina=gasolina
        
    def avanzar(self,recorrido):
        self.kilometros_recorridos+=recorrido
        print(f'Se ha recorrido: {self.kilometros_recorridos} Km.')
        self.gasolina-=0.05*recorrido
        if self.gasolina<=0.1:
            self.gasolina=0
            print('No tienes gasolina nesesitas repostar')
        else:
            print(f'te queda de gasolina: {self.gasolina} galones')
    
    def repostar(self,cantidad):
        self.gasolina+=cantidad
        print(f'Se tiene de gasolina: {self.gasolina} galones')

mi_coche=Coche('BYB-363','Toyota',kilometros_recorridos=0.0,gasolina=15.0)
mi_coche.avanzar(50)
mi_coche.avanzar(100)
    
    
        

