#!/usr/bin/env python
"""
Word Class
Author: Ali Aydogdu
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""


class Word:
    """
    Word class is a helper class to provide methods for easy access to sign_bit, opcode,
    operand, and magnitude of an instruction or data that stored in memory
    """

    def __init__(self, word="00000"):
        """
        Default word value is "00000"
        """
        self.__word = word

    def get_sign_bit(self):
        """
        Returns the Sign Bit 
        If "1" negative number, otherwise positive number 
        """
        return self.__word[0]

    def get_opcode(self):
        """
        Returns the opcode of the instruction
        """
        return self.__word[1:3]

    def get_operand(self):
        """
        Returns the operand of the instruction
        """
        return self.__word[3:]

    def get_magnitude(self):
        """
        Returns all the bits except sign bit
        This is used when stored data is not an instruction, it is rather pure data
        """
        return self.__word[1:]

    def __str__(self):
        """
        Returns string representation of the word
        """
        return self.__word
