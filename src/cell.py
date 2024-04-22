from graphics import (
    Point,
    Line,
)

class Cell:

    def __init__(self, p1, p2, win=None):
        self.p1 = p1
        self.p2 = p2
        self.win = win
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, fill_color="white"):

        # raise error if root window not set
        if self.win is None:
            raise ValueError("Root window not set.")

        # check if cell has top wall
        if self.has_top_wall:
            # Get top wall of cell
            top_wall = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
            # Draw top wall
            self.win.draw_line(top_wall, fill_color)

        # check if cell has right wall
        if self.has_right_wall:
            # Get right wall of cell
            right_wall = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
            # Draw right wall
            self.win.draw_line(right_wall, fill_color)

        # check if cell has bottom wall
        if self.has_bottom_wall:
            # Get bottom wall of cell
            bottom_wall = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
            # Draw bottom wall
            self.win.draw_line(bottom_wall, fill_color)

        # check if cell has left wall
        if self.has_left_wall:
            # Get left wall of cell
            left_wall = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
            # Draw left wall
            self.win.draw_line(left_wall, fill_color)