"""
Author: Moa Burke
Date: 10 Oct 2024
Description: This module defines the Paddle class for a Pong Game, inheriting from the Turtle class.
             The Paddle class handles movement and positioning.

Version: 1.0

Changelog:
    - 1.0: Initial creation of the Paddle class with movement and reset functionality.
"""

from turtle import Turtle

# Paddle appearance constants
PADDLE_SHAPE = "square" # Shape of the paddle
PADDLE_COLOR = "aquamarine3" # Color of the paddle
PADDLE_WIDTH = 1 # Width of the paddle shape (default is 20)
PADDLE_HEIGHT = 5 #Height of the paddle shape (default is 100)

# Paddle movement constants
PADDLE_MOVE_DISTANCE = 20 # Distance to move the paddle up or down
PADDLE_TOP_LIMIT = 250 # Y-coordinate limit for the upper boundary
PADDLE_BOTTOM_LIMIT = -240 # Y-coordinate limit for the lower boundary

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__() # Initialize the turtle class
        self.shape(PADDLE_SHAPE) # Set the paddle shape
        self.color(PADDLE_COLOR) # Set the paddle color
        self.penup() # Lift pen to avoid drawing lines
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)  # Paddle size height=100, width=20
        self.goto(x=x_pos, y=y_pos)  # Move paddle to its starting position

    def move_up(self):
        """
        Moves the paddle up if it is below upper limit.
        """
        if self.ycor() >= PADDLE_TOP_LIMIT:
            pass # If paddle is at the upper limit, do nothing
        else:
            new_y = self.ycor() + PADDLE_MOVE_DISTANCE # Calculate new y position
            self.goto(self.xcor(), new_y) # Move the paddle to the new position

    def move_down(self):
        """
        Moves the paddle down if it is above the lower limit.
        """
        if self.ycor() <= PADDLE_BOTTOM_LIMIT:
            pass # If paddle is at the lower limit, do nothing
        else:
            new_y = self.ycor() - PADDLE_MOVE_DISTANCE # Calculate new y position
            self.goto(self.xcor(), new_y) # MOve the paddle to the new position

    def reset_paddle(self, x_pos, y_pos):
        """
        Resets the paddle to its starting position.
        """
        self.goto(x=x_pos, y=y_pos)  # Move paddle to its starting position