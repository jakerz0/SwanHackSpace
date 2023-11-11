
class Shot():
    dmg:int
    posX:int
    posY:int
    speed:int

    def __init__(self, attack, x, y):
        self.dmg = attack.dmg
        self.speed = attack.spd
        self.posX = x
        self.posY = y
    
    def collide(self, target):
        target.health -= self.dmg

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
