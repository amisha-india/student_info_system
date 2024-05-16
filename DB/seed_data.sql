--Inseting into students table
INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number)
VALUES
(1, 'Nura', 'Das', '2000-01-15', 'nura.das@example.com', '193-756-4453'),
(2, 'Jane', 'Smith', '1998-05-20', 'jane.smith@example.com', '234-567-8901'),
(3, 'Sam', 'Williams', '2001-03-12', 'sam.williams@example.com', '345-678-9012'),
(4, 'Emily', 'Johnson', '1999-11-25', 'emily.johnson@example.com', '456-789-0123'),
(5, 'Michael', 'Brown', '2000-07-30', 'michael.brown@example.com', '567-890-1234'),
(6, 'Olivia', 'Davis', '1997-09-10', 'olivia.davis@example.com', '678-901-2345'),
(7, 'Liam', 'Miller', '1998-12-01', 'liam.miller@example.com', '789-012-3456'),
(8, 'Sophia', 'Wilson', '2001-06-18', 'sophia.wilson@example.com', '890-123-4567'),
(9, 'Jacob', 'Taylor', '1999-02-22', 'jacob.taylor@example.com', '901-234-5678'),
(10, 'Mia', 'Anderson', '2000-04-05', 'mia.anderson@example.com', '012-345-6789');

--Inserting into teachers table
INSERT INTO Teacher (teacher_id, first_name, last_name, email)
VALUES
(1, 'Sarah', 'Connor', 'sarah.connor@example.com'),
(2, 'James', 'Clark', 'james.clark@example.com'),
(3, 'Laura', 'Lewis', 'laura.lewis@example.com'),
(4, 'Chris', 'Walker', 'chris.walker@example.com'),
(5, 'Emma', 'White', 'emma.white@example.com'),
(6, 'Daniel', 'Hall', 'daniel.hall@example.com'),
(7, 'Grace', 'King', 'grace.king@example.com'),
(8, 'Matthew', 'Green', 'matthew.green@example.com'),
(9, 'Lucas', 'Baker', 'lucas.baker@example.com'),
(10, 'Chloe', 'Campbell', 'chloe.campbell@example.com'),
(11,'Rakul','Kushar','rakul.kushar@example.com');

--Inserting into Courses table
INSERT INTO Courses (course_id, course_name,course_code, credits, teacher_id)
VALUES
(1, 'Mathematics 101', 3, 1),
(2, 'Physics 101', 4, 2),
(3, 'Chemistry 101', 4, 3),
(4, 'Biology 101', 3, 4),
(5, 'English 101', 3, 5),
(6, 'History 101', 3, 6),
(7, 'Geography 101', 3, 7),
(8, 'Art 101', 2, 8),
(9, 'Music 101', 2, 9),
(10, 'Computer Science 101', 3, 11);

--Inserting into Enrollment table
INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date)
VALUES
(1, 1, 1, '2023-01-10'),
(2, 2, 9, '2023-01-11'),
(3, 3, 3, '2023-01-12'),
(4, 4, 4, '2023-01-13'),
(5, 5, 9, '2023-01-14'),
(6, 2, 6, '2023-01-15'),
(7, 7, 7, '2023-01-16'),
(8, 8, 8, '2023-01-17'),
(9, 9, 9, '2023-01-18'),
(10, 10, 3, '2023-01-19'),
(12,11 , 9, '2023-01-20'),
(13,4,7,'2023-04-05'),
(14,7,4,'2023-04-13');

--Inserting into Payments
INSERT INTO Payments (payment_id, student_id, amount, payment_date)
VALUES
(1, 1, 300.00, '2023-01-25'),
(2, 2, 400.00, '2023-01-26'),
(3, 8, 400.00, '2023-01-27'),
(4, 4, 300.00, '2023-01-28'),
(5, 5, 300.00, '2023-01-29'),
(6, 2, 300.00, '2023-01-30'),
(7, 7, 300.00, '2023-01-31'),
(8, 8, 200.00, '2023-02-01'),
(9, 9, 200.00, '2023-02-02'),
(10, 10, 100.00, '2023-02-03'),
(11, 8, 500.00, '2023-03-08');
