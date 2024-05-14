-- Task 1. Database Design:

-- Create the database named "SISDB"
CREATE DATABASE SISDB;

-- Use the SISDB database
USE SISDB;

-- Create the Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone_number VARCHAR(20)
);

-- Create the Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- Create the Enrollments table
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create the Teacher table
CREATE TABLE Teacher (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100)
);

-- Create the Payments table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Insert data into the Students table
INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number)
VALUES
    (1, 'Raj', 'Patel', '2000-01-01', 'raj.patel@example.com', '1234567890'),
    (2, 'Emily', 'Johnson', '2000-02-02', 'emily.johnson@example.com', '9876543210'),
    (3, 'Aarav', 'Sharma', '2000-03-03', 'aarav.sharma@example.com', '1231231234'),
    (4, 'Sophia', 'Williams', '2000-04-04', 'sophia.williams@example.com', '4567890123'),
    (5, 'Aaradhya', 'Brown', '2000-05-05', 'aaradhya.brown@example.com', '7890123456'),
    (6, 'James', 'Patel', '2000-06-06', 'james.patel@example.com', '2345678901'),
    (7, 'Olivia', 'Smith', '2000-07-07', 'olivia.smith@example.com', '6789012345'),
    (8, 'Arjun', 'Johnson', '2000-08-08', 'arjun.johnson@example.com', '3456789012'),
    (9, 'Emma', 'Gupta', '2000-09-09', 'emma.gupta@example.com', '8901234567'),
    (10, 'Ayaan', 'Miller', '2000-10-10', 'ayaan.miller@example.com', '5678901234'),
    (11, 'Liam', 'Kumar', '2000-11-11', 'liam.kumar@example.com', '9012345678'),
    (12, 'Aria', 'Jones', '2000-12-12', 'aria.jones@example.com', '4321098765'),
    (13, 'Ishaan', 'Anderson', '2001-01-01', 'ishaan.anderson@example.com', '2109876543'),
    (14, 'Ella', 'Singh', '2001-02-02', 'ella.singh@example.com', '6543210987'),
    (15, 'Aryan', 'Wilson', '2001-03-03', 'aryan.wilson@example.com', '8765432109'),
    (16, 'Mia', 'Patel', '2001-04-04', 'mia.patel@example.com', '3210987654'),
    (17, 'Aaliyah', 'Thompson', '2001-05-05', 'aaliyah.thompson@example.com', '7654321098'),
    (18, 'Aadvik', 'Brown', '2001-06-06', 'aadvik.brown@example.com', '5432109876'),
    (19, 'Ethan', 'Sharma', '2001-07-07', 'ethan.sharma@example.com', '9876543210'),
    (20, 'Amelia', 'Lee', '2001-08-08', 'amelia.lee@example.com', '6789012345');

-- Insert data into the Courses table
INSERT INTO Courses (course_id, course_name, credits, teacher_id)
VALUES
    (1, 'Mathematics', 3, 1),
    (2, 'English Literature', 3, 2),
    (3, 'Computer Science', 4, 3),
    (4, 'History', 3, 4),
    (5, 'Physics', 4, 5),
    (6, 'Chemistry', 4, 6),
    (7, 'Biology', 4, 7),
    (8, 'Economics', 3, 8),
    (9, 'Psychology', 3, 9),
    (10, 'Sociology', 3, 10),
    (11, 'Political Science', 3, 11),
    (12, 'Art History', 3, 12),
    (13, 'Geography', 3, 13),
    (14, 'Literary Theory', 3, 14),
    (15, 'Philosophy', 3, 15),
    (16, 'Music Theory', 3, 16),
    (17, 'Statistics', 4, 17),
    (18, 'Data Science', 4, 18),
    (19, 'Engineering', 4, 19),
    (20, 'Business Management', 4, 20);

-- Insert data into the Enrollments table
INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date)
VALUES
    (1, 1, 1, '2024-01-01'),
    (2, 2, 2, '2024-01-15'),
    (3, 3, 3, '2024-01-20'),
    (4, 4, 4, '2024-02-05'),
    (5, 5, 5, '2024-02-10'),
    (6, 6, 6, '2024-02-15'),
    (7, 7, 7, '2024-02-20'),
    (8, 8, 8, '2024-03-01'),
    (9, 9, 9, '2024-03-05'),
    (10, 10, 10, '2024-03-10'),
    (11, 11, 11, '2024-03-15'),
    (12, 12, 12, '2024-03-20'),
    (13, 13, 13, '2024-04-01'),
    (14, 14, 14, '2024-04-05'),
    (15, 15, 15, '2024-04-10'),
    (16, 16, 16, '2024-04-15'),
    (17, 17, 17, '2024-04-20'),
    (18, 18, 18, '2024-05-01'),
    (19, 19, 19, '2024-05-05'),
    (20, 20, 20, '2024-05-10');

-- Insert data into the Teacher table
INSERT INTO Teacher (teacher_id, first_name, last_name, email)
VALUES
    (1, 'Professor', 'Patel', 'prof.patel@example.com'),
    (2, 'Professor', 'Johnson', 'prof.johnson@example.com'),
    (3, 'Professor', 'Sharma', 'prof.sharma@example.com'),
    (4, 'Professor', 'Williams', 'prof.williams@example.com'),
    (5, 'Professor', 'Brown', 'prof.brown@example.com'),
    (6, 'Professor', 'Miller', 'prof.miller@example.com'),
    (7, 'Professor', 'Gupta', 'prof.gupta@example.com'),
    (8, 'Professor', 'Lee', 'prof.lee@example.com'),
    (9, 'Professor', 'Anderson', 'prof.anderson@example.com'),
    (10, 'Professor', 'Thompson', 'prof.thompson@example.com'),
    (11, 'Professor', 'Jones', 'prof.jones@example.com'),
    (12, 'Professor', 'Kumar', 'prof.kumar@example.com'),
    (13, 'Professor', 'Wilson', 'prof.wilson@example.com'),
    (14, 'Professor', 'Singh', 'prof.singh@example.com'),
    (15, 'Professor', 'Smith', 'prof.smith@example.com'),
    (16, 'Professor', 'Brown', 'prof.brown@example.com'),
    (17, 'Professor', 'Williams', 'prof.williams@example.com'),
    (18, 'Professor', 'Sharma', 'prof.sharma@example.com'),
    (19, 'Professor', 'Anderson', 'prof.anderson@example.com'),
    (20, 'Professor', 'Johnson', 'prof.johnson@example.com');

-- Insert data into the Payments table
INSERT INTO Payments (payment_id, student_id, amount, payment_date)
VALUES
    (1, 1, 500.00, '2024-02-01'),
    (2, 2, 600.00, '2024-02-15'),
    (3, 3, 700.00, '2024-03-01'),
    (4, 4, 800.00, '2024-03-15'),
    (5, 5, 900.00, '2024-04-01'),
    (6, 6, 1000.00, '2024-04-15'),
    (7, 7, 1100.00, '2024-05-01'),
    (8, 8, 1200.00, '2024-05-15'),
    (9, 9, 1300.00, '2024-06-01'),
    (10, 10, 1400.00, '2024-06-15'),
    (11, 11, 1500.00, '2024-07-01'),
    (12, 12, 1600.00, '2024-07-15'),
    (13, 13, 1700.00, '2024-08-01'),
    (14, 14, 1800.00, '2024-08-15'),
    (15, 15, 1900.00, '2024-09-01'),
    (16, 16, 2000.00, '2024-09-15'),
    (17, 17, 2100.00, '2024-10-01'),
    (18, 18, 2200.00, '2024-10-15'),
    (19, 19, 2300.00, '2024-11-01'),
    (20, 20, 2400.00, '2024-11-15');

INSERT INTO Payments (payment_id, student_id, amount, payment_date)
VALUES 
	(21,16,2340.00,'2024-07-02');

SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Teacher;
SELECT * FROM Enrollments;
SELECT * FROM Payments;

-- Tasks 2: Select, Where, Between, AND, LIKE: 
-- 1. Write an SQL query to insert a new student into the "Students" table with the following details:
		-- a. First Name: John
		-- b. Last Name: Doe
		-- c. Date of Birth: 1995-08-15
		-- d. Email: john.doe@example.com
		-- e. Phone Number: 1234567890

INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number)
VALUES (21,'John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');

SELECT * FROM Students;

-- 2. Write an SQL query to enroll a student in a course. Choose an existing student and course and 
-- insert a record into the "Enrollments" table with the enrollment date.

INSERT INTO Enrollments(enrollment_id, student_id, course_id, enrollment_date)
VALUES(21,21,20,'2023-06-01');

SELECT * FROM Enrollments;

-- 3. Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and 
-- modify their email address.

UPDATE Teacher
SET email = 'professor.jones@gmail.com'
WHERE teacher_id = 11;

SELECT * FROM Teacher;

-- 4. Write an SQL query to delete a specific enrollment record from the "Enrollments" table. Select 
-- an enrollment record based on the student and course.

DELETE FROM Enrollments
WHERE student_id = 12 AND course_id = 12;

SELECT * FROM Enrollments;

-- 5. Update the "Courses" table to assign a specific teacher to a course. Choose any course and 
-- teacher from the respective tables.

UPDATE Courses
SET teacher_id = 4
WHERE course_id = 4;

SELECT * FROM Courses;

-- 6. Delete a specific student from the "Students" table and remove all their enrollment records 
-- from the "Enrollments" table. Be sure to maintain referential integrity

DELETE FROM Enrollments
WHERE student_id = 21;

DELETE FROM Students
WHERE student_id = 21;

SELECT * FROM Enrollments;
SELECT * FROM Students;

-- 7. Update the payment amount for a specific payment record in the "Payments" table. Choose any 
-- payment record and modify the payment amount.

UPDATE Payments
SET amount = 25000.00
WHERE student_id = 16;

SELECT * FROM Payments;

-- Task 3. Aggregate functions, Having, Order By, GroupBy and Joins:

-- 1. Write an SQL query to calculate the total payments made by a specific student. You will need to 
-- join the "Payments" table with the "Students" table based on the student's ID.

SELECT SUM(amount) AS Total_Amount
FROM Payments
JOIN Students
ON Payments.student_id = Students.student_id
WHERE Students.student_id = 16;

-- 2. Write an SQL query to retrieve a list of courses along with the count of students enrolled in each 
-- course. Use a JOIN operation between the "Courses" table and the "Enrollments" table.

SELECT Courses.course_id, 
       Courses.course_name, 
       COUNT(Enrollments.student_id) AS Enrollment_Count
FROM Courses
LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY Courses.course_id, Courses.course_name;

-- 3. Write an SQL query to find the names of students who have not enrolled in any course. Use a 
-- LEFT JOIN between the "Students" table and the "Enrollments" table to identify students 
-- without enrollments.

SELECT Students.first_name, 
       Students.last_name
FROM Students
LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id
WHERE Enrollments.student_id IS NULL;

-- 4. Write an SQL query to retrieve the first name, last name of students, and the names of the 
-- courses they are enrolled in. Use JOIN operations between the "Students" table and the 
-- "Enrollments" and "Courses" tables.

SELECT Students.first_name,
		Students.last_name,
		Courses.course_name
FROM Students
JOIN Courses ON Students.student_id = Courses.course_id
JOIN Enrollments ON Enrollments.course_id = Courses.course_id;

-- 5. Create a query to list the names of teachers and the courses they are assigned to. Join the 
-- "Teacher" table with the "Courses" table.

SELECT Teacher.first_name,
		Teacher.last_name,
		Courses.course_name
FROM Teacher
JOIN Courses ON Teacher.teacher_id = Courses.teacher_id;

-- 6. Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the 
-- "Students" table with the "Enrollments" and "Courses" tables.

SELECT Students.first_name,
       Students.last_name,
       Enrollments.enrollment_date,
       Courses.course_name
FROM Students
JOIN Enrollments ON Enrollments.student_id = Students.student_id
JOIN Courses ON Courses.course_id = Enrollments.course_id;

-- 7. Find the names of students who have not made any payments. Use a LEFT JOIN between the 
-- "Students" table and the "Payments" table and filter for students with NULL payment records.

SELECT Students.first_name,
		Students.last_name
FROM Students
LEFT JOIN Payments ON Payments.student_id = Students.student_id
WHERE Payments.payment_id IS NULL;

-- 8. Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN 
-- between the "Courses" table and the "Enrollments" table and filter for courses with NULL 
-- enrollment records.

SELECT Courses.course_id,
		Courses.course_name
FROM Courses
LEFT JOIN Enrollments ON Enrollments.course_id = Courses.course_id
WHERE Enrollments.enrollment_id IS NULL;
		

-- 9. Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" 
-- table to find students with multiple enrollment records.

SELECT Students.first_name,
       Students.last_name,
	   COUNT(Enrollments.enrollment_id) AS no_of_enrollments
FROM Students
JOIN Enrollments ON Students.student_id = Enrollments.student_id
GROUP BY Students.first_name, Students.last_name
HAVING COUNT(Enrollments.course_id) > 1;


-- 10. Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" 
-- table and the "Courses" table and filter for teachers with NULL course assignments.

SELECT Teacher.first_name,
		Teacher.last_name
FROM Teacher
LEFT JOIN Courses ON Courses.teacher_id = Teacher.teacher_id
WHERE Courses.teacher_id IS NULL;

-- Task 4. Subquery and its type:

-- 1. Write an SQL query to calculate the average number of students enrolled in each course. Use 
-- aggregate functions and subqueries to achieve this.

SELECT AVG(enrollment_count) AS avg_no_of_students
FROM (
    SELECT COUNT(*) AS enrollment_count
    FROM Enrollments
    GROUP BY student_id
) AS enrollment_counts;

-- 2. Identify the student(s) who made the highest payment. Use a subquery to find the maximum 
-- payment amount and then retrieve the student(s) associated with that amount.

SELECT Students.first_name,
       Students.last_name,
	   MAX(Payments.amount) AS max_payment_amount
FROM Students
JOIN Payments ON Students.student_id = Payments.student_id
GROUP BY Students.first_name, Students.last_name
HAVING MAX(Payments.amount) = (
    SELECT MAX(amount)
    FROM Payments
);

-- 3. Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the 
-- course(s) with the maximum enrollment count.

SELECT Courses.course_id,
       Courses.course_name,
       enrollment_counts.enrollment_count
FROM Courses
JOIN (
    SELECT course_id, COUNT(*) AS enrollment_count
    FROM Enrollments
    GROUP BY course_id
) AS enrollment_counts ON Courses.course_id = enrollment_counts.course_id
WHERE enrollment_counts.enrollment_count = (
    SELECT MAX(enrollment_count)
    FROM (
        SELECT COUNT(*) AS enrollment_count
        FROM Enrollments
        GROUP BY course_id
    ) AS max_enrollment_counts
);

-- 4. Calculate the total payments made to courses taught by each teacher. Use subqueries to sum 
-- payments for each teacher's courses.

SELECT Teacher.teacher_id,
       Teacher.first_name,
       Teacher.last_name,
	   Courses.course_name,
       COALESCE(SUM(Payments.amount), 0) AS total_payments
FROM Teacher
LEFT JOIN Courses ON Teacher.teacher_id = Courses.teacher_id
LEFT JOIN Payments ON Courses.course_id = Payments.student_id
GROUP BY Teacher.teacher_id, Teacher.first_name, Teacher.last_name, Courses.course_name;

-- 5. Identify students who are enrolled in all available courses. Use subqueries to compare a 
-- student's enrollments with the total number of courses.

SELECT student_id, first_name, last_name
FROM Students
WHERE (
    SELECT COUNT(DISTINCT course_id)
    FROM Enrollments
    ) = (
    SELECT COUNT(DISTINCT course_id)
    FROM Courses
    );

-- 6. Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to 
-- find teachers with no course assignments.

SELECT first_name, last_name
FROM Teacher
WHERE teacher_id NOT IN (
    SELECT DISTINCT teacher_id
    FROM Courses
);

-- 7. Calculate the average age of all students. Use subqueries to calculate the age of each student 
-- based on their date of birth.

SELECT *, DATEDIFF(YEAR, date_of_birth, GETDATE()) AS avg_age
FROM Students;

-- 8. Identify courses with no enrollments. Use subqueries to find courses without enrollment 
-- records.

SELECT *
FROM Courses
WHERE course_id NOT IN (
    SELECT DISTINCT course_id
    FROM Enrollments
);

-- 9. Calculate the total payments made by each student for each course they are enrolled in. Use 
-- subqueries and aggregate functions to sum payments.

SELECT Students.student_id,
       Students.first_name,
       Students.last_name,
       Courses.course_id,
       Courses.course_name,
       COALESCE(SUM(Payments.amount), 0) AS total_payments
FROM Students
JOIN Enrollments ON Students.student_id = Enrollments.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id
LEFT JOIN Payments ON Enrollments.student_id = Payments.student_id
GROUP BY Students.student_id, Students.first_name, Students.last_name, Courses.course_id, Courses.course_name;

-- 10. Identify students who have made more than one payment. Use subqueries and aggregate 
-- functions to count payments per student and filter for those with counts greater than one.

SELECT Students.student_id, Students.first_name, Students.last_name
FROM (
    SELECT student_id, COUNT(*) AS payment_count
    FROM Payments
    GROUP BY student_id
) AS payment_counts
JOIN Students ON Students.student_id = payment_counts.student_id
WHERE payment_counts.payment_count > 1;

-- 11. Write an SQL query to calculate the total payments made by each student. Join the "Students" 
-- table with the "Payments" table and use GROUP BY to calculate the sum of payments for each 
-- student.

SELECT Students.student_id,
       Students.first_name,
       Students.last_name,
       COALESCE(SUM(Payments.amount), 0) AS total_payments
FROM Students
LEFT JOIN Payments ON Students.student_id = Payments.student_id
GROUP BY Students.student_id, Students.first_name, Students.last_name;

-- 12. Retrieve a list of course names along with the count of students enrolled in each course. Use 
-- JOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY to 
-- count enrollments.

SELECT Courses.course_name, COUNT(Enrollments.student_id) AS enrolled_students_count
FROM Courses
LEFT JOIN Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY Courses.course_name;

-- 13. Calculate the average payment amount made by students. Use JOIN operations between the 
-- "Students" table and the "Payments" table and GROUP BY to calculate the average.

SELECT AVG(Payments.amount) AS average_payment_amount
FROM Payments
JOIN Students ON Payments.student_id = Students.student_id;








