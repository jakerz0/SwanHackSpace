import curses
def startup(window):

    score = open('highscore.txt', 'r')
    highscore = score.readlines()

    # window.addstr(0, 0, str(curses.has_colors()))
    # window.addstr(2, 4, str(curses.has_extended_color_support()))
    
    window.addstr(3, 6, '[g] Start Game')
    window.addstr(4, 6, '[h] High Score: ' + highscore[1].strip() + ' -- ' + highscore[0].strip())
    window.addstr(5, 6, '[q] Quit')

    window.addstr(8,1,' _____                     _    _ _             ')
    window.addstr(9,1,'/  ___|                   | |  | (_)            ')
    window.addstr(10,1,'\ `--.__      ____ _ _ __ | |  | |_ _ __   __ _ ')
    window.addstr(11,1," `--. \ \ /\ / / _` | '_ \| |/\| | | '_ \ / _` |")
    window.addstr(12,1,"/\__/ /\ V  V / (_| | | | \  /\  / | | | | (_| |")
    window.addstr(13,1,"\____/  \_/\_/ \__,_|_| |_|\/  \/|_|_| |_|\__, |")
    window.addstr(14,1,"                                           __/ |")
    window.addstr(15,1,"                                          |___/ ")
    window.addstr(16,1, " _____  _______   ____   __")
    window.addstr(17,1, "/ __  \|  _  \ \ / /\ \ / /")
    window.addstr(18,1, "`' / /'| |/' |\ V /  \ V / ")
    window.addstr(19,1, "  / /  |  /| |/   \  /   \ ")
    window.addstr(20,1, "./ /___\ |_/ / /^\ \/ /^\ \ ")
    window.addstr(21,1, "\_____/ \___/\/   \/\/   \/")

    ret = 0
    while(True):
        try:
            ret = window.getkey()      
            if(ret == 'q' or ret == 'h' or ret == 'g'):
                break
        except curses.error:
            pass
    return ret