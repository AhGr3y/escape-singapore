from graphics import Window
from maze import Maze
from character import Character
from bot import Bot

win = Window(1500, 900)
maze = Maze(50, 50, 10, 14, 80, 80, win)
char = Character(0, 0, maze)
bot1_1 = Bot(1, 0, 3, char, maze)
bot1_2 = Bot(1, 2, 6, char, maze)
bot1_3 = Bot(1, 4, 9, char, maze)
bot1_4 = Bot(1, 6, 12, char, maze)
win._root.mainloop()