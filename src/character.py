from tkinter import PhotoImage

class Character():

    def __init__(self, row, col, maze=None, character="default"):
        self._character = character
        self._img = None
        self._maze = maze
        self._info = None
        self._row = row
        self._col = col
        self.draw_main_character()

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
                self._img = PhotoImage(file="./assets/images/player.png")
            except Exception as e:
                print("Error loading character image:", e)
                return
            char = self._maze._win._content_canvas.create_image(default_x, default_y, image=self._img)
            self.enable_movement()

    def kill_character(self):
        self._img = None

    def catch_character(self):
        pass

    def enable_movement(self):
        # Enable movement via arrow keys
        self._maze._win._root.bind("<Right>", self.move_right)
        self._maze._win._root.bind("<Left>", self.move_left)
        self._maze._win._root.bind("<Up>", self.move_up)
        self._maze._win._root.bind("<Down>", self.move_down)

        # Enable movement via wasd keys
        self._maze._win._root.bind("<KeyPress-d>", self.move_right)
        self._maze._win._root.bind("<KeyPress-a>", self.move_left)
        self._maze._win._root.bind("<KeyPress-w>", self.move_up)
        self._maze._win._root.bind("<KeyPress-s>", self.move_down)

    def move_right(self, event):
        # Stop character from exiting edge of maze
        if self._col == self._maze._num_cols - 1:
            return
        
        # Stop character from passing thru wall
        cell_to_right = self._maze._cells[self._col + 1][self._row]
        if cell_to_right._has_left_wall:
            return

        # Move character to the right
        global char
        self._maze._win._root.after(1, self._maze._win._content_canvas.move(char, self._maze._cell_width, 0))
        self._col += 1

        # End game when character reaches the end
        if self._col == self._maze._num_cols - 1 and self._row == self._maze._num_rows - 1:
            self.escaped()
    
    def move_left(self, event):
        # Stop character from exiting edge of maze
        if self._col == 0:
            return
        
        # Stop character from passing thru wall
        cell_to_left = self._maze._cells[self._col - 1][self._row]
        if cell_to_left._has_right_wall:
            return
        
        # Move character to the left
        global char
        self._maze._win._root.after(1, self._maze._win._content_canvas.move(char, -self._maze._cell_width, 0))
        self._col -= 1

        # End game when character reaches the end
        if self._col == self._maze._num_cols - 1 and self._row == self._maze._num_rows - 1:
            self.escaped()

    def move_up(self, event):
        # Stop character from exiting edge of maze
        if self._row == 0:
            return
        
        # Stop character from passing thru wall
        cell_to_top = self._maze._cells[self._col][self._row - 1]
        if cell_to_top._has_bottom_wall:
            return
        
        # Move character to the top
        global char
        self._maze._win._root.after(1, self._maze._win._content_canvas.move(char, 0, -self._maze._cell_height))
        self._row -= 1

        # End game when character reaches the end
        if self._col == self._maze._num_cols - 1 and self._row == self._maze._num_rows - 1:
            self.escaped()

    def move_down(self, event):
        # Stop character from exiting edge of maze
        if self._row == self._maze._num_rows - 1:
            return
        
        # Stop character from passing thru wall
        cell_to_bottom = self._maze._cells[self._col][self._row + 1]
        if cell_to_bottom._has_top_wall:
            return
        
        # Move character to the bottom
        global char
        self._maze._win._root.after(1, self._maze._win._content_canvas.move(char, 0, self._maze._cell_height))
        self._row += 1

        # End game when character reaches the end
        if self._col == self._maze._num_cols - 1 and self._row == self._maze._num_rows - 1:
            self.escaped()

    def escaped(self):
        self._img = None
        if self._info is not None:
            self._info._status = "player_escaped"

    def restart_game(self):
        self._row = 0
        self._col = 0
        self.draw_main_character()