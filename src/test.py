import unittest

from graphics import Window
from maze import (
    Maze,
    Wall,
)

class Test(unittest.TestCase):
    
    def test_generate_maze(self):
        win = Window(800, 800)
        maze = Maze(50, 50, 5, 5, 50, 50, win)
        maze._draw_cells()
        for i in range(maze._num_cols):
            x1 = maze._x1 + maze._cell_width * i
            x2 = x1 + maze._cell_width
            for j in range(maze._num_rows):
                y1 = maze._y1 + maze._cell_height * j
                y2 = y1 + maze._cell_height
                self.assertEqual(x1, maze._cells[i][j].p1.x)
                self.assertEqual(x2, maze._cells[i][j].p2.x)
                self.assertEqual(y1, maze._cells[i][j].p1.y)
                self.assertEqual(y2, maze._cells[i][j].p2.y)

    def test_get_walls(self):
        win = Window(800, 800)
        maze = Maze(50, 50, 4, 4, 50, 50, win)
        maze._draw_cells()
        walls = maze._get_walls()
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                if j != maze._num_rows - 1:
                    b_wall = Wall(i, j, 'b')
                    self.assertEqual(str(b_wall), f"Wall({i}, {j}, b)")
                if i != maze._num_cols - 1:
                    r_wall = Wall(i, j, 'r')
                    self.assertEqual(str(r_wall), f"Wall({i}, {j}, r)")

    def test_get_walls_more_walls(self):
        win = Window(800, 800)
        maze = Maze(50, 50, 20, 20, 50, 50, win)
        maze._draw_cells()
        walls = maze._get_walls()
        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                if j != maze._num_rows - 1:
                    b_wall = Wall(i, j, 'b')
                    self.assertEqual(str(b_wall), f"Wall({i}, {j}, b)")
                if i != maze._num_cols - 1:
                    r_wall = Wall(i, j, 'r')
                    self.assertEqual(str(r_wall), f"Wall({i}, {j}, r)")

if __name__ == "__main__":
    unittest.main()