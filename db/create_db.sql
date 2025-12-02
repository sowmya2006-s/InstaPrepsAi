CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    gpa NUMERIC(3,2)
);

INSERT INTO students (first_name, last_name, email, gpa)
VALUES 
    ('Sowmya', 'S', 'sowmya@.com', 9.5),
    ('Anu', 'S', 'anu@.com', 7.5),
    ('Shalu', 'R', 'shalu@.com', 7.8),
    ('Shakthi', 'S', 'shakthi@example.com', 8.5);

SELECT * FROM students;
