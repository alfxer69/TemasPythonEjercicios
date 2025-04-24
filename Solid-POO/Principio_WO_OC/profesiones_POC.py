from abc import ABC,abstractmethod

class actionManager(ABC):
    
    @abstractmethod
    def action(self,profesional):
        pass

class industrialengineer(actionManager):
    def action(self, profesional):
        return f'{profesional.name} Working in a factory'

class teacher(actionManager):
    def action(self, profesional):
        return f'{profesional.name} working in a school'

class salesmanager(actionManager):
    def action(self, profesional):
        return f'{profesional.name} working in the office'

class driver(actionManager):
    def action(self, profesional):
        return f'{profesional.name} working in a bus'

class accountant(actionManager):
    def action(self, profesional):
        return f'{profesional.name} working in the office'

class soldier(actionManager):
    def action(self, profesional):
        return f'{profesional.name} working in the Army'

class Profesional:
    def __init__(self,name,sueldo_prom,actionManager):
        self.name=name
        self.sueldo_prom=sueldo_prom
        self.action_manager=actionManager 

    def action(self):
        return self.action_manager.action(self)    
    
class Trabajo:
    def __init__(self)->None:
        self.profesionales=[]
    
    def add_profesional(self,profesional):
        self.profesionales.append(profesional)
    
    def profesional_action(self):
        for profesional in self.profesionales:
            print(profesional.action())

trabajo=Trabajo()
profesional1=Profesional('Ingeniero Industrial',2500,industrialengineer())
profesional2=Profesional('Soldier',3000,soldier())
profesional3=Profesional('driver',1500,driver())
trabajo1=Trabajo()
trabajo1.add_profesional(profesional1)
trabajo1.add_profesional(profesional2)
trabajo1.add_profesional(profesional3)
trabajo1.profesional_action()