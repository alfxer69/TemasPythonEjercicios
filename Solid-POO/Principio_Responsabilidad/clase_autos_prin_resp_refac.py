class Engine:
    
    def getRPM(self):
        return 3000 #valor por defecto

class Vehicle:
    def __init__(self,name,speed,engine):
        self._name=name
        self._speed=speed
        self._engine=engine
    
    def getName(self):
        return self._name
    
    def getEngineRPM(self):
        return self._engine.getRPM()
    
    def getMaxSpeed(self):
        return self._speed
    #no podemos acceder si no es por medio de los getters

class VehiclePrinter:
    def __init__(self,vehicles):
        self._vehicles=vehicles

    def printInfo(self):
        print(f'Vehicle: {self._vehicles.getName()} Max Speed: {self._vehicles.getMaxSpeed()} RPM: {self._vehicles.getEngineRPM()}')
    
    
    
if __name__=='__main__':
    engine=Engine()
    vehicle=Vehicle(name='Car',engine=engine,speed=200)
    printer=VehiclePrinter(vehicles=vehicle)
    printer.printInfo()

    
    
    
    