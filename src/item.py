from tkinter import PhotoImage

class Item():

    def __init__(self, row, col, name, player, maze=None):
        self._maze = maze
        self._row = row
        self._col = col
        self._x = None
        self._y = None
        self._name = name
        self._player = player
        self._body = None
        self._img = None
        self._collected = False
        self.set_default_position()
        self.draw()

    def set_default_position(self):

        if self._maze is None:
            raise ValueError("Maze not defined.")
        
        if self._col > self._maze._num_cols or self._row > self._maze._num_rows:
            raise ValueError("Cannot draw item outside of maze.")

        self._x = self._maze._x1 + self._maze._cell_width/2 + (self._col * self._maze._cell_width)
        self._y = self._maze._y1 + self._maze._cell_height/2 + (self._row * self._maze._cell_height)

    def draw(self):

        if not self._collected:

            # player collects item
            if self._row == self._player._row and self._col == self._player._col:
                self._collected = True

            if self._name == "passport":
                try:
                    self._img = PhotoImage(file="./assets/images/passport.png")
                except Exception as e:
                    print("Error loading character image:", e)
                    return
                
        if self._collected:
            self._img = None
            
        self._body = self._maze.win._main_canvas.create_image(self._x, self._y, image=self._img)

        self._maze.win._root.after(100, self.draw)