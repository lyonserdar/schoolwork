__class__ = "CS 1410"
__project__ = "Programming Exercise 5.1"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "1/15/2021"
__divider__ = "------------------------------------------------------------------------"

"""
A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers. Define these functions, median and
mode, in a module named stats.py. Also include a function named mean, which computes the
average of a set of numbers. Each function should expect a list of numbers as an
argument and return a single number. Each function should return 0 if the list is empty.
Include a main function that tests the three statistical functions using the following
list defined in main:
lyst = [3, 1, 7, 1, 4, 10]
An example of the program output is shown below:
List: [3, 1, 7, 1, 4, 10] Mode: 1 Median: 3.5 Mean: 4.33333333333333
"""


def median(numbers):
    """Calculates the median"""
    if not numbers:
        return 0
    numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[int(len(numbers) / 2)]
    else:
        return (numbers[int(len(numbers) / 2 - 1)] + numbers[int(len(numbers) / 2)]) / 2


def mode(numbers):
    """Calculates the mode"""
    if not numbers:
        return 0
    return max(set(numbers), key=numbers.count)


def mean(numbers):
    """Calculates the mean"""
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def main():

    lyst = [3, 1, 7, 1, 4, 10]

    print(f"List: {lyst}")
    print(f"Mode: {mode(lyst)}")
    print(f"Median: {median(lyst)}")
    print(f"Mean: {mean(lyst)}")


if __name__ == "__main__":
    main()
