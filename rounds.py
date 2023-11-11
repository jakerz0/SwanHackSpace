from ship import Ship
import curses

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



def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.border()
    r = Round(1)
    r.generateRound()
    for s in r.enemyShips:
        stdscr.addstr(s.posX,s.posY,"<")

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()



if __name__ == '__main__':
    main()