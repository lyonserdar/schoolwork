__class__ = "CS 1410"
__project__ = "Programming Exercise 6.1"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "1/26/2021"
__divider__ = "------------------------------------------------------------------------"

"""
Define and test a function myRange. This function should behave like Python’s standard
range function, with the required and optional arguments, but it should return a list.
Do not use the range function in your implementation!
Study Python’s help on range to determine the names, positions, and what to do with your
function’s parameters. Use a default value of None for the two optional parameters. If
these parameters both equal None, then the only provided argument should be considered
the stop value, and the start value should default to 0. If just the third parameter
equals None, then the function has been called with a start and stop value. Thus, the
first part of the function’s code establishes what the values of the parameters are or
should be. The rest of the code uses those values to build a list by counting up or
down.
An example of the myRange function with only one argument provided is shown below:
print(myRange(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def myRange(start=0, stop=None, step=None):
    """Returns a list of numbers with given start, stop, step"""
    range_list = []
    if stop and start > stop:
        temp = 0
        temp = start
        start = stop
        stop = temp

        if not step:
            step = -1

        while stop > start:
            range_list.append(stop)
            stop += step

    if not stop:
        stop = start
        start = 0
        step = 1

        if not step:
            step = 1

        while start < stop:
            range_list.append(start)
            start += step
    else:
        if not step:
            step = 1
        while start < stop:
            range_list.append(start)
            start += step
    print(range_list)
    return range_list


print(myRange(5))
print(myRange(5, 9))
print(myRange(5, 18, 2))
print(myRange(9, 5))
