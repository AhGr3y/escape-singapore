from tkinter import *
from tkinter import ttk

class Window:
    
    def __init__(self, width, height):
        # Initialize root window.
        self._root = Tk()
        self._root.title("Escape Singapore")
        # Initialize background color
        self._bg_color = "black"
        # Initialize a canvas
        self._canvas = Canvas(self._root, background=self._bg_color, width=width, height=height)
        self._canvas.grid(column=0, row=0, sticky=NSEW)
        # Configure grid to expand slave when master expands
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_rowconfigure(0, weight=1)
        # Set action after window is closed
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        # Close root window
        self._root.destroy()
        # Inform user that root window is closed.
        print("Application closed.")

    def draw_line(self, line, fill_color="white"):
        line.draw(self._canvas, fill_color)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="white"):
        # Draw line on canvas
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)