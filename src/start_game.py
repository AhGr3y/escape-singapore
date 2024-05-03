import random

from graphics import Window
from maze import Maze
from info_panel import InfoPanel
from character import Character
from bot import Bot
from item import Item

class StartGame():

    def __init__(self):
        win = Window()
        maze = Maze(90, 60, 12, 17, 80, 80, win)
        info = InfoPanel([], win)
        mc = Character(0, 0, maze)
        bot1_1 = Bot(1, random.randint(0, 11), 1, mc, maze)
        bot1_2 = Bot(1, random.randint(0, 11), 2, mc, maze)
        bot1_3 = Bot(1, random.randint(0, 11), 3, mc, maze)
        bot1_4 = Bot(1, random.randint(0, 11), 4, mc, maze)
        bot1_5 = Bot(1, random.randint(0, 11), 5, mc, maze)
        bot1_6 = Bot(1, random.randint(0, 11), 6, mc, maze)
        bot1_7 = Bot(1, random.randint(0, 11), 7, mc, maze)
        bot1_8 = Bot(1, random.randint(0, 11), 8, mc, maze)
        bot1_9 = Bot(1, random.randint(0, 11), 9, mc, maze)
        bot1_10 = Bot(1, random.randint(0, 11), 10, mc, maze)
        bot1_11 = Bot(1, random.randint(0, 11), 11, mc, maze)
        bot1_12 = Bot(1, random.randint(0, 11), 12, mc, maze)
        bot1_13 = Bot(1, random.randint(0, 11), 13, mc, maze)
        bot1_14 = Bot(1, random.randint(0, 11), 14, mc, maze)
        bot1_15 = Bot(1, random.randint(0, 11), 15, mc, maze)
        win._root.mainloop()