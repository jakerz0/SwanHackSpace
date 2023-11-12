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
    global isBossLevel
    
    def __init__ (self,roundNumber,player):
        global isBossLevel
        self.roundNumber = roundNumber
        self.player = player
        self.lastTime = time.time()
        if roundNumber == 6:
            isBossLevel = True
        else:
            isBossLevel = False

        

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
            
        if isBossLevel: 
            self.enemyShips.append(Ship(int(enemies[1][1]), int(enemies[1][0]),
                                        False, int(enemies[1][3]), int(enemies[1][2]),
                                        enemies[1][5].strip(), int(enemies[1][4]))
                                    ) # y, x, player?, speed, health, icon, dmg
            
        else:
            for i in range(len(enemies)):
                # print(enemies[i])
                if i == 0: continue # first thing in enemies is dummy notation, ignore
                self.enemyShips.append(Ship(int(enemies[i][1]), int(enemies[i][0]),
                                            False, int(enemies[i][3]), int(enemies[i][2]),
                                            enemies[i][5].strip(), int(enemies[i][4]))
                                        ) # y, x, player?, speed, health, icon, dmg
            
    
    def bossMove(self):
        # for e in self.enemyShips:
        #     if(random.random() * e.speed > 0.9):
        #         if(e.posX > 2):
        #             e.move("a")
        #         else: 
        #             return True #return true that it made it to the other end
        bossShip = self.enemyShips[0]
        if(bossShip.posY < 4):
            bossShip.move('s')
        elif(bossShip.posY > 20):
            bossShip.move('w')
        else:
            if random.random() * 10 < 5:
                bossShip.move('w')
            else:
                bossShip.move('s')

    def fireCannon(self):
        self.attacks.append(self.player.attack())

    def enemiesDefeated(self):
        if(len(self.enemyShips) == 0):
            return True
        else:
            return False

    def enemyFire(self):
        factor = 0.05
        if isBossLevel: factor = 0.25
        for s in self.enemyShips:
            if(random.random() < factor):
                self.attacks.append(s.attack())
    
    def shotMove(self):
        for a in self.attacks:
            if(a.isPlayer == False):
                if(a.posX == 1):
                    self.attacks.remove(a)
                else:
                    didCollide = False
                    for a1 in self.attacks:
                        if(a.posX-1 == a1.posX and a.posY == a1.posY):
                            self.attacks.remove(a)
                            self.attacks.remove(a1)
                            didCollide = True
                    if(didCollide == False):
                        a.move('a')
                        playerHit = a.collideCheck(self.player.posX,self.player.posY)
                        if(playerHit):
                            return True
            else: #for when the player fires
                if(a.posX == 79):
                    self.attacks.remove(a)
                else:
                    didCollide1 = False
                    for a1 in self.attacks:
                        if(a.posX+1 == a1.posX and a.posY == a1.posY):
                            self.attacks.remove(a)
                            self.attacks.remove(a1)
                            didCollide1 = True
                    if(didCollide1 == False):
                        a.move('d')
                        for e in self.enemyShips:
                            if(isBossLevel):
                                if e.posX - 1 == a.posX and (e.posY - 1 == a.posY or e.posY + 1 == a.posY or e.posY == a.posY):
                                    e.health -= 1
                                    if(e.health == 0):
                                        self.enemyShips.remove(e)
                                    self.attacks.remove(a)
                                    self.player.score += e.damage

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
                if(not isBossLevel and self.enemyMove()): #returns true if enemy made it to the other end
                    ret = -1
                elif len(self.enemyShips) > 0 and isBossLevel and self.bossMove():
                    ret = -1
                self.lastTime = time.time()

            
            window.clear()
            window.box()
            printMap(self,window)
            window.refresh()
        self.enemyShips.clear()
        self.attacks.clear()
        return ret
    

def bossprint(bossShip, std):
    #print around the 'M'
    for i in range(-1,2):
        for j in range(-1,2):
            std.addstr(bossShip.posY + i, bossShip.posX + j, bossShip.icon)

def printMap(roundObject,std):
    global isBossLevel
    for s in roundObject.enemyShips:
        std.addstr(s.posY,s.posX,s.icon)
        if isBossLevel:
            bossprint(s,std)
    std.addstr(roundObject.player.posY,roundObject.player.posX,">", curses.color_pair(roundObject.player.colorCode))
    for a in roundObject.attacks:
        std.addstr(a.posY,a.posX,"~")
    std.addstr(0,10, " Health:" + "\u2764" * roundObject.player.health +" ", curses.color_pair(2))
    std.addstr(0,25, " Round: " + str(roundObject.roundNumber) + " ", curses.color_pair(3))
    std.addstr(0,40, " Score: " + str(roundObject.player.score) + " ", curses.color_pair(6))


