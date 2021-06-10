#!/usr/bin/env python

"""
Project: 6 - Hashmap
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 06/10/2021
Date Last Modified: 06/10/2021
"""


class HashMap:
    """
    Hashmap
    """

    def __init__(self):
        """
        Initialize
        """
        pass

    def __get_hash(self, key):
        """
        Returns the hash value of the key
        """
        pass

    def get(self, key):
        """
        Returns the value for key if key is in the dictionary.
        If key is not in the dictionary, raises a KeyError.
        """
        pass

    def set(self, key, value):
        """
        Adds the key-value pair to the hashmap.
        If the load-factor >= 80%, rehashes the hashmap and doubles the capacity.
        """
        pass

    def remove(self, key):
        """
        Removes the key-value pair from the hashmap.
        If the key does not exist, nothing happens.
        """
        pass

    def clear(self):
        """
        Empties the hashmap
        """
        pass

    def capacity(self):
        """
        Returns the capacity of the hashmap.
        """
        pass

    def size(self):
        """
        Returns the number of key-value pairs in the hashmap.
        """
        pass

    def keys(self):
        """
        Returns a list of all keys in the hashmap.
        """
        pass
