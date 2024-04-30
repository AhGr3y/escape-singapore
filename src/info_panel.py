from tkinter import ttk

class InfoPanel():

    def __init__(self, item_list, win=None):
        self._win = win
        self._item_list = item_list

    def draw_exit_button(self):
        exit = ttk.Button(self.win._root, text='Quit Game', command=self.win.close)
        exit.grid(column=0, row=0)