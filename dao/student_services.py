from util import *
from myexception.exception_handeling import *
from entity.student import Student
from datetime import date

class Student_management:
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    #Getting the student info with student id    
    def get_student_id(self):
        try:
            student_id = int(input("Enter student_id: "))
            print("Searching for student with ID:", student_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                print("Student found:", row)
                student = Student(*row)
                return student
            else:
                raise StudentNotFoundException(f"No student found with ID: {student_id}")

        except StudentNotFoundException as e:
            raise e
        except Exception as e:
            print("Error in retrieving student:", e)
            return None
        
    #Adding new student        
    def add_student(self):

        student_id = int(input("Enter the student id:"))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")

        if not student_id or not first_name or not last_name or not date_of_birth or not email or not phone_number:
            raise InvalidStudentDataException("Please fill properly.")
        
        date_of_birth = str(date_of_birth)
        phone_number = str(phone_number)

        stmt = self.conn.cursor()
        stmt.execute(
            "INSERT INTO students (student_id,first_name, last_name, date_of_birth, email, phone_number) VALUES (?,?,?,?,?,?)",
            (student_id,first_name, last_name, date_of_birth, email, phone_number))
        self.conn.commit()
        print("student added successfully!")
    
    #Updating the student information
    def update_student(self):

        student_id = input("Enter the student ID : ")
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ")
        email = input("Enter the email: ")
        phone_number = input("Enter the phone number: ")
        date_of_birth = str(date_of_birth)
        phone_number = str(phone_number)
        stmt = self.conn.cursor()
        stmt.execute(
            "UPDATE students SET first_name=?, last_name=?, date_of_birth=?, email=?, phone_number=? WHERE student_id=?",
            (first_name, last_name, date_of_birth, email, phone_number, student_id))
        self.conn.commit()
        print("student updated successfully!")

    #Enrolling student in a course 
    def enroll_in_course(self):
        try:
            student_id = int(input("Enter the student id:"))
            course_id = int(input("Enter the course id:"))
            enrollment_date = input("Enter enrollment date :")
            enrollment_id = int(input("Enter the enrollment id:"))
            if not student_id or not course_id or not enrollment_id or not enrollment_date:
                raise InvalidEnrollmentDataException("Enrollment date is required.")
            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM enrollments WHERE student_id = ? AND course_id = ?", (student_id, course_id))
            existing = stmt.fetchone()
            if existing:
                raise DuplicateEnrollmentException("Student is already enrolled in the course.")

            stmt.execute("INSERT INTO enrollments (student_id, course_id, enrollment_date,enrollment_id) VALUES (?,?,?,?)",
                     (student_id,course_id,enrollment_date,enrollment_id))
            self.conn.commit()
            print("enrollment added successfully!")
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException(f"No such data found with ID: {enrollment_id}")
        
    #Making payment for the student    
    def make_payment(self,student_id,amount):
        try:
            self.cursor.execute("select payment_id from payments order by payment_id desc offset 0 rows fetch next 1 rows only")
            payment_id=self.cursor.fetchone()
            self.cursor.execute("INSERT INTO payments VALUES (?, ?, ?, GETDATE())", (payment_id[0] + 1, student_id, amount))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: {}".format(str(e)))
        
    #display student info
    def display_student_info(self):
        try:
            student_id = int(input("Enter student_id: "))
            print("Searching for student with ID:", student_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                print("Student found:", row)
                student = Student(*row)
                return student
            else:
                raise StudentNotFoundException(f"No student found with ID: {student_id}")

        except StudentNotFoundException as e:
            raise e
        except Exception as e:
            print("Error retrieving student:", e)
            return None
        
    #Getting the enrolled courses
    def get_enrolled_courses(self):
        try:
            student_id = int(input("Enter the student id:"))
            self.cursor.execute("select students.student_id,first_name,last_name,course_name from students inner join enrollments  on students.student_id=enrollments.student_id inner join courses on courses.course_id=enrollments.course_id where students.student_id=?"
                                , (student_id))
            print((self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error student not found".format(str(e)))
        
    #Getting payment History
    def get_payment_history(self):
        try:
            student_id = int(input("Enter the student id:"))
            self.cursor.execute("Select * from payments where student_id=?"
                                , (student_id))
            print(self.cursor.fetchall())
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: in reteriving the student ".format(str(e)))
    
    #Getting the enrollement
    def get_enrollment(self):
        enrollment_id = int(input("Enter enrollment id :"))
        stmt = self.conn.cursor()
        stmt.execute("SELECT * FROM enrollments WHERE enrollment_id= ?", (enrollment_id,))
        row = stmt.fetchone()
        if row:
            enrollment_id,student_id,course_id,enrollment_date = row
            print(f"enrollment ID: {enrollment_id}")
            print(f"course ID: {course_id}")
            print(f"student ID: {student_id}")
            print(f"enrollment date: {enrollment_date}")
            print("enrollment details retrieved successfully!")
        else:
            print("No course found with ID:", enrollment_id)
            return None
        
    