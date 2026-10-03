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
(5, 'Charlie Davis', 20, 'Biology');

SELECT * FROM students;