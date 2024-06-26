from util import *
from myexception.exception_handeling import InvalidEnrollmentDataException
from entity import *

class Enrollment_management:
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    #Getting the student info
    def get_student(self):
        stmt = self.conn.cursor()

        try:
            course_id = int(input("Enter the course id:"))
            stmt.execute("select first_name,last_name,course_id from students inner join enrollments on students.student_id=enrollments.student_id where enrollment_id=?"
                                , (course_id))
            print(stmt.fetchall())
            print(f"Enrolled student/students for spicified course:{course_id}")
        except Exception as e:
            raise InvalidEnrollmentDataException("Error: In retrieving the student  data".format(str(e)))

    #Getting course info                                             
    def get_course(self):
        stmt = self.conn.cursor()

        try:
            enrollment_id = int(input("Enter the enrollment id:"))
            stmt.execute("select course_name,credits,teacher_id from courses inner join enrollments on courses.course_id=enrollments.course_id where enrollment_id=?"
                                , (enrollment_id))
            print((stmt.fetchall()))
        except Exception as e:
            raise InvalidEnrollmentDataException("Error: In retrieving the course data".format(str(e)))
    