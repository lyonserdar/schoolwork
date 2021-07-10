#!/usr/bin/env python
"""
Accumulator Class
Author: Ali Aydogdu
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""


class Accumulator:
    """
    Simple function for Accumulator 
    You can set and get the data
    This can be updated to add data validation
    Right now it can store anything
    Author: Ali Aydogdu
    """

    def __init__(self, init_value="00000"):
        self.__data = init_value

    def get_data(self):
        """
        Returns the data stored in accumulator
        """

        return self.__data

    def set_data(self, data):
        """
        Sets the accumulators data
        """

        self.__data = data
