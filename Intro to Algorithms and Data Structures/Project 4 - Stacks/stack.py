#!/usr/bin/env python

# ======================================================================================
# * Project 4 - Stack
# ======================================================================================
# Author: Ali Serdar Aydogdu
# Email: lyonserdar@gmail.com
# UVU ID: 10593855
# Class: CS 2420-601
# Date Created: 05/12/2021
# Date Last Modified: 06/2/2021


class Stack:
    """Stack"""

    class Node:
        """Node"""

        def __init__(self, data):
            """Initialize node"""
            self.data = data
            self.next = None

    def __init__(self):
        """Initialize"""
        self.head = None
        self.__size = 0

    def push(self, item):
        """Pushes an item onto the stack, size increases by 1"""
        node = Stack.Node(item)
        node.next = self.head
        self.head = node
        self.__size += 1

    def pop(self):
        """
        Removes the top item from the stack and returns it, raises an IndexError if the
        stack is empty
        """
        if self.__size < 1:
            raise IndexError("Stack is empty!")
        node = self.head
        self.head = node.next
        self.__size -= 1
        return node.data

    def top(self):
        """
        Returns the item on top of the stack without removing it, raises an IndexError
        if the stack is empty
        """
        if self.__size < 1:
            raise IndexError("Stack is empty!")
        return self.head.data

    def size(self):
        """
        Returns the number of items on the stack
        """
        return self.__size

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise
        """
        return self.head is None

    def clear(self):
        """
        Empty the stack
        """
        self.head = None
        self.__size = 0
