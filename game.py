import curses
from ship import Ship
from attack import Attack
from startup import startup
from rounds import Round
from match import Match

def parsescore(f: list):
    ret: str
    name:str = list[0]
    score:str = list[1]
    ret = '' + score + ' -- ' + name
    return ret

def main():
    playerShip = Ship(11, 2, True)
    
    curses.initscr()
    stdscr = curses.newwin(24, 80)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.box()

    while(True):
        choice = startup(stdscr)

        
        match choice:
            case 's':
                m = Match(stdscr, playerShip)
                m.run()
            case 'q':
                break

    stdscr.refresh()
    curses.endwin()




if __name__ == '__main__':
    main()