from ship import Ship
import curses
import time

class Round:
    enemyShips = []
    player = 0
    def __init__ (self,roundNumber):
        self.roundNumber = roundNumber

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


def printMap(roundObject,std):
    for s in roundObject.enemyShips:
        std.addstr(s.posY,s.posX,"<")
    std.addstr(roundObject.player.posY,roundObject.player.posX,">")

def main():
    curses.initscr()
    stdscr = curses.newwin(24, 80)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.box()
    r = Round(1)
    r.generateRound()
    
    printMap(r,stdscr)
    stdscr.refresh()
    while(True):
        printMap(r,stdscr)
        stdscr.refresh()
        userInput = stdscr.getkey()
        if(userInput == curses.KEY_UP):
            stdscr.addstr(2,5,"went up")
            r.player.move('u')
            stdscr.addstr(0,0,str(r.player.posY))
            stdscr.refresh()
        if(userInput == curses.KEY_DOWN):
            r.player.move('d')
            stdscr.addstr(0,0,str(r.player.posX))
        printMap(r,stdscr)
        stdscr.refresh()
        time.sleep(1)
        stdscr.clear()
        stdscr.box()



    curses.endwin()



if __name__ == '__main__':
    main()