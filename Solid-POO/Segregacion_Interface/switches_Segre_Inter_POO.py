from abc import ABC,abstractmethod

class ISwitchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class ITemperatureRegulable(ABC):
    @abstractmethod
    def set_temperature(self, temperature):
        pass

class SmartLight(ISwitchable):
    def turn_on(self):
        print("Smart light is turned on.")

    def turn_off(self):
        print("Smart light is turned off.")

class SmartThermostat(ISwitchable, ITemperatureRegulable):
    def turn_on(self):
        print("Smart thermostat is turned on.")

    def turn_off(self):
        print("Smart thermostat is turned off.")

    def set_temperature(self, temperature):
        print(f"Temperature set to {temperature} degrees.")
        
smartligtht = SmartLight()
smartligtht.turn_on()
smartligtht.turn_off()

smartshermostat= SmartThermostat()
smartshermostat.turn_on()
smartshermostat.turn_off()
smartshermostat.set_temperature(22)


    

    
