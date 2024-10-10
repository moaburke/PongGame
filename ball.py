"""
Author: Moa Burke
Date: 10 Oct 2024
Description: This module defines the Ball class for a Pong Game, inheriting from the Turtle class.
             The Ball class handles the movement, bouncing behavior, and reset logic for the game.

Version: 1.0

Changelog:
    - 1.0: Initial creation of the Ball class with movement, bounce, and reset functionality.
"""

from turtle import Turtle

# Ball reset position constants
START_X = 0 # X-coordinate for ball reset
START_Y = 0 # Y-coordinate for ball reset
BALL_RESET_POSITION = (0, 0) # Position where the ball resets

# Ball movement constants
INITIAL_SPEED = 0.1 #Initial ball speed
INITIAL_X_MOVE = 10 # Initial horizontal movement increment
INITIAL_Y_MOVE = 10 # Initial vertical movement increment
SPEED_INCREMENT = 0.9 # Factor by which the speed increases after bouncing
REVERSE_DIRECTION = -1 # Multiplier to reverse the ball direction

# Animation speed constant
ANIMATION_SPEED = "slowest" # Speed of the ball's animation

# Appearance constants
BALL_SHAPE = "circle"
BALL_COLOR = "white"

class Ball(Turtle):
    def __init__(self):
        super().__init__() # Initialize the turtle superclass
        self.shape(BALL_SHAPE) # Set shape of the ball
        self.color(BALL_COLOR) # Set color of the ball
        self.penup() # Lift pen to avoid drawing lines
        self.speed(ANIMATION_SPEED) # #Set the ball's animation speed to the slowest
        self.move_speed = INITIAL_SPEED # Initialize ball movement speed
        # Set initial movement directions
        self.x_move = INITIAL_X_MOVE
        self.y_move = INITIAL_Y_MOVE

    def move_ball(self):
        """
        Moves the ball by updating its x and y coordinates.
        The ball moves by adding x_move and y_move to its current position.
        """
        new_x = self.xcor() + self.x_move # Calculate new x-coordinate
        new_y = self.ycor() + self.y_move # Calculate new y-coordinate
        self.goto(new_x, new_y) # Move the ball to the new position

    def bounce_y(self):
        """
        Reverses the y direction of the ball to simulate bouncing off the top or bottom walls.
        """
        self.y_move *= REVERSE_DIRECTION # Reverse the y movement direction

    def bounce_x(self):
        """
        Reverses the x direction of the ball to simulate bouncing off a paddle
        and increases the ball's speed to make the game more challenging.
        """
        self.x_move *= REVERSE_DIRECTION # Reverse the movement direction
        self.move_speed *= SPEED_INCREMENT #Increase the ball speed by reducing sleep time between moves

    def reset_position(self):
        """
        Resets the ball to the center of the screen after a point is scored.
        Also reverses the x direction to ensure the ball moves in opposite direction.
        """
        self.goto(START_X, START_Y) # Move the ball to the center of the screen
        self.x_move *= REVERSE_DIRECTION # Reverse the x direction to send the ball toward the other player
        self.move_speed = INITIAL_SPEED # Reset the movement speed to the initial value