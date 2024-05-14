# Creating all the teacher related services(CRUD) at same place (encapsulation)

from util.myDBconnection import DBConnection
class SIS(DBConnection):

    def EnrollStudentInCourse(self, student, course):
        pass

    def AssignTeacherToCourse(self, course, teacher):
        pass

    def RecordPayment(self, student, amount, paymentDate):
        pass

    def GenerateEnrollmentReport(self, course):
        pass

    def GeneratePaymentReport(self, student):
        pass

    def CalculateCourseStatistics(self,course):
        pass

    def AddEnrollment(self,student_id, course,enrollment_date):
        pass

    def AddPayment(self,student_id, amount, payment_date):
        pass

    def AssignCourseToTeacher(self,course, teacher_id):
        pass

    def GetEnrollmentsForStudent(self,student_id):
        pass

    def GetCoursesForTeacher(self,teacher_id):
        pass


