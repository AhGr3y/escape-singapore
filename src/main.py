from graphics import Window
from maze import Maze
from character import Character

win = Window(1500, 900)
maze = Maze(50, 50, 10, 14, 80, 80, win, 10)
char = Character(maze)
win._root.mainloop()
