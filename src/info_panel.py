from tkinter import *
from tkinter import ttk

class InfoPanel():

    def __init__(self, win=None, item=None):
        self._win = win
        self._item = item
        self._status = None
        self._msg = None
        self.draw_exit_button()
        self.draw_restart_button()
        self.draw_textbox()

    def draw_exit_button(self):
        exit = ttk.Button(self._win._info_canvas, text='Quit Game', command=self.quit_game, width=30, padding=15)
        exit.place(relx=0.5, rely=0.92, anchor='center')

    def quit_game(self):
        self._win._root.destroy()
        print(f"See you next time!")

    def draw_restart_button(self):
        restart = ttk.Button(self._win._info_canvas, text='Restart Game', command=self.restart_game, width=30, padding=15)
        restart.place(relx=0.5, rely= 0.8, anchor='center')

    def restart_game(self):
        pass

    def draw_textbox(self):
        
        if self._status != "player_escaped":
            if self._status != "player_captured":
                if not self._item._collected:
                    self._status = "items_not_collected"
                if self._item._collected:
                    self._status = "items_collected"

        if self._status == "items_not_collected":
            self._msg = "Use arrow keys to move.\nSteal the key to open up the escape route!\nBecareful not to get caught by the little ruffians!"
        if self._status == "items_collected":
            self._msg = "NO TIME TO HESITATE! TIME TO ESCAPE! SHINZO WO SASAGEYO!"
        if self._status == "player_captured":
            self._msg = "OH NO! You got caught by a little ruffian! Better luck next time!"
        if self._status == "player_escaped":
            self._msg = "Congratulations! You have escaped successfully!"

        t = Text(self._win._info_canvas, width=40, height=10, padx=5, pady=5, bg='black', fg='white', wrap='word')
        t.insert(END, self._msg)
        t.place(relx=0.5, rely=0.1, anchor='center')

        self._win._root.after(100, self.draw_textbox)