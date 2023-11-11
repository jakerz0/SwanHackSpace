import curses

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

    

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()



if __name__ == '__main__':
    main()
