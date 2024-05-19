
from util import *
from myexception.exception_handeling import *
from entity.course import Course

    
class Course_management():
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    #Assign teacher to course based on course_id
    def assign_teacher(self):
        stmt = self.conn.cursor()

        try:
            course_id = int(input("Enter the course id:"))
            teahcer_id = int(input("Enter the teacher id:"))
            stmt.execute("UPDATE Courses SET teacher_id=? WHERE course_id = ?"
                                , (teahcer_id, course_id))
            self.conn.commit()
        except Exception as e:
            raise StudentNotFoundException(f"Error the student not found with given :{course_id}")
    
    #update course info based on course_id
    def update_course_info(self):

        try:
            course_id = int(input("Enter course_id :"))
            course_name = input("Enter course name :")
            course_code = input("Enter the course code:")
            credits = int(input("Enter credits :"))
            teacher_id = int(input("Enter teacher_id :"))
            stmt = self.conn.cursor()
            stmt.execute("UPDATE courses SET course_name=?,course_code=?, teacher_id=?, credits=? WHERE course_id=?",
                     (course_name,course_code,teacher_id,credits,course_id))
            self.conn.commit()
            print("course updated successfully!")
        except Exception as e:
            raise  CourseNotFoundException(f"No such course found with ID: {course_id}")

    #Dispaying the course information based on course_id
    def display_course_info(self):
        try:
            course_id = int(input("Enter course_id: "))
            print("Finding for course with ID:", course_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM courses WHERE course_id = ?", (course_id,))
            print("SQL query executed successfully")

            row = stmt.fetchone()
            if row:
                course_id, course_name,course_code, credits,teacher_id =row
                print(f"Course ID: {course_id}")
                print(f"Course Name: {course_name}")
                print(f"Course Code: {course_code}")
                print(f"credits: {credits}")
                print(f"teacher_id: {teacher_id}")
                print("course details retrieved successfully!")
            else:
                raise CourseNotFoundException(f"No course found with ID: {course_id}")
            
        except CourseNotFoundException as e:
            raise e

        except Exception as e:
            print("Error in retrieving course:", e)
            return None

    #Getting the enrollments based on course_id
    def get_enrollments(self):
        try:
            course_id = int(input("Enter course_id: "))
            print("Finding for enrollments with ID:", course_id)

            stmt = self.conn.cursor()
            stmt.execute("SELECT * FROM enrollments WHERE course_id = ?", (course_id,))
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

    #Getting Teacher info based on course id
    def get_teacher(self):
        try:
            course_id = int(input("Enter course id :"))
            self.cursor.execute("select first_name,last_name,course_name from teacher inner join courses on courses.teacher_id=teacher.teacher_id where course_id=?"
                                , (course_id))
            print(self.cursor.fetchall())
        except Exception as e:
            raise CourseNotFoundException(f"No such course found with ID: {course_id}")
      

    