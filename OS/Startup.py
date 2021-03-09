import random
import curses
import sys
from curses import textpad
import time
import pyfiglet
from pyfiglet import Figlet

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    h, w = stdscr.getmaxyx()
    text = "WELCOME TO AM OS!"

    time.sleep(2)

    x = w//2 - len(text)//2
    y = h//2

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y, x, text)
    stdscr.attroff(curses.color_pair(1))
    
    stdscr.refresh()
    time.sleep(3)
    import Menu

curses.wrapper(main)
