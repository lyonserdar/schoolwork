-- ----------------------------------------------------------------------------------------
-- Assignment 1
-- ----------------------------------------------------------------------------------------
-- Author: Ali Aydogdu
-- Email: lyonserdar@gmail.com
-- Course: CS 3520-602
-- Date Created: 7/3/2021
-- Date Last Modified: 7/9/2021
-- To run the script:
--      psql -d new_university -a -f Assignment1.sql
-- ----------------------------------------------------------------------------------------
SELECT
    count(*)
FROM
    "public"."class";

SELECT
    count(*)
FROM
    "public"."enroll";

SELECT
    count(*)
FROM
    "public"."faculty";

SELECT
    count(*)
FROM
    "public"."student";

-- ----------------------------------------------------------------------------------------
-- 1. Insert yourself as a Student and add your major
-- You will need to define a unique value for stuId
-- ----------------------------------------------------------------------------------------
SELECT
    count(*)
FROM
    "public"."student";

INSERT INTO "public"."student" ("stuid", "lastname", "firstname", "major", "credits")
    VALUES ('S200000', 'Aydogdu', 'Ali', 'CSC', 80);

SELECT
    count(*)
FROM
    "public"."student";

EXPLAIN
SELECT
    *
FROM
    "public"."student"
WHERE
    "stuid" = 'S200000';

SELECT
    *
FROM
    "public"."student"
WHERE
    "stuid" = 'S200000';

-- ----------------------------------------------------------------------------------------
-- 2.  Insert (Enroll) yourself in class MTH748C. Give yourself an 'A'
-- ----------------------------------------------------------------------------------------
SELECT
    count(*)
FROM
    "public"."enroll";

INSERT INTO "public"."enroll" ("stuid", "classnumber", "grade")
    VALUES ('S200000', 'MTH748C', 'A');

SELECT
    count(*)
FROM
    "public"."enroll";

EXPLAIN
SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = 'S200000';

SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = 'S200000';

-- ----------------------------------------------------------------------------------------
-- 3. Select every Class that meets on Monday
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."class"
WHERE
    "schedule" LIKE '%M%';

SELECT
    *
FROM
    "public"."class"
WHERE
    "schedule" LIKE '%M%'
LIMIT 10;

-- ----------------------------------------------------------------------------------------
-- 4. Delete student with the stuId ('S100760' from Class 'HST1049C')
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = 'S100760'
    AND "classnumber" = 'HST1049C';

SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = 'S100760'
    AND "classnumber" = 'HST1049C';

DELETE FROM "public"."enroll"
WHERE "stuid" = 'S100760'
    AND "classnumber" = 'HST1049C';

SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = 'S100760'
    AND "classnumber" = 'HST1049C';

-- ----------------------------------------------------------------------------------------
-- 5. Update the grade for the student with stuId 'S100784' in class 'MTH1022A' with a 'B'
-- ----------------------------------------------------------------------------------------
UPDATE
    "enroll"
SET
    "grade" = 'B'
WHERE
    "stuid" = 'S100784'
    AND "classnumber" = 'MTH1022A';

-- ----------------------------------------------------------------------------------------
-- 6. Barbara Jones has graduated. Delete her data from both the Student and Enroll tables
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = (
        SELECT
            "stuid"
        FROM
            "public"."student"
        WHERE
            "firstname" = 'BARBARA'
            AND "lastname" = 'JONES');

SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = (
        SELECT
            "stuid"
        FROM
            "public"."student"
        WHERE
            "firstname" = 'BARBARA'
            AND "lastname" = 'JONES');

DELETE FROM "public"."enroll"
WHERE "stuid" = (
        SELECT
            "stuid"
        FROM
            "public"."student"
        WHERE
            "firstname" = 'BARBARA'
            AND "lastname" = 'JONES');

SELECT
    *
FROM
    "public"."enroll"
WHERE
    "stuid" = (
        SELECT
            "stuid"
        FROM
            "public"."student"
        WHERE
            "firstname" = 'BARBARA'
            AND "lastname" = 'JONES');

EXPLAIN
SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'BARBARA'
    AND "lastname" = 'JONES';

SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'BARBARA'
    AND "lastname" = 'JONES';

DELETE FROM "public"."student"
WHERE "firstname" = 'BARBARA'
    AND "lastname" = 'JONES';

SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'BARBARA'
    AND "lastname" = 'JONES';

-- ----------------------------------------------------------------------------------------
-- 7. Student John Ling changed his major to history and earned 12 more credits
-- Update the students information
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'JOHN'
    AND "lastname" = 'LING';

SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'JOHN'
    AND "lastname" = 'LING';

UPDATE
    "public"."student"
SET
    "major" = 'History',
    "credits" = "credits" + 12
WHERE
    "firstname" = 'JOHN'
    AND "lastname" = 'LING';

SELECT
    *
FROM
    "public"."student"
WHERE
    "firstname" = 'JOHN'
    AND "lastname" = 'LING';

-- ----------------------------------------------------------------------------------------
-- 8. There is a new Python CSC class
-- Insert the new class. The classNumber is CSC227A and it meets on M, W and F at 10 in room M009.
-- The class is taught by Lor with Faculty Id F308
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."class"
WHERE
    "classnumber" = 'CSC227A';

SELECT
    *
FROM
    "public"."class"
WHERE
    "classnumber" = 'CSC227A';

INSERT INTO "public"."class" ("classnumber", "facid", "schedule", "room")
    VALUES ('CSC227A', 'F308', 'MWF10', 'M009');

SELECT
    *
FROM
    "public"."class"
WHERE
    "classnumber" = 'CSC227A';

-- ----------------------------------------------------------------------------------------
-- 9. A new Art teacher has joined the faculty and there last name is Close. Close's rank is Instructor
-- Insert the the new teacher into the Faculty table
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."faculty"
WHERE
    "facid" = 'F380';

SELECT
    *
FROM
    "public"."faculty"
WHERE
    "facid" = 'F280';

INSERT INTO "public"."faculty" ("facid", "name", "department", "fac_rank")
    VALUES ('F380', 'CLOSE', 'Art', 'Instructor');

SELECT
    *
FROM
    "public"."faculty"
WHERE
    "facid" = 'F380';

-- ----------------------------------------------------------------------------------------
-- 10. select all students that are CSC majors
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "public"."student"
WHERE
    "major" LIKE 'CSC';

SELECT
    *
FROM
    "public"."student"
WHERE
    "major" LIKE 'CSC'
LIMIT 10;
