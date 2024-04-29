from tkinter import ttk

class InfoPanel():

    def __init__(self, win=None):
        self.win = win
        self.draw_exit_button()

    def draw_exit_button(self):
        exit = ttk.Button(self.win._root, text='Quit Game', command=self.win.close)
        exit.grid(column=0, row=0)