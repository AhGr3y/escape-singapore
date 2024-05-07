import random

from graphics import Window
from maze import Maze
from path import Path
from info_panel import InfoPanel
from character import Character
from bot import Bot
from item import Item

class StartGame():

    def __init__(self):
        num_row = 12
        num_col = 17
        win = Window()
        maze = Maze(90, 60, num_row, num_col, 80, 80, win)
        path = Path(num_col, num_row, maze)
        mc = Character(0, 0, maze)
        key = Item(int(num_row/2), int(num_col/2), "key", mc, maze)
        info = InfoPanel(win, key)
        mc._info = info
        for i in range(1, num_col - 1, 1):
            Bot(1, random.randint(0, 11), i, mc, info, maze)
        win._root.mainloop()