import curses
from inbetween import Frame
def main():

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.box()

    stdscr.addstr(0, 0, str(curses.has_colors()))
    stdscr.addstr(2, 4, str(curses.has_extended_color_support()))
    stdscr.addstr(3, 6, '[s] Start Game')
    stdscr.addstr(4, 6, '[h] High Score: ')
    stdscr.addstr(5, 6, '[i] inbetween')

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()




if __name__ == '__main__':
    main()
