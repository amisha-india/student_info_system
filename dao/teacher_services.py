from util import *
from myexception.exception_handeling import TeacherNotFoundException
from entity import *



class Teacher_management():
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    #Displaying teacher info
    def display_teacher_info(self):
        stmt = self.conn.cursor()

        try:
            teacher_id = int(input("Enter the teacher id:"))
            stmt.execute("select * from teacher  where teacher_id=?"
                                , (teacher_id))
            print(stmt.fetchall())

        except Exception as e:
            raise TeacherNotFoundException("Error: In retrieving the teacher data".format(str(e)))  
        
    #Getting the assigned cources to teacher
    def get_assigned_courses(self):
        stmt = self.conn.cursor()

        try:
            teacher_id = int(input("Enter the teacher id:"))
            stmt.execute("select first_name,last_name,course_name from teacher inner join courses on courses.teacher_id=teacher.teacher_id where courses.teacher_id=?"
                                , (teacher_id))
            print(stmt.fetchall())

        except Exception as e:
            raise TeacherNotFoundException("Error: In retrieving the data ".format(str(e))) 
        
    #Updating the teacher 
    def update_teacher(self):
        try:
            first_name=input("Enter first name :")
            last_name=input("Enter last name :")
            email = input("Enter email :")
            teacher_id=int(input("Enter teacher id :"))
            stmt = self.conn.cursor()
            stmt.execute("UPDATE teacher SET first_name= ?, last_name= ?, email= ? WHERE teacher_id= ?",
                            (first_name,last_name,email,teacher_id))
            self.conn.commit()
            print("teacher updated successfully!")

        except Exception as e:
            raise TeacherNotFoundException("Erroe : Teacher not found".format(str(e)))   
        