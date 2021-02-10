__class__ = "CS 1410"
__project__ = "Programming Exercise 11.2"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/10/2021"
__divider__ = "------------------------------------------------------------------------"

"""
The list method reverse reverses the elements in the list. Define a function named
reverse that reverses the elements in its list argument (without using the inbuilt
reverse() list method).

Try to make this function as efficient as possible, and state its computational
complexity using big-O notation.
"""


def reverse(lyst):
    # Define your reverse function here without using the inbuilt reverse() method.
    lyst[:] = lyst[::-1]


def main():
    """Tests with two lists."""
    lyst = list(range(4))
    reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    reverse(lyst)
    print(lyst)


if __name__ == "__main__":
    main()
