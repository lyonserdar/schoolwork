-- ----------------------------------------------------------------------
-- Assignment 1
-- ----------------------------------------------------------------------
-- Author: Ali Aydogdu
-- Email: lyonserdar@gmail.com
-- Course: CS 3520
-- To run the script:
--      psql -d new_university -a -f Assignment1.sql
-- ----------------------------------------------------------------------
-- Insert yourself as a Student and add your major
-- You will need to define a unique value for stuId
INSERT INTO student (stuid, lastname, firstname, major, credits)
    VALUES ('S200000', 'Aydogdu', 'Ali', 'CSC', 80);

-- Insert (Enroll) yourself in class CSC201A
INSERT INTO enroll (stuid, classnumber, grade)
    VALUES ('S200000', 'CSC201A', 'A');

-- Select every Class that meets on Monday
EXPLAIN
SELECT
    *
FROM
    class
WHERE
    schedule LIKE '%M%';

-- Delete student with the stuId (1020' from Class 'MTH101B'

-- Update the grade for the student with stuId 'S1010' in class 'MTH103C' with a 'B'

-- Jane Riveria has graduated. Delete her data from both the Student and Enroll tables

-- Student Edward Burns changed his major to history and earned 12 more credits
-- Update the students information

-- There is a new Python CSC class
-- Insert the new class. The classNumber is CSC227A and it meets on M, W and F at 10 in room M009

-- A new Art teacher has joined the factulty and there last name is Close
-- Insert the the new teacher into the Faculty table

-- select all CSC classes that students are enrolled in
