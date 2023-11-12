from shot import Shot
from attack import Attack
import curses

class Ship():
    health: int
    maxHealth: int
    armor: int
    colorCode: int
    speed: int
    money: int
    barriers: int
    posX: int
    posY: int
    attackprotos:list
    attackIdx:int
    isPlayer: bool
    itemsUnlocked: list

    def __init__(self, y, x, p):
        self.health = 3
        self.maxHealth = 3
        self.armor = 0
        self.colorCode = 0
        self.speed = 1
        self.money = 5
        self.barriers = 1
        self.posX = x
        self.posY = y
        self.attackIdx = 0
        self.attackprotos = []
        self.attackprotos.append(Attack(1,1)) # basic attack
        self.isPlayer = p
        self.itemsUnlocked = []

    def move(self, dir):
        if(dir == 'w'):
            if(self.posY > 1):
                self.posY -= 1 * self.speed
        elif(dir == 's'):
            if(self.posY < 22):
                self.posY += 1 * self.speed
        elif(dir == 'a'):
            if(self.posX > 1):
                self.posX -= 1 * self.speed
        elif(dir == 'd'):
            if(self.posX < 79):
                self.posX += 1 * self.speed

        return (self.posX, self.posY)
    
    def attack(self):
        return Shot(self.attackprotos[self.attackIdx], self.posX, self.posY)
    
    def isDead(self):
        if(self.health <= 0):
            return True
        else:
            return False
        

    

        

