#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I declare that the following source code was written solely by me. I understand that
copying any source code, in whole or in part, constitutes cheating, and that I will
receive a zero on this project if I am found in violation of this policy. This script
benchmarks the speed difference of quicksort, mergesort, insertion sort, selection sort,
and timesort"""

# * Project 2 - Benchmarking Sorting Algorithms

__project__ = "Project 2 - Benchmarking Sorting Algorithms"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "6/15/2021"
__divider__ = 72 * "-"

from random import seed, sample, randint
from time import perf_counter

DATA_SIZE = 10_000
SEED = 10


def quicksort(lyst):
    """Quicksort implementation"""
    if len(lyst) < 2:
        return lyst

    low, high, same = [], [], []

    pivot = lyst[randint(0, len(lyst) - 1)]  # random pivot

    for element in lyst:
        if element < pivot:
            low.append(element)
        elif element > pivot:
            high.append(element)
        else:
            same.append(element)

    return quicksort(low) + same + quicksort(high)


def mergesort(lyst):
    """Mergesort implementation"""

    def merge(left, right):
        """Merges the left and right sublists"""
        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        list_to_return = []
        left_index = 0
        right_index = 0

        while len(list_to_return) < len(left) + len(right):
            if left[left_index] <= right[right_index]:
                list_to_return.append(left[left_index])
                left_index += 1
            else:
                list_to_return.append(right[right_index])
                right_index += 1

            if left_index == len(left):
                list_to_return.extend(right[right_index:])
                break

            if right_index == len(right):
                list_to_return.extend(left[left_index:])
                break

        return list_to_return

    if len(lyst) < 2:
        return lyst

    midpoint = len(lyst) // 2

    left = lyst[:midpoint]
    right = lyst[midpoint:]

    return merge(mergesort(left), mergesort(right))


def insertion_sort(lyst):
    """Insertion sort implementation"""
    for index in range(1, len(lyst)):
        stored_value = lyst[index]
        insertion_index = index
        while insertion_index > 0 and lyst[insertion_index - 1] > stored_value:
            lyst[insertion_index] = lyst[insertion_index - 1]
            insertion_index -= 1
        lyst[insertion_index] = stored_value
    return lyst


def selection_sort(lyst):
    """Selection sort implementation"""
    for index in range(len(lyst) - 1):
        minimum_index = index
        for compare_index in range(index + 1, len(lyst)):
            if lyst[compare_index] < lyst[minimum_index]:
                minimum_index = compare_index
        temp = lyst[index]
        lyst[index] = lyst[minimum_index]
        lyst[minimum_index] = temp
    return lyst


def bubble_sort(lyst):
    """Bubble sort implementation"""
    for index in range(1, len(lyst)):
        sorted_flag = True
        for compare_index in range(len(lyst) - index):
            if lyst[compare_index] > lyst[compare_index + 1]:
                temp = lyst[compare_index]
                lyst[compare_index] = lyst[compare_index + 1]
                lyst[compare_index + 1] = temp
                sorted_flag = False
        if sorted_flag:
            break
    return lyst


def timsort(lyst):
    """Timsort call"""
    lyst.sort()  # Use builtin timesort
    return lyst


def is_sorted(lyst):
    """Check if the given list is sorted"""
    # check if lyst is a list
    if type(lyst) is not list:
        return False
    if len(lyst) == 0:
        return False
    if not all(isinstance(x, int) for x in lyst):
        return False
    if not all(lyst[i] <= lyst[i + 1] for i in range(len(lyst) - 1)):
        return False
    return True


def generate_data():
    """Generates the data"""
    seed(10)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    while True:
        yield data


def benchmark(func, *args):
    """Performs benchmark for given function and returns elapsed time"""
    start = perf_counter()
    func(*args)
    finish = perf_counter()
    return f"{finish - start:.6f}"


def test_sorting_algorithms(data, name, algorithm):
    """Tests the sorting algorithms"""
    print(f"Starting {name}")
    print(f"{name} duration: {benchmark(algorithm, data)} seconds.\n")


def main():
    """This is the main function"""
    print(__divider__)
    print(__project__)
    print(f"by {__author__}")
    print(__divider__)
    data = next(generate_data())  # Generate the data
    test_sorting_algorithms(data.copy(), "Insertion Sort", insertion_sort)
    test_sorting_algorithms(data.copy(), "Selection Sort", selection_sort)
    test_sorting_algorithms(data.copy(), "Bubble Sort", bubble_sort)
    test_sorting_algorithms(data.copy(), "Mergesort", mergesort)
    test_sorting_algorithms(data.copy(), "Quicksort", quicksort)
    test_sorting_algorithms(data.copy(), "Timsort", timsort)


if __name__ == "__main__":
    main()
