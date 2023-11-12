import curses
from ship import Ship
from attack import Attack
from startup import startup
from inbetween import Frame
from rounds import Round

def parsescore(f: list):
    ret: str
    name:str = list[0]
    score:str = list[1]
    ret = '' + score + ' -- ' + name
    return ret

def main():

    curses.initscr()
    stdscr = curses.newwin(24, 80)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.box()

    choice = startup(stdscr)

    
    match choice:
        case 'i':
            f = Frame(stdscr)
            f.printScreen()
            f.makeSelection()
        case 's':
            Round()

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()




if __name__ == '__main__':
    main()