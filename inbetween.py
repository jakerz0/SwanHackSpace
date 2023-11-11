import curses
from curses import textpad
class Frame:
    screen = 0
    inbetweenBox = 0
    healBox = 0
    shopBox = 0
    upgBox = 0
    conBox = 0
    def __init__(self, stdscr):    
        curses.curs_set(0)
        maxY, maxX = stdscr.getmaxyx()
        self.screen = stdscr
        self.inbetweenBox = curses.newwin(maxY, maxX)

    def printScreen(self):
        self.screen.border(0)
        self.inbetweenBox.box()
        self.healBox = self.inbetweenBox.subwin(11, 39, 1, 1)
        self.healBox.box()
        self.healBox.addstr(5, 17, "Heal")
        self.healBox.addstr(6, 17, "[H]")
        self.shopBox = self.inbetweenBox.subwin(11, 39, 12, 1)
        self.shopBox.box()
        self.shopBox.addstr(5, 17, "Shop")
        self.shopBox.addstr(6, 17, "[S]")
        self.upgBox = self.inbetweenBox.subwin(11, 39, 1, 40)
        self.upgBox.box()
        self.upgBox.addstr(5, 17, "Upgrade")
        self.upgBox.addstr(6, 19, "[U]")
        self.conBox = self.inbetweenBox.subwin(11, 39, 12, 40)
        self.conBox.box()
        self.conBox.addstr(5, 16, "Configure")
        self.conBox.addstr(6, 19, "[C]")
        self.inbetweenBox.refresh()
    
    def makeSelection(self):
        choice = ''
        while choice != 'h' and choice != 's' and choice != 'u' and choice != 'c':
            choice = self.inbetweenBox.getkey()
            choice = choice.lower()
        match choice:
            case 'h':
                self.healBox.clear()
                self.healBox.box()
                self.healBox.addstr(5, 10, "Heal to full health?")
                self.healBox.addstr(6, 17, "[Y]/[N]")
                self.healBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.healBox.getkey()
                if (choice == 'y'):
                    # do something
                    print("todo")
                else:
                    self.healBox.clear()
                    self.printScreen()
                    self.makeSelection()
            case 's':
                self.shopBox.clear()
                self.shopBox.box()
                self.shopBox.addstr(5, 11, "Enter the shop?")
                self.shopBox.addstr(6, 15, "[Y]/[N]")
                self.shopBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.shopBox.getkey()
                if (choice == 'y'):
                    # do something
                    print("todo")
                else:
                    self.shopBox.clear()
                    self.printScreen()
                    self.makeSelection()
            case 'u':
                self.upgBox.clear()
                self.upgBox.box()
                self.upgBox.addstr(5, 10, "Upgrade your ship?")
                self.upgBox.addstr(6, 16, "[Y]/[N]")
                self.upgBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.upgBox.getkey()
                if (choice == 'y'):
                    # do something
                    print("todo")
                else:
                    self.upgBox.clear()
                    self.printScreen()
                    self.makeSelection()
            case 'c':
                self.conBox.clear()
                self.conBox.box()
                self.conBox.addstr(5, 10, "Configure your ship?")
                self.conBox.addstr(6, 13, "(Free action)")
                self.conBox.addstr(7, 16, "[Y]/[N]")
                self.conBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.conBox.getkey()
                if (choice == 'y'):
                    # do something
                    print("todo")
                else:
                    self.conBox.clear()
                    self.printScreen()
                    self.makeSelection()
        self.inbetweenBox.refresh()
        self.inbetweenBox.getch()
        
        
        


    
