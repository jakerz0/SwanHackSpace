import curses

def main():

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.border()

    stdscr.addstr(0, 0, str(curses.has_colors()))
    stdscr.addstr(2, 4, str(curses.has_extended_color_support()))
    stdscr.addstr(3, 6, 'piece of text')

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()



if __name__ == '__main__':
    main()
