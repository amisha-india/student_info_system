# Creating all the teacher related services(CRUD) at same place (encapsulation)

class SIS:

    def EnrollStudent(self, student, course):
        pass

    def AssignTeacherToCourse(self, course, teacher):
        pass

    def RecordPayment(self, student, amount, paymentDate):
        pass

    def GenerateEnrollmentReport(self, course):
        pass

    def GeneratePaymentReport(self, student):
        pass
