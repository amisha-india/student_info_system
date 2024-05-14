# Creating all the teacher related services(CRUD) at same place (encapsulation)

from util.myDBconnection import DBConnection
class Teacher_services(DBConnection):

    def UpdateTeacherInfo(self, teacher_id):
        pass

    def DisplayTeacherInfo(self, teacher_id):
        pass

    def GetAssignedCourses(self, teacher_id):
        pass
