from shot import Shot
from attack import Attack

class Ship():
    health: int
    speed: int
    posX: int
    posY: int
    attackprotos:list
    attackIdx:int

    def __init__(self, y, x):
        self.health = 5
        self.speed = 1
        self.posX = x
        self.posY = y
        self.attackIdx = 0
        self.attackprotos = []
        self.attackprotos.append(Attack(1,1)) # basic attack

    def move(self, dir:str):
        if(dir == 'n'):
            self.posY += 1 * self.speed
        elif(dir == 's'):
            self.posY -= 1 * self.speed
        elif(dir == 'w'):
            self.posX -= 1 * self.speed
        elif(dir == 'e'):
            self.posX += 1 * self.speed

        return (self.posX, self.posY)
    
    def attack(self):
        return Shot(self.attackprotos[self.attackIdx], self.posX, self.posY)
    
    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False
        
    def getX(self):
        return self.posX
    
    def getY(self):
        return self.posY
    

        

