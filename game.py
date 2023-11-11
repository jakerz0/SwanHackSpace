import curses

def main():

    game_name = "SWAN SPACE DESTROYER"
    start_name = "[s] Start Game"
    high_score_name = "[h] High Score"
    inbetween_name = "[i] inbetween"

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.border()

    stdscr.addstr(1, curses.COLS // 2 - len(game_name) // 2, game_name)
    stdscr.addstr(3, curses.COLS // 2 - len(start_name) // 2, start_name)
    stdscr.addstr(4, curses.COLS // 2 - len(high_score_name) // 2, high_score_name)
    stdscr.addstr(5, curses.COLS // 2 - len(high_score_name) // 2, inbetween_name)

    while(True):
        stdscr.refresh()
        input =stdscr.getkey()

        if(input == 's' or input == 'S'):
            stdscr.addstr(0,0,"started game")
        elif(input == 'h' or input == 'H'):
            stdscr.addstr(0,0,"high score")
        elif(input == 'i' or input == 'I'):
            stdscr.addstr(0,0,"inbetween")
        else:
            stdscr.addstr(0,0,"invalid key")


    curses.endwin()



if __name__ == '__main__':
    main()
