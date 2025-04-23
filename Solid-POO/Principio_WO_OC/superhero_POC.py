from abc import ABC,abstractmethod

class attackManager(ABC):
    
    @abstractmethod
    def attack(self,superhero):
        pass

class PunchAttack(attackManager):
    def attack(self, superhero):
        return f'{superhero.name} attack with a powerful punch'

class LaserAttack(attackManager):
    def attack(self, superhero):
        return f'{superhero.name} attack with a laser beam'

class RegularAttack(attackManager):
    def attack(self, superhero):
        return f'{superhero.name} attack with a Regular Attack'

class Superhero():
    def __init__ (self,name,health,attackManager)->None:
        self.name=name
        self.health=health
        self.attackManager=attackManager
    
    def attack(self):
        return self.attackManager.attack(self)

class Game:
    def __init__(self)->None:
        self.superheroes=[]
    
    def add_superhero(self,superhero):
        self.superheroes.append(superhero)
        
    def superhero_action(self):
        for superhero in self.superheroes:
            print(superhero.attack())

game=Game()
superhero1=Superhero('Superman',100,PunchAttack())
superhero2=Superhero('Cyclops',80,LaserAttack())
game.add_superhero(superhero1)
game.add_superhero(superhero2)
game.superhero_action()