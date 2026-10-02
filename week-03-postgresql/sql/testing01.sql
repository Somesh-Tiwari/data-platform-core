--Week 3 - Day 0 practice and testing SQL queries

-- Test query
SELECT version();

-- Create a sample table
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    major VARCHAR(100)
);

-- Insert sample data
INSERT INTO students (name, age, major) VALUES
('Somesh', 25, 'Data Engineering'),
('John', 22, 'Computer Science'),
('Jane', 24, 'Mathematics');

-- Query the data
SELECT * FROM students;