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

    stdscr.addstr(8,1,' _____                     _    _ _             ')
    stdscr.addstr(9,1,'/  ___|                   | |  | (_)            ')
    stdscr.addstr(10,1,'\ `--.__      ____ _ _ __ | |  | |_ _ __   __ _ ')
    stdscr.addstr(11,1," `--. \ \ /\ / / _` | '_ \| |/\| | | '_ \ / _` |")
    stdscr.addstr(12,1,"/\__/ /\ V  V / (_| | | | \  /\  / | | | | (_| |")
    stdscr.addstr(13,1,"\____/  \_/\_/ \__,_|_| |_|\/  \/|_|_| |_|\__, |")
    stdscr.addstr(14,1,"                                           __/ |")
    stdscr.addstr(15,1,"                                          |___/ ")
    stdscr.addstr(16,1, " _____  _______   ____   __")
    stdscr.addstr(17,1, "/ __  \|  _  \ \ / /\ \ / /")
    stdscr.addstr(18,1, "`' / /'| |/' |\ V /  \ V / ")
    stdscr.addstr(19,1, "  / /  |  /| |/   \  /   \ ")
    stdscr.addstr(20,1, "./ /___\ |_/ / /^\ \/ /^\ \ ")
    stdscr.addstr(21,1, "\_____/ \___/\/   \/\/   \/")

    s = Ship(1,1)
    a = s.attack()
    stdscr.addstr(7, 7, '' + str(a.dmg) + ' ' + str(a.speed) + ' ' + str(a.posX) + ' ' + str(a.posY))

    stdscr.refresh()
    stdscr.getkey()
    curses.endwin()



if __name__ == '__main__':
    main()
