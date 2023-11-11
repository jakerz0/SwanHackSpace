import curses
from ship import Ship
from attack import Attack

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
    stdscr.border()

    score = open('highscore.txt', 'r')
    highscore = score.readlines()

    # stdscr.addstr(0, 0, str(curses.has_colors()))
    # stdscr.addstr(2, 4, str(curses.has_extended_color_support()))
    stdscr.addstr(3, 6, '[s] Start Game')
    stdscr.addstr(4, 6, '[h] High Score: ' + highscore[1].strip() + ' -- ' + highscore[0].strip())
    stdscr.addstr(5, 6, '[i] inbetween')

    s = Ship(1,1)
    a = s.attack()
    stdscr.addstr(7, 7, '' + str(a.dmg) + ' ' + str(a.speed) + ' ' + str(a.posX) + ' ' + str(a.posY))

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()



if __name__ == '__main__':
    main()
