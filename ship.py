import shot
import attack

class Ship():
    health: int
    speed: int
    posX: int
    posY: int
    attackprotos:list
    attackIdx:int

    def __init__(self, x, y ):
        self.health = 5
        self.speed = 1
        self.posX = x
        self.posY = y
        self.attackIdx = 0
        self.attackprotos.add(attack(1,1))

    def move(self, dir:str):
        if(dir == 'u'):
            self.posY += 1 * self.speed
        elif(dir == 's'):
            self.posY -= 1 * self.speed
        elif(dir == 'w'):
            self.posX -= 1 * self.speed
        elif(dir == 'e'):
            self.posX += 1 * self.speed

        return (self.posX, self.posY)
    
    def attack(self):
        return shot(self.attack[self.attackIdx])
    

        

