from ship import Ship
from shot import Shot
import curses
import time
import random

class Round:
    enemyShips = []
    player: Ship
    attacks = []
    player = 0
    lastTime = 0
    currentTime = 0
    
    def __init__ (self,roundNumber,player):
        self.roundNumber = roundNumber
        self.player = player
        self.lastTime = time.time()

        

    def generateEnemies(self):
        self.enemyShips.append(Ship(4,77, False))
        self.enemyShips.append(Ship(6,77, False))
        self.enemyShips.append(Ship(8,77, False))
        self.enemyShips.append(Ship(10,77, False))
        self.enemyShips.append(Ship(12,77, False))
        self.enemyShips.append(Ship(14,77, False))
        self.enemyShips.append(Ship(16,77, False))
        self.enemyShips.append(Ship(18,77, False))

    def generateRound(self):
        self.generateEnemies()
        #self.generatePlayer()


    def enemyFire(self):
        for s in self.enemyShips:
            if(random.random() < 0.05):
                self.attacks.append(s.attack())
    
    def enemyShotMove(self):
        for a in self.attacks:
            if(a.posX == 0):
                self.attacks.remove(a)
            else:
                a.move('a')
                playerHit = a.collideCheck(self.player.posX,self.player.posY)
                if(playerHit):
                    return True
        return False
    
    def start(self, window):
        curses.noecho()
        curses.cbreak()
        window.nodelay(True)
        window.keypad(True)
        printMap(self,window)
        window.box()
        window.refresh()
        playerHit = False
        ret = 0
        while(playerHit == False):
            printMap(self,window)
            window.refresh()
            try:
                userInput = window.getkey()
                if(userInput == 'w'):
                    self.player.move(userInput)
                if(userInput == 's'):
                    self.player.move(userInput)
            except curses.error:
                pass
            window.clear()
            window.box()
            printMap(self,window)
            window.refresh()
            self.currentTime = time.time()
            if((self.currentTime - self.lastTime) > 0.05):
                if(random.random() < 0.5):
                    self.enemyFire()
                playerHit = self.enemyShotMove()
                if(playerHit == True):
                    ret = -1
                self.lastTime = time.time()

            window.clear()
            window.box()
            printMap(self,window)
            window.refresh()
        return ret
    



def printMap(roundObject,std):
    for s in roundObject.enemyShips:
        std.addstr(s.posY,s.posX,"<")
    std.addstr(roundObject.player.posY,roundObject.player.posX,">")
    for a in roundObject.attacks:
        std.addstr(a.posY,a.posX,"~")


