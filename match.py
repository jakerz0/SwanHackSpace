from rounds import Round
from ship import Ship
from inbetween import Frame
import curses
import time



class Match():

    lost = False
    f: Frame
    player: Ship
    window = 0
    

    def __init__(self, window, player):
        
        self.f = Frame(window)
        self.window = window
        self.player = player


    def run(self):
        self.window.clear()
        while not self.lost:
            r = Round(1, self.player)
            r.generateRound()
            result = r.start(self.window)
            if result == -1:
                self.lost = True
                break
            


            # in between screen
            self.f.printScreen(self.player)
            self.f.makeSelection(self.player)
        
        self.gameOverScreen()
        


    def gameOverScreen(self):
        self.window.nodelay(False)
        self.window.clear()
        self.window.box()
        self.window.addstr(1,1, "Game Over - you lost :(")
        self.window.addstr(3,1, "HIGH SCORE: " + str(-1))
        self.window.addstr(4,1, "YOUR SCORE: " + str(0))
        self.window.refresh()
        self.window.getch()
        self.window.clear()

