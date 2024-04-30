import random

from tkinter import PhotoImage

class Bot():

    def __init__(self, level, row, col, player, maze=None):
        self._maze = maze
        self._level = level
        self._row = row
        self._col = col
        self._player = player
        self._img = None
        self._body = None
        self._move_direction = None
        self.draw()
        self.patrol()

    def draw(self):

        if self._maze is None:
            raise ValueError("Maze not defined.")
        
        if self._col > self._maze._num_cols or self._row > self._maze._num_rows:
            raise ValueError("Cannot draw bot outside of maze.")

        # draw a level 1 bot
        if self._level == 1:
            
            # set initial move direction
            if self._row == 0:
                self._move_direction = "down"
            elif self._row == self._maze._num_rows - 1:
                self._move_direction = "up"
            else:
                self._move_direction = random.choice(["up", "down"])

            x = self._maze._x1 + self._maze._cell_width/2 + (self._col * self._maze._cell_width)
            y = self._maze._y1 + self._maze._cell_height/2 + (self._row * self._maze._cell_height)

            try:
                self._img = PhotoImage(file="./assets/images/level-1-bot.png")
            except Exception as e:
                print("Error loading character image:", e)
                return
            
            self._body = self._maze.win._canvas.create_image(x, y, image=self._img)

    def patrol(self):

        if self._body is None:
            raise ValueError("Bot body is not defined.")
        
        # level 1 bot patrols up and down
        if self._level == 1:

            # Change direction when reach the edge of maze
            if self._row == self._maze._num_rows - 1:
                self._move_direction = "up"
            if self._row == 0:
                self._move_direction = "down"

            # Move bot down
            if self._move_direction == "down":
                self._maze.win._canvas.move(self._body, 0, self._maze._cell_height)
                self._row += 1

                # End the game if bot encounters player; additional hit box to make up for the delay, if not, player can touch bot from the back
                if self._col == self._player._col and self._row - 1 == self._player._row:
                    self.game_over()

            # Move bot up
            if self._move_direction == "up":
                self._maze.win._canvas.move(self._body, 0, -self._maze._cell_height)
                self._row -= 1

                # End the game if bot encounters player; additional hit box to make up for the delay, if not, player can touch bot from the back
                if self._col == self._player._col and self._row + 1 == self._player._row:
                    self.game_over()

            # End the game if bot encounters player
            if self._col == self._player._col and self._row == self._player._row:
                self.game_over()

            self._maze.win._root.after(300, self.patrol)

    def game_over(self):
        self._maze.win._root.destroy()
        print("Game over!")