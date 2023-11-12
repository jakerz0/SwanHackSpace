from ship import Ship
from shot import Shot
import curses
import time
import random

class Round:
    enemyShips = []
    attacks = []
    player = 0
    lastTime = 0
    currentTime = 0
    def __init__ (self,roundNumber):
        self.roundNumber = roundNumber
        self.lastTime = time.time()

    def generateEnemies(self):
        self.enemyShips.append(Ship(4,77))
        self.enemyShips.append(Ship(6,77))
        self.enemyShips.append(Ship(8,77))
        self.enemyShips.append(Ship(10,77))
        self.enemyShips.append(Ship(12,77))
        self.enemyShips.append(Ship(14,77))
        self.enemyShips.append(Ship(16,77))
        self.enemyShips.append(Ship(18,77))
    
    def generatePlayer(self):
        self.player = Ship(11,2)

    def generateRound(self):
        self.generateEnemies()
        self.generatePlayer()

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





def printMap(roundObject,std):
    for s in roundObject.enemyShips:
        std.addstr(s.posY,s.posX,"<")
    std.addstr(roundObject.player.posY,roundObject.player.posX,">")
    for a in roundObject.attacks:
        std.addstr(a.posY,a.posX,"~")


def main():
    curses.initscr()
    stdscr = curses.newwin(24, 80)
    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    stdscr.box()
    r = Round(1)
    r.generateRound()
    playerHit = False
    printMap(r,stdscr)

    stdscr.refresh()
    while(playerHit == False):
        printMap(r,stdscr)
        stdscr.refresh()
        
        try:
            userInput = stdscr.getkey()
            if(userInput == 'w'):
                r.player.move(userInput)
            if(userInput == 's'):
                r.player.move(userInput)
        except curses.error:
            pass
        stdscr.clear()
        stdscr.box()
        printMap(r,stdscr)
        stdscr.refresh()
        r.currentTime = time.time()
        if((r.currentTime - r.lastTime) > 0.05):
            if(random.random() < 0.5):
                r.enemyFire()
            playerHit = r.enemyShotMove()
            r.lastTime = time.time()

 

    stdscr.addstr(5,5,"play again")
    stdscr.refresh()
    time.sleep(5)
        

    curses.endwin()



if __name__ == '__main__':
    main()