#!/usr/bin/env python

"""
Project: 6 - Hashmap
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 06/10/2021
Date Last Modified: 06/11/2021
"""


class HashMap:
    """
    Hashmap
    """

    def __init__(self):
        """
        Initialize
        """
        self.__capacity = 7
        self.__size = 0
        self.__hash_map = [[] for _ in range(self.__capacity)]

    def __hash(self, key):
        """
        Returns the hash value of the key
        """
        row, col = key
        return (row * 10 + col) % self.__capacity

    def __rehash(self):
        self.__capacity = 2 * self.__capacity - 1
        new_hash_map = [[] for _ in range(self.__capacity)]

        for bucket in self.__hash_map:
            for index, entry in enumerate(bucket):
                entry_key, entry_value = entry
                hash_key = self.__hash(entry_key)
                new_hash_map[hash_key].append((entry))

        self.__hash_map = new_hash_map

    def get(self, key):
        """
        Returns the value for key if key is in the dictionary.
        If key is not in the dictionary, raises a KeyError.
        """
        hash_key = self.__hash(key)
        bucket = self.__hash_map[hash_key]

        for index, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if key == entry_key:
                return entry_value

        raise KeyError()

    def set(self, key, value):
        """
        Adds the key-value pair to the hashmap.
        If the load-factor >= 80%, rehashes the hashmap and doubles the capacity.
        """
        hash_key = self.__hash(key)
        bucket = self.__hash_map[hash_key]

        key_found = False

        for index, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if key == entry_key:
                bucket[index] = (key, value)
                key_found = True
                break

        if not key_found:
            bucket.append((key, value))
            self.__size += 1

        if self.__size / self.__capacity >= 0.80:
            self.__rehash()

    def remove(self, key):
        """
        Removes the key-value pair from the hashmap.
        If the key does not exist, nothing happens.
        """
        hash_key = self.__hash(key)
        bucket = self.__hash_map[hash_key]

        for index, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if key == entry_key:
                bucket.remove(entry)

    def clear(self):
        """
        Empties the hashmap
        """
        self.__capacity = 7
        self.__size = 0
        self.__hash_map = [[] for _ in range(self.__capacity)]

    def capacity(self):
        """
        Returns the capacity of the hashmap.
        """
        return self.__capacity

    def size(self):
        """
        Returns the number of key-value pairs in the hashmap.
        """
        return self.__size

    def keys(self):
        """
        Returns a list of all keys in the hashmap.
        """
        keys_list = []
        for bucket in self.__hash_map:
            for index, entry in enumerate(bucket):
                entry_key, entry_value = entry
                keys_list.append(entry_key)

        return keys_list

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        hash_key = self.__hash(key)
        bucket = self.__hash_map[hash_key]

        for index, entry in enumerate(bucket):
            entry_key, entry_value = entry
            if key == entry_key:
                return True

        return False
