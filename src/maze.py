import random

from graphics import (
    Window,
    Point,
)

from cell import Cell

class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self.win = win
        self._cells = []

    def _draw_cells(self, fill_color="white"):

        # Raise error if root window is not set.
        if self.win is None:
            raise ValueError("Root window is not set.")

        # Loop through cols
        for i in range(self._num_cols):
            # Get x-coordinates of cell
            x1 = self._x1 + self._cell_width * i
            x2 = x1 + self._cell_width
            # Create variable to hold row of cells for each column
            col = []
            
            # Loop through rows
            for j in range(self._num_rows):
                # Get y-coordinates of cell
                y1 = self._y1 + self._cell_height * j
                y2 = y1 + self._cell_height
                # Get cell
                cell = Cell(Point(x1, y1), Point(x2, y2), self.win)
                # Add cell to col
                col.append(cell)
                # Draw cell
                cell.draw(fill_color)
            # Exit looping thru rows

            # Add filled up col to cells
            self._cells.append(col)
        # Exit looping thru cols
        
    def _break_entrance_and_exit(self):

        # Get entrance cell
        entrance_cell = self._cells[0][0]
        # Break left wall of entrance
        entrance_cell.has_left_wall = False
        # Redraw entrance cell
        entrance_cell.draw()

        # Get exit cell
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        # Break right wall of exit
        exit_cell.has_right_wall = False
        # Redraw exit cell
        exit_cell.draw()

    def _break_walls(self):
        
        # Get list of randomized walls
        walls = self._get_walls()
        random.shuffle(walls)
        
        # Create a nested list of CellDisjointSet
        cds_list = []
        for i in range(self._num_cols):
            cols = []
            for j in range(self._num_rows):
                cds = CellDisjointSet(i, j)
                cols.append(cds)
            cds_list.append(cols)

        # for each wall, if cells separated by wall dont have the same parent, join them
        while(len(walls) > 0):
            
            # get random wall
            wall = walls.pop()
            # get matrix of current wall
            i = wall.i
            j = wall.j
            if wall.direction == 'r': # wall is a right wall of a cell
                # get cds of left and right cell
                left_cds = cds_list[i][j]
                right_cds = cds_list[i + 1][j]
                # get parent of both cells
                left_parent = left_cds.find(left_cds)
                right_parent = right_cds.find(right_cds)
                # if parents are not the same, the merge them
                if left_parent != right_parent:
                    left_cds.union(right_cds)
                    # break wall and redraw both cells
                    left_cell = self._cells[i][j]
                    left_cell.has_right_wall = False
                    left_cell.draw()
                    right_cell = self._cells[i + 1][j]
                    right_cell.has_left_wall = False
                    right_cell.draw()

            if wall.direction == 'b': # wall is a bottom wall of a cell
                # get cds of top and bottom cell
                top_cds = cds_list[i][j]
                bottom_cds = cds_list[i][j + 1]
                # get parent of both cells
                top_parent = top_cds.find(top_cds)
                bottom_parent = bottom_cds.find(bottom_cds)
                # if parents are not the same, the merge them
                if top_parent != bottom_parent:
                    top_cds.union(bottom_cds)
                    # break wall and redraw both cells
                    top_cell = self._cells[i][j]
                    top_cell.has_bottom_wall = False
                    top_cell.draw()
                    bottom_cell = self._cells[i][j + 1]
                    bottom_cell.has_top_wall = False
                    bottom_cell.draw()
                
    def _get_walls(self):

        walls = []

        for i in range(self._num_cols):

            for j in range(self._num_rows):
                
                if j != self._num_rows - 1: # Cell not at the last row
                    # Get bottom wall and add to walls
                    b_wall = Wall(i, j, 'b')
                    walls.append(b_wall)

                if i != self._num_cols - 1: # Cell not at the last column
                    # Get right wall and add to walls
                    r_wall = Wall(i, j, 'r')
                    walls.append(r_wall)
        
        return walls

class Wall():

    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction

    def __repr__(self):
        return f"Wall({self.i}, {self.j}, {self.direction})"
    
class CellDisjointSet():

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.size = 1
        self.parent = self

    def find(self, cds):
        if cds.parent != cds:
            # Find parent of cds
            cds.parent = self.find(cds.parent)
        return cds.parent
    
    def union(self, other):

        # Get our parents
        my_parent = self.find(self)
        their_parent = self.find(other)

        if my_parent != their_parent:

            # if the size of my parent is bigger, 
            # set their parent to my parent and increment the size of my parent by 1, 
            # and vice versa
            if my_parent.size > their_parent.size:
                their_parent.parent = my_parent
                my_parent.size += 1
            else:
                my_parent.parent = their_parent
                their_parent.size += 1


win = Window(800, 800)
maze = Maze(50, 200, 10, 14, 50, 50, win)
#maze = Maze(50, 200, 5, 5, 50, 50, win)
maze._draw_cells()
maze._break_entrance_and_exit()
maze._break_walls()
win._root.mainloop()
