from tkinter import *
from tkinter import ttk

class InfoPanel():

    def __init__(self, win=None, item=None):
        self._win = win
        self._item = item
        self.draw_exit_button()
        self.draw_textbox()

    def draw_exit_button(self):
        exit = ttk.Button(self._win._info_canvas, text='Quit Game', command=self.quit_game, width=30, padding=15)
        exit.place(relx=0.5, rely=0.92, anchor='center')

    def quit_game(self):
        self._win._root.destroy()
        print(f"See you next time!")

    def draw_textbox(self):
        global msg

        if not self._item._collected:
            msg = "Use arrow keys to move.\nSteal the key to open up the escape route!\nBecareful not to get caught by the little ruffians!"
        else:
            msg = "NO TIME TO HESITATE! TIME TO ESCAPE! SHINZO WO SASAGEYO!"
        t = Text(self._win._info_canvas, width=40, height=10, padx=5, pady=5, bg='black', fg='white', wrap='word')
        t.insert(END, msg)
        t.place(relx=0.5, rely=0.1, anchor='center')

        self._win._root.after(100, self.draw_textbox)