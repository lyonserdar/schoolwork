#!/usr/bin/env python

# ======================================================================================
# * Project 3 - Main
# ======================================================================================
# Author: Ali Serdar Aydogdu
# Email: lyonserdar@gmail.com
# UVU ID: 10593855
# Class: CS 2420-601
# Date Created: 05/12/2021
# Date Last Modified: 06/2/2021

# Imports
from course import Course
from courselist import CourseList

# Constants
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
    data = read_data(FILENAME)
    course_list = organize_data(data)
    display_report(course_list)


if __name__ == "__main__":
    main()
