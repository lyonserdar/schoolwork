#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I declare that the following source code was written solely by me. I understand that
copying any source code, in whole or in part, constitutes cheating, and that I will
receive a zero on this project if I am found in violation of this policy.
This script benchmarks the speed difference of linear search, binary search and, jump
search"""

# * Project 1 - Benchmarking Search Algorithms

__project__ = "Project 1 - Benchmarking Search Algorithms"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "6/15/2021"
__divider__ = "------------------------------------------------------------------------"

from random import seed, sample
from time import perf_counter
from math import sqrt

DATA_SIZE = 1_000_000
SEED = 10


def linear_search(lyst, target):
    """Linear search algorithm"""
    i = 0
    while i < len(lyst):
        if lyst[i] == target:
            return True
        i += 1
    return False


def binary_search(lyst, target, left=0, right=0):
    """Binary search algorithm"""
    if right == 0:
        # initialize the right
        right = len(lyst) - 1

    if left > right:
        # target not found, search unsuccessfully ended
        return False

    # set the middle point of the search
    middle = (left + right) // 2

    if lyst[middle] == target:
        # target found, search successfully ended
        return True
    elif lyst[middle] < target:
        # search the right side
        left = middle + 1
        return binary_search(lyst, target, left, right)
    elif lyst[middle] > target:
        # search the left side
        right = middle - 1
        return binary_search(lyst, target, left, right)


def jump_search(lyst, target):
    """Jump search algorithm"""
    jump = int(sqrt(len(lyst)))
    index = 0

    while index < len(lyst):
        if lyst[index] == target:
            return True
        elif lyst[index] > target:
            return linear_search(lyst[index - jump : index], target)

        index += jump

    return linear_search(lyst[index - jump :], target)


def generate_data():
    """Generates the data"""
    seed(10)
    data = sample(range(DATA_SIZE * 2), k=DATA_SIZE)
    data.sort()
    while True:
        yield data


def benchmark(func, *args):
    """Performs benchmark for given function and returns elapsed time"""
    start = perf_counter()
    func(*args)
    finish = perf_counter()
    return f"{finish - start:.10f}"


def main():
    """This is the main function"""
    print(__divider__)
    print(__project__)
    print(__divider__)
    data = next(generate_data())  # Generate the data
    print("['first_element', 'middle_element', 'last_element', 'missing_element']")
    results = []
    print("Benchmark for Linear Search")
    results.append(benchmark(linear_search, data, data[0]))
    results.append(benchmark(linear_search, data, data[(len(data) // 2)]))
    results.append(benchmark(linear_search, data, data[-1]))
    results.append(benchmark(linear_search, data, -1))
    print(results)
    results.clear()
    print("Benchmark for Binary Search")
    results.append(benchmark(binary_search, data, data[0]))
    results.append(benchmark(binary_search, data, data[(len(data) // 2)]))
    results.append(benchmark(binary_search, data, data[-1]))
    results.append(benchmark(binary_search, data, -1))
    print(results)
    results.clear()
    print("Benchmark for Jump Search")
    results.append(benchmark(jump_search, data, data[0]))
    results.append(benchmark(jump_search, data, data[(len(data) // 2 - 4)]))
    results.append(benchmark(jump_search, data, data[-1]))
    results.append(benchmark(jump_search, data, -1))
    print(results)


if __name__ == "__main__":
    main()
