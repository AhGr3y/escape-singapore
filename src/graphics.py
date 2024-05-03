from tkinter import *
from tkinter import ttk

class Window:
    
    def __init__(self, width=800, height=600):
        # create root window
        self._root = Tk()
        self._root.attributes("-fullscreen", 1)
        self._root.title("Escape Singapore")
        # set background color
        self._bg_color = "black"

        # create main frame
        self._main_frame = ttk.Frame(self._root, width=width, height=height)
        self._main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        # make main frame expandable
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_rowconfigure(0, weight=1)
        
        # create content frame
        self._content_frame = ttk.Frame(self._main_frame)
        self._content_frame.grid(column=0, row=0, columnspan=5, sticky=(N, S, E, W))
        # make content frame expandable
        self._main_frame.grid_columnconfigure(0, weight=1)
        self._main_frame.grid_rowconfigure(0, weight=1)

        # create info frame
        self._info_frame = ttk.Frame(self._main_frame)
        self._info_frame.grid(column=5, row=0, sticky=(N, S, E, W))
        # make info frame expandable
        self._main_frame.grid_columnconfigure(1, weight=1)
        
        # create content canvas
        self._content_canvas = Canvas(self._content_frame, background=self._bg_color)
        self._content_canvas.grid(column=0, row=0, sticky=(N, S, E, W))
        # make content canvas expandable
        self._content_frame.grid_columnconfigure(0, weight=1)
        self._content_frame.grid_rowconfigure(0, weight=1)

        # create info canvas
        self._info_canvas = Canvas(self._info_frame, background=self._bg_color)
        self._info_canvas.grid(column=0, row=0, sticky=(N, S, E, W))
        # make info canvas expandable
        self._info_frame.grid_columnconfigure(0, weight=1)
        self._info_frame.grid_rowconfigure(0, weight=1)

        # close root window when user clicks window close button
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        # Close root window
        self._root.destroy()
        # Inform user that root window is closed.
        print("Application closed.")

    def draw_line(self, line, fill_color="white"):
        line.draw(self._content_canvas, fill_color)

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