#!/usr/bin/env python

"""
Project: 4 - Binary Search Tree
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 05/12/2021
Date Last Modified: 06/09/2021
"""

from pathlib import Path
from string import whitespace, punctuation
from bst import BST


INPUT_FILE = "around-the-world-in-80-days-3 copy.txt"
PUNCTUATIONS = (
    "\n",
    " ",
    ".",
    ",",
    '"',
    ":",
    ";",
    "!",
    "'",
    "(",
    ")",
    "-",
    "?",
    "`",
)


class Pair:
    """ 
    Encapsulate letter,count pair as a single entity.
    Relational methods make this object comparable using built-in operators. 
    """

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __add__(self, other):
        return Pair(self.letter, self.count + other.count)

    def __sub__(self, other):
        return Pair(self.letter, self.count - other.count)

    def __repr__(self):
        return f"({self.letter}, {self.count})"

    def __str__(self):
        return f"({self.letter}, {self.count})"


def make_tree():
    """ 
    A helper function to build the tree.
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    """
    tree = BST()

    with open(INPUT_FILE, "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c not in PUNCTUATIONS:
                tree.add(Pair(c))

    return tree


def main():
    """ 
    Program kicks off here.
    """
    make_tree()


if __name__ == "__main__":
    main()
