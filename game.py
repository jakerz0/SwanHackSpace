import curses
from ship import Ship
from attack import Attack
from startup import startup

def parsescore(f: list):
    ret: str
    name:str = list[0]
    score:str = list[1]
    ret = '' + score + ' -- ' + name
    return ret

def main():

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    # stdscr.border()

    startup(stdscr)

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()




if __name__ == '__main__':
    main()
