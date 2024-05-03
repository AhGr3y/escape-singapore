from tkinter import N, S, E, W
from tkinter import ttk

class InfoPanel():

    def __init__(self, item_list, win=None):
        self._win = win
        self._item_list = item_list
        self.draw_exit_button(0, 0)

    def draw_exit_button(self, col, row):
        exit = ttk.Button(self._win._info_canvas, text='Quit Game', command=self.quit_game, width=40)
        exit.grid(column=col, row=row, stick=(N, S, E, W))

    def quit_game(self):
        self._win._root.destroy()
        print(f"See you next time!")