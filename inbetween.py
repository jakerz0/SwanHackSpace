import curses
from curses import textpad
class Frame:
    screen = 0
    def __init__(self, stdscr):    
        curses.curs_set(0)
        self.screen = stdscr

    def printScreen(self):
        self.screen.border(0)
        maxY, maxX = self.screen.getmaxyx()
        box1 = curses.newwin(maxY, maxX)
        box1.box(0, 0)
        box1.addstr(1, 1, "Hello")
        box1.refresh()
        box1.getch()

    
