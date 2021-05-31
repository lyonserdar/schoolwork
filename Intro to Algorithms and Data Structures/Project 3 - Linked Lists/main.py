#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
I declare that the following source code was written solely by me. I understand that
copying any source code, in whole or in part, constitutes cheating, and that I will
receive a zero on this project if I am found in violation of this policy.
"""

# * Project 3 - Student Class List

__project__ = "Project 3 - Student Class List"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "5/31/2021"
__divider__ = "------------------------------------------------------------------------"

from course import Course
from courselist import CourseList

FILENAME = "data.txt"


def read_data(filename):
    """Reads the course data"""
    with open(filename, "r") as f:
        return f.read().splitlines()


def organize_data(data):
    """Create a course list"""
    course_list = CourseList()
    for line in data:
        line = line.split(",")
        course_list.insert(Course(line[0], line[1], line[2], line[3]))
    return course_list


def display_report(course_list):
    """Displays the course report"""
    print(f"Current List: ({course_list.size()})")
    print(course_list)
    print(f"\n\nCumulative GPA: {course_list.calculate_gpa():.3f}")


def main():
    """This is the main function"""
    print(__divider__)
    print(__project__)
    print(f"by {__author__}")
    print(__divider__)
    data = read_data(FILENAME)
    course_list = organize_data(data)
    display_report(course_list)


if __name__ == "__main__":
    main()
