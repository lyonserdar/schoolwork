-- ----------------------------------------------------------------------------------------
-- Assignment 1
-- ----------------------------------------------------------------------------------------
-- Author: Ali Aydogdu
-- Email: lyonserdar@gmail.com
-- Course: CS 3520
-- To run the script:
--      psql -d new_university -a -f Assignment1.sql
-- ----------------------------------------------------------------------------------------
-- ----------------------------------------------------------------------------------------
-- Insert yourself as a Student and add your major
-- You will need to define a unique value for stuId
--                                    QUERY PLAN
-- ----------------------------------------------------------------------------------------
-- INSERT ON student (
--     COST = 0.00..0.01 ROWS = 1 width = 390) -> Result (
--     COST = 0.00..0.01 ROWS = 1 width = 390)
-- ----------------------------------------------------------------------------------------
EXPLAIN INSERT INTO "student" ("stuid", "lastname", "firstname", "major", "credits")
    VALUES ('S200000', 'Aydogdu', 'Ali', 'CSC', 80);

-- ----------------------------------------------------------------------------------------
-- Insert (Enroll) yourself in class MTH748C
--                                    QUERY PLAN
-- ----------------------------------------------------------------------------------------
-- INSERT ON enroll (
--     COST = 0.00..0.01 ROWS = 1 width = 84) -> Result (
--     COST = 0.00..0.01 ROWS = 1 width = 84)
-- ----------------------------------------------------------------------------------------
EXPLAIN INSERT INTO "enroll" ("stuid", "classnumber", "grade")
    VALUES ('S200000', 'MTH748C', 'A');

-- ----------------------------------------------------------------------------------------
-- Select every Class that meets on Monday
--                                    QUERY PLAN
-- ----------------------------------------------------------------------------------------
-- Seq Scan on class  (cost=0.00..20.50 rows=672 width=29)
--    Filter: ((schedule)::text ~~ '%M%'::text)
-- ----------------------------------------------------------------------------------------
EXPLAIN
SELECT
    *
FROM
    "class"
WHERE
    "schedule" LIKE '%M%';

-- ----------------------------------------------------------------------------------------
-- Delete student with the stuId ('S100760') from Class 'HST1049C'
--                                         QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Delete on enroll  (cost=0.29..8.31 rows=1 width=6)
--    ->  Index Scan using enroll_pkey on enroll  (cost=0.29..8.31 rows=1 width=6)
--          Index Cond: ((stuid = 'S100760'::bpchar) AND (classnumber = 'HST1049C'::bpchar))
-- ----------------------------------------------------------------------------------------
EXPLAIN DELETE FROM "enroll"
WHERE "stuid" = 'S100760'
    AND "classnumber" = 'HST1049C';

-- ----------------------------------------------------------------------------------------
-- Update the grade for the student with stuId 'S100784' in class 'MTH1022A' with a 'B'
--                                         QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Update on enroll  (cost=0.29..8.31 rows=1 width=33)
--    ->  Index Scan using enroll_pkey on enroll  (cost=0.29..8.31 rows=1 width=33)
--          Index Cond: ((stuid = 'S100784'::bpchar) AND (classnumber = 'MTH1022A'::bpchar))
-- ----------------------------------------------------------------------------------------
EXPLAIN UPDATE
    "enroll"
SET
    "grade" = 'B'
WHERE
    "stuid" = 'S100784'
    AND "classnumber" = 'MTH1022A';

-- ----------------------------------------------------------------------------------------
-- Barbara Jones has graduated. Delete her data from both the Student and Enroll tables
--                                             QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Delete on enroll  (cost=489.53..500.05 rows=3 width=6)
--    InitPlan 1 (returns $0)
--      ->  Seq Scan on student  (cost=0.00..485.22 rows=1 width=8)
--            Filter: (((firstname)::text = 'BARBARA'::text) AND ((lastname)::text = 'JONES'::text))
--    ->  Bitmap Heap Scan on enroll  (cost=4.31..14.83 rows=3 width=6)
--          Recheck Cond: (stuid = $0)
--          ->  Bitmap Index Scan on enroll_pkey  (cost=0.00..4.31 rows=3 width=0)
--                Index Cond: (stuid = $0)
--                                            QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Delete on student  (cost=0.00..485.22 rows=1 width=6)
--    ->  Seq Scan on student  (cost=0.00..485.22 rows=1 width=6)
--          Filter: (((firstname)::text = 'BARBARA'::text) AND ((lastname)::text = 'JONES'::text))
-- ----------------------------------------------------------------------------------------
EXPLAIN DELETE FROM "enroll"
WHERE "stuid" = (
        SELECT
            "stuid"
        FROM
            "student"
        WHERE
            "firstname" = 'BARBARA'
            AND "lastname" = 'JONES');

EXPLAIN DELETE FROM "student"
WHERE "firstname" = 'BARBARA'
    AND "lastname" = 'JONES';

-- ----------------------------------------------------------------------------------------
-- Student John Ling changed his major to history and earned 12 more credits
-- Update the students information
--                                          QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Update on student  (cost=0.00..485.22 rows=1 width=149)
--    ->  Seq Scan on student  (cost=0.00..485.22 rows=1 width=149)
--          Filter: (((firstname)::text = 'JOHN'::text) AND ((lastname)::text = 'LING'::text))
-- ----------------------------------------------------------------------------------------
EXPLAIN UPDATE
    "student"
SET
    "major" = 'History',
    "credits" = "credits" + 12
WHERE
    "firstname" = 'JOHN'
    AND "lastname" = 'LING';

-- ----------------------------------------------------------------------------------------
-- There is a new Python CSC class
-- Insert the new class. The classNumber is CSC227A and it meets on M, W and F at 10 in room M009
--                      QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Insert on class  (cost=0.00..0.01 rows=1 width=166)
--    ->  Result  (cost=0.00..0.01 rows=1 width=166)
-- ----------------------------------------------------------------------------------------
EXPLAIN INSERT INTO "class" ("classnumber", "schedule", "room")
    VALUES ('CSC227A', 'MWF10', 'M009');

-- ----------------------------------------------------------------------------------------
-- A new Art teacher has joined the faculty and there last name is Close
-- Insert the the new teacher into the Faculty table
--                       QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  Insert on faculty  (cost=0.00..0.01 rows=1 width=254)
--    ->  Result  (cost=0.00..0.01 rows=1 width=254)
-- ----------------------------------------------------------------------------------------
EXPLAIN INSERT INTO "faculty" ("facid", "name", "department", "fac_rank")
    VALUES ('F380', 'CLOSE', 'Art', 'Instructor');

-- ----------------------------------------------------------------------------------------
-- select all CSC classes that students are enrolled in
--                             QUERY PLAN
-- ----------------------------------------------------------------------------------------
--  HashAggregate  (cost=323.06..332.97 rows=991 width=11)
--    Group Key: classnumber
--    ->  Seq Scan on enroll  (cost=0.00..312.77 rows=4115 width=11)
--          Filter: (classnumber ~~ 'CSC%'::text)
-- ----------------------------------------------------------------------------------------
EXPLAIN SELECT DISTINCT
    "classnumber"
FROM
    "enroll"
WHERE
    "classnumber" LIKE 'CSC%';
