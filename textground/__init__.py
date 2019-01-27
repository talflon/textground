import curses

from .typewriter import typewriter_mode

if __name__ == '__main__':
    curses.wrapper(typewriter_mode)
