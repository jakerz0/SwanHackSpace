import curses
import random
from curses import textpad
#from game import playerShip
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

    def printScreen(self, playerShip):
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
        self.inbetweenBox.addstr(1, 1, str(playerShip.isPlayer))
        self.inbetweenBox.refresh()
    
    def makeSelection(self, playerShip):
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
                    #need some kind of outside logic because cant see ship here
                    return 'heal'
                else:
                    self.healBox.clear()
                    self.printScreen(playerShip)
                    self.makeSelection(playerShip)
            case 's':
                self.shopBox.clear()
                self.shopBox.box()
                self.shopBox.addstr(5, 11, "Enter the shop?")
                self.shopBox.addstr(6, 15, "[Y]/[N]")
                self.shopBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.shopBox.getkey()
                if (choice == 'y'):
                    self.shopEvent()
                    return 'shop'
                else:
                    self.shopBox.clear()
                    self.printScreen(playerShip)
                    self.makeSelection(playerShip)
            case 'u':
                self.upgBox.clear()
                self.upgBox.box()
                self.upgBox.addstr(5, 10, "Upgrade your ship?")
                self.upgBox.addstr(6, 16, "[Y]/[N]")
                self.upgBox.refresh()
                while choice != 'y' and choice != 'n':
                    choice = self.upgBox.getkey()
                if (choice == 'y'):
                    return 'upgrade'
                else:
                    self.upgBox.clear()
                    self.printScreen(playerShip)
                    self.makeSelection(playerShip)
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
                    return 'configure'
                else:
                    self.conBox.clear()
                    self.printScreen(playerShip)
                    self.makeSelection(playerShip)
        self.inbetweenBox.refresh()
        self.inbetweenBox.getch()
        
        
    def shopEvent(self):
        choice = 0
        # Add more Items
        shopItems = {1: '+2 Health',
                     2: '+2 Armor',
                     3: '+1 Max Health',
                     4: '+1 Armor each round',
                     5: 'Rockets (1)',
                     6: 'Dodge Ability (space)',
                     7: 'Blue Ship Skin',
                     8: 'Pink Ship Skin',
                     9: 'Green Ship Skin',
                     10: 'Red Ship Skin'
                     }
        inShop = random.sample(range(1, 10), 6)
        self.inbetweenBox.clear()
        self.inbetweenBox.box()
        item1 = self.inbetweenBox.subwin(10, 26, 1, 1)
        item1.addstr(5, 2, shopItems[inShop[0]])
        item1.addstr(6, 2, '[1]')
        item1.box()
        item2 = self.inbetweenBox.subwin(10, 26, 1, 27)
        item2.addstr(5, 2, shopItems[inShop[1]])
        item2.addstr(6, 2, '[2]')
        item2.box()
        item3 = self.inbetweenBox.subwin(10, 26, 1, 53)
        item3.addstr(5, 2, shopItems[inShop[2]])
        item3.addstr(6, 2, '[3]')
        item3.box()
        item4 = self.inbetweenBox.subwin(10, 26, 11, 1)
        item4.addstr(5, 2, shopItems[inShop[3]])
        item4.addstr(6, 2, '[4]')
        item4.box()
        item5 = self.inbetweenBox.subwin(10, 26, 11, 27)
        item5.addstr(5, 2, shopItems[inShop[4]])
        item5.addstr(6, 2, '[5]')
        item5.box()
        item6 = self.inbetweenBox.subwin(10, 26, 11, 53)
        item6.addstr(5, 2, shopItems[inShop[5]])
        item6.addstr(6, 2, '[6]')
        item6.box()
        self.inbetweenBox.addstr(22, 34, "Leave: [Esc]")
        self.inbetweenBox.refresh()
        while (choice != 49 and choice != 50 and choice != 51 and choice != 52
        and choice != 53 and choice != 54 and choice != 27):
            choice = self.inbetweenBox.getch()
        # match choice:
        #     case 49:
                
            
        self.inbetweenBox.getch()


    
