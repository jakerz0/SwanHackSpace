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
        #self.generateEnemies()
        #self.generatePlayer()
        fname = './levels/level' + str(self.roundNumber) + '.txt'
        src = open(fname, 'r')
        tmp = src.readlines()
        enemies = []
        for e in tmp:
            enemies.append(e.split(' '))
            
        
        for i in range(len(enemies)):
            print(enemies[i])
            if i == 0: continue # first thing in enemies is dummy notation, ignore
            self.enemyShips.append(Ship(int(enemies[i][1]), int(enemies[i][0]),
                                        False, int(enemies[i][3]), int(enemies[i][2]),
                                        enemies[i][5].strip(), int(enemies[i][4]))
                                    ) # y, x, player?, speed, health, icon, dmg
            
        

    def fireCannon(self):
        self.attacks.append(self.player.attack())

    def enemiesDefeated(self):
        if(len(self.enemyShips) == 0):
            return True
        else:
            return False

    def enemyFire(self):
        for s in self.enemyShips:
            if(random.random() < 0.05):
                self.attacks.append(s.attack())
    
    def shotMove(self):
        for a in self.attacks:
            if(a.isPlayer == False):
                if(a.posX == 1):
                    self.attacks.remove(a)
                else:
                    a.move('a')
                    playerHit = a.collideCheck(self.player.posX,self.player.posY)
                    if(playerHit):
                        return True
            else: #for when the player fires
                if(a.posX == 79):
                    self.attacks.remove(a)
                else:
                    a.move('d')
                    for e in self.enemyShips:
                        if(e.posX == a.posX and e.posY == a.posY): #if it hits, remove the ship and attack from respective arrays
                            e.health -= 1
                            if(e.health == 0):
                                self.enemyShips.remove(e)
                            self.attacks.remove(a)
                            self.player.score += 1
        return False
    
    def enemyMove(self):
        for e in self.enemyShips:
            if(random.random() * e.speed > 0.9):
                if(e.posX > 2):
                    e.move("a")
                else: 
                    return True #return true that it made it to the other end
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
        while(ret == 0):
            printMap(self,window)
            window.refresh()
            try:
                userInput = window.getkey()
                if(userInput == 'w'):
                    self.player.move(userInput)
                if(userInput == 's'):
                    self.player.move(userInput)
                if(userInput == ' '):
                    self.fireCannon()
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
                playerHit = self.shotMove()
                if(playerHit == True):
                    self.player.health -= 1
                    if(self.player.health == 0):
                        ret = -1
                if(self.enemiesDefeated()):
                    ret = 1
                if(self.enemyMove()): #returns true if enemy made it to the other end
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
    std.addstr(0,10, " Health: " + str(roundObject.player.health) +" ")
    std.addstr(0,25, " Round: " + str(roundObject.roundNumber) + " ")
    std.addstr(0,40, " Score: " + str(roundObject.player.score) + " ")


