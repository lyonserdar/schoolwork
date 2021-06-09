"""
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

"""
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


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
        self.count += other.count

    def __sub__(self, other):
        self.count -= other.count

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
    pass


def main():
    """ 
    Program kicks off here.
    """
    tree = BST()

    tree.add(Pair("d", 4))
    tree.add(Pair("e", 5))
    tree.add(Pair("a", 1))
    tree.add(Pair("b", 2))
    tree.add(Pair("c", 3))
    tree.add(Pair("f", 6))
    tree.add(Pair("g", 7))

    print(tree.inorder())

    print(tree.height())

    print(tree.find(Pair("d")))

    print(tree.size())


if __name__ == "__main__":
    main()
