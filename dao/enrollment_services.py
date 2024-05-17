from util import *
from myexception.exception_handeling import InvalidEnrollmentDataException
from entity import *

class Enrollment_management:
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    #Getting the student info
    def get_student(self):
        try:
            enrollment_id = int(input("Enter the enrollment id:"))
            self.cursor.execute("select first_name,last_name,course_id from students inner join enrollments on students.student_id=enrollments.student_id where enrollment_id=?"
                                , (enrollment_id))
            print(self.cursor.fetchall())
        except Exception as e:
            self.connection.rollback()
            raise InvalidEnrollmentDataException("Error: In retrieving the student  data".format(str(e)))

    #Getting course info                                             
    def get_course(self):
        try:
            enrollment_id = int(input("Enter the enrollment id:"))
            self.cursor.execute("select course_name,credits,teacher_id from courses inner join enrollments on courses.course_id=enrollments.course_id where enrollment_id=?"
                                , (enrollment_id))
            print((self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise InvalidEnrollmentDataException("Error: In retrieving the course data".format(str(e)))
    