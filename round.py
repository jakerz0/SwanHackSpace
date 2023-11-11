import curses

class Round:
    x = 0
    y = 0
    map = []
    def __init__(self,roundNumber):

        self.roundNumber = roundNumber
        self.x = 3
        self.y = 11 
        temp = []
        for j in range(24):
            for i in range(80):
                temp.append('')
            self.map.append(temp)

    def generateRound(self):
        self.map[2][78] = '<'

    def printMap(self):
        stdscr = curses.initscr()
        for j in range(24):
            for i in range(80):
                if(self.map[j][i] == '<'):
                    print(self.map[j][i])


    def playInput(self,input):
        match input:
            case curses.KEY_UP:
                if(self.y > 1):
                    self.y -= 1
            case curses.KEY_DOWN:
                if(self.y < 79):
                    self.x += 1


    def playRound(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.border()
        while(True):
            stdscr.refresh()
            input =stdscr.getkey()






def main():
    r = Round(1)
    r.generateRound()
    print(r.map)


if __name__ == '__main__':
    main()