"""
Author: Moa Burke
Date: 10 Oct 2024
Description:
    This program implements a simple Pong game using Python's Turtle graphics module.
    Players control paddles to hit a ball back and forth, with the objective of scoring
    points by making the opponent miss the ball. The game keeps track of scores and
    displays a winner when a player reaches a specified score.

Version: 1.0

Changelog:
    - 1.0: Initial release of the Pong Game with basic functionality including paddle movement,
           ball physics, scoring system, and game reset capability.
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Game configuration constants
SCREEN_WIDTH = 800 # Width of thr game screen
SCREEN_HEIGHT = 600 # Height of the game screen
BACKGROUND_COLOR = "gray10" # Background color of the screen
TITLE = "Pong Game by Moa Burke"

# Dashed line properties
LINE_START_POS = (0, 300)
LINE_COLOR = "aquamarine3" # Color of the dashed line
LINE_SIZE = 4
DASH_LENGTH = 30
DASH_GAP = 10
LINE_SEGMENTS = 15

# Game control constants
UP_KEY_LEFT = "w" # Key to move the left paddle up
DOWN_KEY_LEFT = "s" # Key to move the left paddle down
UP_KEY_RIGHT = "Up" # Key to move the right paddle up
DOWN_KEY_RIGHT = "Down" # Key to move the right paddle down
RESTART_KEY = "space" # Key to restart the game
EXIT_KEY = "Escape" # Key to end the game

# Starting position constants
Y_POS_START = 0
X_POS_LEFT_START = -350
X_POS_RIGHT_START = 350

# Game state variables
game_is_running = True # Main loop control variable
game_over_state = False # Flag to check if the game is in "game over" state

def play_again():
    """Resets the game state to allow the player to start over."""
    global game_over_state
    scoreboard.reset()  # Reset the scoreboard
    l_paddle.reset_paddle(X_POS_LEFT_START, Y_POS_START)  # Reset left paddle position
    r_paddle.reset_paddle(X_POS_RIGHT_START, Y_POS_START)  # Reset right paddle position
    game_over_state = False  # Reset the game-over flag to continue the game

def press_space_bar():
    """
    Handles the event of pressing the space bar to restart the game.

    If the game is in the "game over" state, this function triggers the 'play_again()'
    function to reset the game and start over.
    """
    if game_over_state:
        play_again()

def move_up_left():
    """Moves the left paddle up if the game is not over."""
    if not game_over_state:
        l_paddle.move_up()

def move_down_left():
    """Moves the left paddle down if the game is not over."""
    if not game_over_state:
        l_paddle.move_down()

def move_up_right():
    """Moves the right paddle up if the game is not over."""
    if not game_over_state:
        r_paddle.move_up()

def move_down_right():
    """Moves the right paddle down if the game is not over."""
    if not game_over_state:
        r_paddle.move_down()

def end_game():
    """Ends the game if it is in the game over state."""
    if game_over_state:
        global game_is_running
        game_is_running = False

def draw_dashed_line():
    """
    Draws a dashed line down the center of the screen.
    """
    draw_line = Turtle() # Create a new turtle instance for thr center line
    draw_line.color(LINE_COLOR) # Set the color
    draw_line.penup() #List the pen to move without drawing
    draw_line.goto(*LINE_START_POS) # Move to the top of the screen
    draw_line.setheading(270) # Set the turtle to face downward
    draw_line.pensize(LINE_SIZE) # Set the width of the dashed line

    for _ in range (LINE_SEGMENTS): # Draw the dashed line by looping
        draw_line.pendown() #Start drawing
        draw_line.forward(DASH_LENGTH) # Move forward to create a dash
        draw_line.penup() # List pen to create a gap
        draw_line.forward(DASH_GAP) # Move forward to create a gap

    draw_line.hideturtle() # Hide the turtle when done

# Set up the screen
screen = Screen() # Create a screen object from the Screen class
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT) # Set up screen size
screen.bgcolor(BACKGROUND_COLOR) # Set background
screen.title(TITLE) # Set title
screen.tracer(0) # Turn off automatic screen updates for smoother animation

# Draw the center line
draw_dashed_line()

# Set up the scoreboard and ask for player names
scoreboard = Scoreboard() # Create a scoreboard object
name_first = scoreboard.set_player_name(screen.textinput(title="Enter Your Name", prompt="Player One: ")) # Get player 1 name
name_second = scoreboard.set_player_name(screen.textinput(title="Enter Your Name", prompt="Player Two: ")) # Get player 2 name
scoreboard.update_scoreboard() # Update the scoreboard with initial scores and player names

# Define win condition based on scoreboard's win score
WIN_CONDITION = scoreboard.WIN_SCORE

# Create paddles for both players
l_paddle = Paddle(x_pos=X_POS_LEFT_START, y_pos=Y_POS_START) # Create left paddle
r_paddle = Paddle(x_pos=X_POS_RIGHT_START, y_pos=Y_POS_START) # Create right paddle

# Create ball object
ball = Ball()

# Set up keys binding for controlling the paddles
screen.listen() # Enable screen to listen for keystrokes
screen.onkeypress(move_up_left, UP_KEY_LEFT) # Move left paddle up when 'w' key is pressed
screen.onkeypress(move_down_left, DOWN_KEY_LEFT) # Move left paddle up when 's' key is pressed
screen.onkeypress(move_up_right, UP_KEY_RIGHT) # Move right paddle up when 'Up' key is pressed
screen.onkeypress(move_down_right, DOWN_KEY_RIGHT) # Move right paddle down when 'Down' key is pressed

# Bind the space key to restart the game
screen.onkey(press_space_bar, RESTART_KEY) # Restart the game on space bar press
# Bind the esc key to exit the game
screen.onkey(end_game, EXIT_KEY) # Exit the game on escape key press


#Start the game loop
while game_is_running:
    screen.update()  # Update the screen manually

    if not game_over_state:

        ball.move_ball()  # Move the ball across the screen
        time.sleep(ball.move_speed)  # Control the speed of the ball

        # Detect collision with top and bottom walls
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y() # Reverse the ball's y direction when it hits the wall

        #Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()  # Reverse the ball's x direction when it hits the paddle

        # Detect when left paddle misses the ball
        if ball.xcor() < -380:
            ball.reset_position() # Reset ball to center
            scoreboard.r_increase_score() # Increase left payer score

        # Detect when right paddle misses the ball
        if ball.xcor() > 380:
            ball.reset_position() # Reset ball to center
            scoreboard.l_increase_score() # Increase left payer score

        # Check for a winner
        if scoreboard.l_score == WIN_CONDITION or scoreboard.r_score == WIN_CONDITION:
            scoreboard.display_winner() # Display the winner message
            scoreboard.display_restart_message()  # Prompt to restart the game
            game_over_state = True  # Set the game over state to stop the game loop

    else:
        pass # If the game is over, the game will wait for a space-bar press to reset