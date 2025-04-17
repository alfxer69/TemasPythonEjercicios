class Engine:
    def __init__(self):
        pass
    
    def getRPM(self):
        return 300

class Vehicle:
    def __init__(self,name,speed):
        self._name=name 
        self._speed=speed
        self._engine=Engine() #composicion
    
    def getName(self):
        return self._name
    
    def getEngineRPM(self):
        return self._engine.getRPM()
    
    def getMaxSpeed(self):
        return self._speed
    
    def printInfo(self):
        print(f'Vehicle: {self._name} Max Speed: {self._speed} RPM: {self._engine.getRPM()}')

if __name__=='__main__':
    vehicle=Vehicle('Car','200')
    vehicle.printInfo()
    
        