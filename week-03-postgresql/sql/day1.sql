--Week3 (we will be learning SQL by PostgreSQL)
--Day 1 (where, select, group by, having, order by)

CREATE DATABASE day1;

CREATE TABLE students (
    s_id INT PRIMARY KEY,
    s_name TEXT NOT NULL,
    s_age INT NOT NULL,
    s_department TEXT NOT NULL
)

INSERT into students (s_id, s_name, s_age, s_department) VALUES
(1, 'John Doe', 20, 'Computer Science'),
(2, 'Jane Smith', 22, 'Mathematics'),
(3, 'Alice Johnson', 21, 'Physics'),
(4, 'Bob Brown', 23, 'Chemistry'),
(5, 'Charlie Davis', 20, 'Biology'),
(6, 'David Wilson', 22, 'Computer Science'),
(7, 'Eve Thompson', 21, 'Mathematics'),
(8, 'Frank White', 23, 'Physics'),
(9, 'Grace Lee', 20, 'Chemistry'),
(10, 'Hannah Martin', 22, 'Biology');

--SELECT statement
SELECT * FROM students;   

--ORDER BY clause 
SELECT * from students ORDER BY s_age, s_id DESC;
SELECT * from students ORDER BY s_age ASC;

--WHERE clause
SELECT * from students WHERE s_age > 21;
SELECT * from students WHERE s_department = 'Computer Science';
SELECT * from students WHERE s_age BETWEEN 20 AND 22;
SELECT * from students WHERE s_name LIKE 'J%';
SELECT * from students WHERE s_department IN ('Mathematics', 'Physics');
SELECT * from students WHERE s_age IS NOT NULL;
SELECT * from students WHERE s_age IS NULL;
SELECT * from students WHERE s_age <> 21;\
SELECT * from students WHERE s_id  = 2 AND (s_department = 'Mathematics' OR s_department = 'Computer Science');


--GROUP BY clause
SELECT s_department, COUNT(*) as student_count FROM students GROUP BY s_department;
SELECT s_department, AVG(s_age) as average_age FROM students GROUP BY s_department;
SELECT s_department, MAX(s_age) as oldest_student FROM students GROUP BY s_department;  
SELECT s_department, MIN(s_age) as youngest_student FROM students GROUP BY s_department;
SELECT s_department, SUM(s_age) as total_age FROM students GROUP BY s_department;

--HAVING clause
SELECT s_department, COUNT(*) AS student_count
FROM students
GROUP BY s_department
HAVING COUNT(*) > 1;   