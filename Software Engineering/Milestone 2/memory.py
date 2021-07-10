#!/usr/bin/env python
"""
Memory Class
Author: Ali Aydogdu
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""


class Memory:
    """
    Memory class creates a list of memory locations that can be accessed with index
    The user can specify the memory size, default to 100
    Memory can not grow or shrink
    """

    def __init__(self, size=100):
        self.__size = size
        self.__memory = ["00000"] * size

    def clear(self):
        """
        Clears the memory by setting all the locations to "00000"
        """
        for index in range(self.__size):
            self.__memory[index] = "00000"

    def get_size(self):
        """
        Returns the size of the memory
        """
        return self.__size

    def get_data_at(self, location=0):
        """
        Returns the data value at the given memory location
        """
        return self.__memory[location]

    def set_data_at(self, location=0, data="00000"):
        """
        Stores the given data value at the given memory location
        """
        self.__memory[location] = data

    def find_opcode(self, opcode):
        """
        Checks if a specific opcode in the memory
        This is a helper function to see if the code has "HALT"
        Potentially this function does not belong here
        """
        for data in self.__memory:
            if opcode == data[1:3]:
                return True

        return False
