__class__ = "CS 1410"
__project__ = "Programming Exercise 9.1 and 9.2"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/1/2021"
__divider__ = "------------------------------------------------------------------------"

"""
9.1 
Add three methods to the Student class that compare twoStudent objects. One method
(__eq__) should test for equality. A second method (__lt__) should test for less than.
The third method (__ge__) should test for greater than or equal to. In each case, the
method returns the result of the comparison of the two students’ names. Include a main
function that tests all of the comparison operators.

Note: The program should output in the following format: False: False True: True True:
True False: False True: True True: True True: True True: True True: True True: True 
9.2
This project assumes that you have completed Project 1. Place several Student objects
into a list and shuffle it. Then run the sort method with this list and display all of
the students’ information. Print to the console the unsorted list first of all students
followed by the sorted list of all students

Note: The sorted list should output in the following format:

Sorted list of students: Name: Name1 Scores: 0 0 0 0 0 0 0 0 0 0 Name: Name2 Scores: 0 0
0 0 0 0 0 0 0 0 Name: Name3 Scores: 0 0 0 0 0 0 0 0 0 0 Name: Name4 Scores: 0 0 0 0 0 0
0 0 0 0 Name: Name5 Scores: 0 0 0 0 0 0 0 0 0 0

"""

import random


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    def __lt__(self, other):
        """Returns self < other, with respect
        to names."""
        return self.name < other.name

    def __ge__(self, other):
        """Returns self >= other, with respect
        to names."""
        return self.name >= other.name

    def __eq__(self, other):
        """Tests for equality."""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name


def main():
    """Tests sorting."""
    # Create the list and put 5 students into it
    lyst = []
    for count in reversed(range(5)):
        s = Student("Name" + str(count + 1), 10)
        lyst.append(s)

    # Complete the definition of the main function
    random.shuffle(lyst)

    for item in lyst:
        print(item)

    lyst.sort()

    for item in lyst:
        print(item)


if __name__ == "__main__":
    main()
