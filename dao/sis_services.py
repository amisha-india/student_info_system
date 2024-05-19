from util import *
from myexception.exception_handeling import *
from entity import *

class SIS_management():
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

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
            raise StudentNotFoundException(f"No such data found with ID: {enrollment_id}")
        
    def assign_teacher(self):
        try:
            course_id = int(input("Enter the course id:"))
            teahcer_id = int(input("Enter the teacher id:"))
            self.cursor.execute("UPDATE Courses SET teacher_id=? WHERE course_id = ?"
                                , (teahcer_id, course_id))
            self.connection.commit()
        except Exception as e:
            raise StudentNotFoundException(f"Error the student not found with given :{course_id}")

    #Get payment record
    def get_payment_amount(self):
        try:
            student_id = int(input("Enter the student id:"))
            self.cursor.execute(
                "select amount from Payments  inner join students on Payments.student_id=students.student_id where students.student_id=?;",
                (student_id),
            )
            print(self.cursor.fetchall())
        except Exception as e:
            raise PaymentValidationException(
                "Error: In retrieve the data".format(str(e))
            )
        
    #generate enrollement record
    def get_enrollments(self):
        try:
            course_id = int(input("Enter course_id: "))
            print("Finding for enrollments with ID:", course_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM enrollment WHERE course_id = ?", (course_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                enrollment_id, student_id, course_id, enrollment_date =row
                print(f"Enrollment Id: {enrollment_id}")
                print(f"Student Id: {student_id}")
                print(f"Course Id: {course_id}")
                print(f"Enrollment Date: {enrollment_date}")
                print("Enrollment details retrieved successfully!")
            else:
                print("No course found with ID:", enrollment_id)
                return None
            
        except CourseNotFoundException as e:
            raise e

        except Exception as e:
            print("Error in retrieving Enrollment:", e)
            return None
        
    #generate payment report
    def get_payment_history(self):
        try:
            student_id = int(input("Enter the student id:"))
            self.cursor.execute("Select * from payments where student_id=?"
                                , (student_id))
            print(self.cursor.fetchall())
        except Exception as e:
            raise StudentNotFoundException("Error: in reteriving the student ".format(str(e)))
        
    def calculate_course_statistics(self):
        course_id = input("Enter Course ID: ")
        course = Course(course_id)
        stats =SIS_management.calculate_course_statistics(course)
        print(f"Statistics for course {course_id}:")
        print(stats)
        
             

        
    
        