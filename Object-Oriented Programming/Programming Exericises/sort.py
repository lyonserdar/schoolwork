__class__ = "CS 1410"
__project__ = "Programming Exercise 11.5"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/10/2021"
__divider__ = "------------------------------------------------------------------------"

"""
Python’s list method sort includes the keyword argument reverse, whose default value is
False. The programmer can override this value to sort a list in descending order.

Modify the selectionSort function discussed in this chapter so that it allows the
programmer to supply this additional argument (as the second parameter) to redirect the
sort.
"""


def selectionSort(lyst, reverse=False):
    """Sorts the items in lyst in ascending order."""
    i = 0
    while i < len(lyst) - 1:  # Do n – 1 searches
        minIndex = i  # for the smallest item
        j = i + 1
        while j < len(lyst):  # Start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:  # Swap if necessary
            swap(lyst, minIndex, i)
        i += 1
    if reverse:
        lyst[:] = lyst[::-1]


def swap(lyst, x, y):
    """Exchanges the elements at positions x and y."""
    lyst[x], lyst[y] = lyst[y], lyst[x]


def main():
    """Tests with four lists."""
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst)
    print(lyst)
    lyst = [2, 4, 3, 0, 1, 5]
    selectionSort(lyst, reverse=True)
    print(lyst)
    lyst = list(range(6))
    selectionSort(lyst, reverse=True)
    print(lyst)


if __name__ == "__main__":
    main()

