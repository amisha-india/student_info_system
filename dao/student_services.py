# Creating all the student related services(CRUD) at same place (encapsulation)

from util.myDBconnection import DBConnection
class Student_services(DBConnection):

    def EnrollInCourse(self, enrollments):
        pass

    def UpdateStudentInfo(self, Student):
        pass

    def MakePayment(self, Payment):
        pass

    def DisplayStudentInfo(self, student_id):
        pass

    def GetEnrolledCourses(self, student_id):
        pass

    def GetPaymentHistory(self, student_id):
        pass

    def CreateStudent(self, Student):
        pass

    def GetStudent(self, student_id):
        pass
