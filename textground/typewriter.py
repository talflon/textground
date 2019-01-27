import curses


def typewriter_mode(stdscr):
    stdscr.clear()
    stdscr.move(0, 0)
    curses.curs_set(2)  # very visible cursor
    while True:
        ch = stdscr.getch()
        if 0x20 <= ch <= 0x7E:  # printable ASCII characters
            stdscr.addch(ch)
        elif ch == curses.KEY_LEFT:
            y, x = stdscr.getyx()
            stdscr.move(y, max(x - 1, 0))
        elif ch == curses.KEY_RIGHT:
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move(y, min(x + 1, maxx - 1))
        elif ch == curses.KEY_UP:
            y, x = stdscr.getyx()
            stdscr.move(max(y - 1, 0), x)
        elif ch == curses.KEY_DOWN:
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move(min(y + 1, maxy - 1), x)
        elif ch == ord('\n'):
            y, x = stdscr.getyx()
            maxy, maxx = stdscr.getmaxyx()
            stdscr.move(min(y + 1, maxy - 1), 0)
