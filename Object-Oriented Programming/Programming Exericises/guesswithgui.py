__class__ = "CS 1410"
__project__ = "Programming Exercise 8.5"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/3/2021"
__divider__ = "------------------------------------------------------------------------"

"""
Write a GUI-based program that plays a guess-the-number game in which the roles of the
computer and the user are the reverse of what they are in the Case Study of this
chapter. In this version of the game, the computer guesses a number between 1
(lowerBound) and 100 (upperBound) and the user provides the responses.

The window should display the computer’s guesses with a label. The user enters a hint in
response, by selecting one of a set of command buttons labeled Too small, Too large, and
Correct. When the game is over, you should disable these buttons and wait for the user
to click New game, as before.
"""

import random
from breezypythongui import EasyFrame


class GuessingGame(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window,widgets, and data."""
        EasyFrame.__init__(self, title="Guessing Game")
        self.lowerBound = 1
        self.upperBound = 100
        self.count = 0
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel = self.addLabel(
            text=guess, row=0, column=0, sticky="NSEW", columnspan=4
        )
        self.small = self.addButton(
            text="Too small", row=1, column=0, command=self.goLarge
        )
        self.large = self.addButton(
            text="Too large", row=1, column=1, command=self.goSmall
        )
        self.correct = self.addButton(
            text="Correct", row=1, column=2, command=self.goCorrect
        )
        self.newButton = self.addButton(
            text="New game", row=1, column=3, command=self.newGame
        )

    def goLarge(self):
        """Guess was too small, so move guess to the right of the number."""
        # Write code here
        self.count += 1
        self.lowerBound = self.myNumber + 1
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        self.myLabel["text"] = str(self.myNumber)

    def goSmall(self):
        """Guess was too large, so move guess to the left of the number."""
        self.count += 1
        self.upperBound = self.myNumber - 1
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        self.myLabel["text"] = str(self.myNumber)

    def goCorrect(self):
        """Guess was too correct, so announce and wait."""
        # Write code here
        self.count += 1
        self.small["state"] = "disabled"
        self.large["state"] = "disabled"
        self.correct["state"] = "disabled"

    def newGame(self):
        """Resets the GUI to its original state."""
        # Write code here
        self.count = 0
        self.lowerBound = 1
        self.upperBound = 100
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        self.small["state"] = "normal"
        self.large["state"] = "normal"
        self.correct["state"] = "normal"
        self.myLabel["text"] = f"Is the number {self.myNumber}?"


def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")

