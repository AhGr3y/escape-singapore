from graphics import (
    Window,
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
        self.parent = None

    def __repr__(self):
        return f"Cell(Top-left coordinate: ({self.p1.x},{self.p1.y}), Bottom-right coordinate: ({self.p2.x},{self.p2.y}))"

    def draw(self, fill_color="white"):

        # raise error if root window not set
        if self.win is None:
            raise ValueError("Root window not set.")

        # Get top wall of cell
        top_wall = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
        # check if cell has top wall
        if self.has_top_wall:
            # Draw top wall with fill_color
            self.win.draw_line(top_wall, fill_color)
        # cell does not have top wall
        elif self.has_top_wall == False:
            # Draw top wall with background color
            self.win.draw_line(top_wall, self.win._bg_color)

        # Get right wall of cell
        right_wall = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
        # check if cell has right wall
        if self.has_right_wall:
            # Draw right wall with fill_color
            self.win.draw_line(right_wall, fill_color)
        # cell does not have right wall
        elif self.has_right_wall == False:
            # Draw right wall with background color
            self.win.draw_line(right_wall, self.win._bg_color)

        # Get bottom wall of cell
        bottom_wall = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
        # check if cell has bottom wall
        if self.has_bottom_wall:
            # Draw bottom wall with fill_color
            self.win.draw_line(bottom_wall, fill_color)
        # cell does not have bottom wall
        elif self.has_bottom_wall == False:
            # Draw bottom wall with background color
            self.win.draw_line(bottom_wall, self.win._bg_color)

        # Get left wall of cell
        left_wall = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
        # check if cell has left wall
        if self.has_left_wall:
            # Draw left wall with fill_color
            self.win.draw_line(left_wall, fill_color)
        # cell does not have left wall
        elif self.has_left_wall == False:
            # Draw left wall with background color
            self.win.draw_line(left_wall, self.win._bg_color)