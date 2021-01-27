"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""
__class__ = "CS 1410"
__project__ = "Project 2 - Human Pyramids"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "1/27/2021"
__divider__ = "------------------------------------------------------------------------"

import sys
from time import perf_counter


function_call_counter = 0
cache_hits_counter = 0
cache = {}


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
    print(__divider__)
    print(__project__)
    print(__divider__)
    print()
    start = perf_counter()
    main()
    end = perf_counter() - start
    print()
    print(f"Elapsed time: {end:.20f} seconds")
    print("Number of function calls:", function_call_counter)
    print("Number of cache hits:", cache_hits_counter)
