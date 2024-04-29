from tkinter import PhotoImage

from math import floor

class Character():

    def __init__(self, maze=None, character="default"):
        self._character = character
        self.char_img = ""
        self._maze = maze
        self._row = 0
        self._col = 0
        self._bot1 = None
        self._bot1_img = ""
        self._bot1_row = 0
        self._bot1_col = floor(self._maze._num_cols/2)
        self._bot1_move_direction = "down"
        self._isRunning = False
        self.draw_main_character()
        self.create_bot()
        self.move_bot1()

    def draw_main_character(self):

        if self._maze is None:
            raise ValueError("Maze is not defined!")
        
        # default spawn location
        default_x = self._maze._x1 + self._maze._cell_width/2
        default_y = self._maze._y1 + self._maze._cell_height/2

        # draw default character
        if self._character == "default":
            global char
            try:
                self.char_img = PhotoImage(file="./assets/images/default-boy.png")
            except Exception as e:
                print("Error loading character image:", e)
                return
            char = self._maze.win._canvas.create_image(default_x, default_y, image=self.char_img)
            self.enable_movement()

    def create_bot(self, level=1):

        if level == 1:
            
            # default spawn location
            default_x = self._maze._x1 + (floor(self._maze._num_cols/2) * self._maze._cell_width) + self._maze._cell_width/2
            default_y = self._maze._y1 + self._maze._cell_height/2

            self._bot1_img = PhotoImage(file="./assets/images/bad-boy.png")
            self._bot1 = self._maze.win._canvas.create_image(default_x, default_y, image=self._bot1_img)

    def move_bot1(self):
        
        if self._bot1 is not None:

            # Change direction when reach the edge
            if self._bot1_row == self._maze._num_rows - 1:
                self._bot1_move_direction = "up"
            if self._bot1_row == 0:
                self._bot1_move_direction = "down"

            # Move bot down
            if self._bot1_move_direction == "down":
                self._maze.win._canvas.move(self._bot1, 0, self._maze._cell_height)
                self._bot1_row += 1

            # Move bot up
            if self._bot1_move_direction == "up":
                self._maze.win._canvas.move(self._bot1, 0, -self._maze._cell_height)
                self._bot1_row -= 1

            self._maze.win._root.after(500, self.move_bot1)


    def enable_movement(self):
        # Enable movement via arrow keys
        self._maze.win._root.bind("<Right>", self.move_right)
        self._maze.win._root.bind("<Left>", self.move_left)
        self._maze.win._root.bind("<Up>", self.move_up)
        self._maze.win._root.bind("<Down>", self.move_down)

        # Enable movement via wasd keys
        self._maze.win._root.bind("<KeyPress-d>", self.move_right)
        self._maze.win._root.bind("<KeyPress-a>", self.move_left)
        self._maze.win._root.bind("<KeyPress-w>", self.move_up)
        self._maze.win._root.bind("<KeyPress-s>", self.move_down)

    def move_right(self, event):
        # Stop character from exiting edge of maze
        if self._col == self._maze._num_cols - 1:
            return
        
        # Stop character from passing thru wall
        cell_to_right = self._maze._cells[self._col + 1][self._row]
        if cell_to_right.has_left_wall:
            return

        # Move character to the right
        global char
        self._maze.win._root.after(1, self._maze.win._canvas.move(char, self._maze._cell_width, 0))
        self._col += 1

        #End game if character hit bot
        if self._col == self._bot1_col and self._row == self._bot1_row:
            self._maze.win.close()
    
    def move_left(self, event):
        # Stop character from exiting edge of maze
        if self._col == 0:
            return
        
        # Stop character from passing thru wall
        cell_to_left = self._maze._cells[self._col - 1][self._row]
        if cell_to_left.has_right_wall:
            return
        
        # Move character to the left
        global char
        self._maze.win._root.after(1, self._maze.win._canvas.move(char, -self._maze._cell_width, 0))
        self._col -= 1

        #End game if character hit bot
        if self._col == self._bot1_col and self._row == self._bot1_row:
            self._maze.win.close()

    def move_up(self, event):
        # Stop character from exiting edge of maze
        if self._row == 0:
            return
        
        # Stop character from passing thru wall
        cell_to_top = self._maze._cells[self._col][self._row - 1]
        if cell_to_top.has_bottom_wall:
            return
        
        # Move character to the top
        global char
        self._maze.win._root.after(1, self._maze.win._canvas.move(char, 0, -self._maze._cell_height))
        self._row -= 1

        #End game if character hit bot
        if self._col == self._bot1_col and self._row == self._bot1_row:
            self._maze.win.close()

    def move_down(self, event):
        # Stop character from exiting edge of maze
        if self._row == self._maze._num_rows - 1:
            return
        
        # Stop character from passing thru wall
        cell_to_bottom = self._maze._cells[self._col][self._row + 1]
        if cell_to_bottom.has_top_wall:
            return
        
        # Move character to the bottom
        global char
        self._maze.win._root.after(1, self._maze.win._canvas.move(char, 0, self._maze._cell_height))
        self._row += 1

        #End game if character hit bot
        if self._col == self._bot1_col and self._row == self._bot1_row:
            self._maze.win.close()