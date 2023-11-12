import curses
import time
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
    
    def collision(self):
        newwin = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        newwin.addstr(0, 0, "Game Over")
        newwin.refresh()
        time.sleep(5)

    def collideCheck(self, playerX, playerY):
        if(playerX == self.posX and playerY == self.posY):
            self.collision()
            return True
        else:
            return False

    def move(self, dir:str):
        if(dir == 'w'):
            self.posY -= 1 * self.speed
        elif(dir == 's'):
            self.posY += 1 * self.speed
        elif(dir == 'a'):
            self.posX -= 1 * self.speed
        elif(dir == 'd'):
            self.posX += 1 * self.speed

        return (self.posX, self.posY)
