"""
Author: Moa Burke
Date: 10 Oct 2024
Description: This module defines the Scoreboard class for a Pong Game, inheriting from the Turtle class.
             The Ball class handles the score display and players name.

Version: 1.0

Changelog:
    - 1.0: Initial creation of the Ball class with movement, bounce, and reset functionality.
"""


from turtle import Turtle

# Scoreboard appearance constants
ALIGNMENT = "center" # Text alignment for the scoreboard
FONT_LARGE = ("Courier", 46, "normal") # Font for the mail score display
FONT_MEDIUM = ("Courier", 36, "normal") # Font for the mail score display
FONT_SMALL = ("Courier", 18, "normal") # Font for the small messages
FONT_SMALLEST = ("Courier", 12, "normal") # Font for the small messages
FONT_COLOR = "white"

# Score game constants
WIN_SCORE = 1 # Score needed to win the game
START_SCORE = 0 # Initial score for both players
SCORE_INCREMENT = 1

# Scoreboard position constants
SCORE_POSITION = (0, 220) # Position for the score
L_NAME_POSITION = (-110, 205) # Position for the left player's name
R_NAME_POSITION = (110, 205) # Position for the right player's name
WIN_MESSAGE_POSITION = (0, 0) # Position for displaying the winner's message
RESTART_MESSAGE_POSITION = (0, -240) # Position for displaying the restart message
EXIT_GAME_MESSAGE_POSITION = (0, -270) #Position for displaying the exit game message


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__() # Initialize the turtle superclass
        self.WIN_SCORE = WIN_SCORE # Set winning score
        self.l_score = START_SCORE # Initialize left player's score
        self.r_score = START_SCORE # Initialize right player's score
        self.l_name = "" # Initialize left player's name
        self.r_name = "" # Initialize left player's name
        self.init_scoreboard() # Set up scoreboard appearance
        self.update_scoreboard() # Display initial scores

    def init_scoreboard(self):
        """
        Initialize the scoreboard's appearance.
        """
        self.color(FONT_COLOR) # Set text color
        self.penup() # Lift the pen up to avoid drawing lines
        self.hideturtle() # Hide the turtle icon

    def update_scoreboard(self):
        """
        Updates the scoreboard display with current scores and player names.
        """
        self.clear() # Clear the previous score
        self.setposition(*L_NAME_POSITION) # Set positions for the left player's name
        self.write(f"{self.l_name}", align=ALIGNMENT, font=FONT_SMALLEST) # Write left player's name
        self.setposition(*R_NAME_POSITION) # Set positions for the right player's name
        self.write(f"{self.r_name}", align=ALIGNMENT, font=FONT_SMALLEST) # Write right player's name
        self.setposition(*SCORE_POSITION) # Set position for the score
        self.write(f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT_LARGE) # Display scores

    def l_increase_score(self):
        """
        Increases the left player's score and updates the scoreboard.
        """
        self.l_score += SCORE_INCREMENT # Increment left player's score
        self.update_scoreboard() # Update the display

    def r_increase_score(self):
        """
        Increases the right player's score and updates the scoreboard.
        """
        self.r_score += SCORE_INCREMENT # Increment right player's score
        self.update_scoreboard() # Update the display

    def display_winner(self):
        """
        Display the winner's name when a player reaches the winning score.
        """
        winner = ""
        if self.l_score == WIN_SCORE:
            winner = self.l_name # Set the winner to left player's name
        elif self.r_score == WIN_SCORE:
            winner = self.r_name # Set the winner to right player's name

        self.setposition(*WIN_MESSAGE_POSITION)
        self.write(f"{winner} WINS!", align=ALIGNMENT, font=FONT_MEDIUM)

    def set_player_name(self, name):
        """
        Sets the player's name for the scoreboard.
        """
        if self.l_name == "":
            self.l_name = name.upper() # Set left player's name
        else:
            self.r_name = name.upper() # Set right player's name

    def reset(self):
        """
        Reset the scores for both players to the staring score.
        """
        self.l_score = START_SCORE # Reset left player's score
        self.r_score = START_SCORE # Reset right player's score
        self.update_scoreboard() # Update the display

    def display_restart_message(self):
        """
        Displays a message prompting the player to restart the game.
        """
        self.setposition(*RESTART_MESSAGE_POSITION)  # Position the restart message
        self.write("Press Space to restart", align=ALIGNMENT, font=FONT_SMALL)  # Write the restart message
        self.setposition(*EXIT_GAME_MESSAGE_POSITION)  # Position the restart message
        self.write("Press Esc to exit game", align=ALIGNMENT, font=FONT_SMALLEST)  # Write the exit game message
