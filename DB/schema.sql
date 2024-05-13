-- Students table
CREATE TABLE Students (
  [Student_id] INT  Not Null Primary Key ,
  [first_name] Varchar(100) ,
  [last_name] Varchar(100) , 
  [date_of_birth] Date ,
  [email] Varchar (150) ,
  [phone_number] varchar(50)
  );

-- Teacher table
CREATE TABLE Teacher(
 [teacher_id] INT not null Primary Key ,
 [first_name] varchar(50) ,
 [last_name] varchar(50) ,
 [email] varchar(100)
 );

-- Courses table
CREATE TABLE Courses (
 [course_id] INT not null Primary Key ,
 [course_name] varchar(20) ,
 [credits] INT ,
 [teacher_id] INT Foreign Key References Teacher(Teacher_id)
 );

-- Enrollments table
CREATE TABLE[Enrollments] (
[enrollment_id] INT NOT NULL PRIMARY KEY,
 [student_id] INT,
 [course_id] INT,
 [enrollment_date] DATE,
 FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Payments table
CREATE Table payments(
 [payment_id] INT not null Primary Key ,
 [student_id] Int Foreign Key References Students(student_id) ,
 [amount] Deciamal(10,2) ,
 [payment_date] Date
); 

