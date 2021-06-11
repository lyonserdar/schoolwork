#!/usr/bin/env python

"""
Project: 6 - Hashmap | Pyramid
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 06/10/2021
Date Last Modified: 06/11/2021
"""

import sys
from time import perf_counter
from hashmap import HashMap


function_call_counter = 0
cache_hits_counter = 0
cache = HashMap()


def weight_on(r, c):
    weight = 0
    global function_call_counter
    global cache_hits_counter
    function_call_counter += 1
    if (r, c) in cache:
        cache_hits_counter += 1
        return cache[(r, c)]
    if r < 0 or c < 0:
        raise Exception("r and c must be greater than or equal to 0")
    elif c > r:
        raise Exception("c must be smaller than or equal to r")
    elif r == 0:
        weight = 0.0
    elif c == 0:
        weight = weight_on(r - 1, 0) / 2 + 100
    elif c == r:
        weight = weight_on(r - 1, c - 1) / 2 + 100
    else:
        weight = weight_on(r - 1, c - 1) / 2 + 100 + weight_on(r - 1, c) / 2 + 100
    cache[(r, c)] = weight
    return weight


def main():
    if len(sys.argv) > 1:
        row_count = int(sys.argv[1])
        for r in range(row_count):
            for c in range(r + 1):
                print(f"{weight_on(r, c):.2f}", end=" ")
            print()


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter() - start
    print()
    print(f"Elapsed time: {end:.20f} seconds")
    print("Number of function calls:", function_call_counter)
    print("Number of cache hits:", cache_hits_counter)
