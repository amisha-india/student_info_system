# Creating all the course related services(CRUD) at same place (encapsulation)

from util.myDBconnection import DBConnection
class Course_services(DBConnection):

    def AssignTeacher(self,course,teacher_id):
        pass
    
    def UpdateCourseInfo(self, Course):
        pass

    def DisplayCourseInfo(self):
        pass

    def GetEnrollments(self, course_id):
       pass

    def GetTeacher(self, course_id):
       pass 

    def CreateCourse(self, Course):
        pass