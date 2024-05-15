# Course class with its attributes

class Course:

    def __init__(self, course_id, course_name, credit, teacher_id):

        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.teacher_id = teacher_id

        self.enrollments = []

    #Getters
    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    #Setters
    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_course_name(self, course_name):
        self.__course_name = course_name