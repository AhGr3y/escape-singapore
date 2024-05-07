from tkinter import PhotoImage

class Path():

    def __init__(self, col, row, maze=None):
        self._col = col
        self._row = row
        self._img = None
        self._body = None
        self._maze = maze
        self.draw_escape()

    def draw_escape(self):

        if self._maze is None:
            raise ValueError("Maze is not defined!")

        exit_cell = self._maze._cells[self._maze._num_cols - 1][self._maze._num_rows - 1]
        x = exit_cell._p1.x + self._maze._cell_width/2
        y = exit_cell._p1.y + self._maze._cell_height/2

        try:
            self._img = PhotoImage(file="./assets/images/exit.png")
        except Exception as e:
            print("Error loading escape image:", e)
            return
        self._body = self._maze._win._content_canvas.create_image(x, y, image=self._img)