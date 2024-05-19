from dao import *
from myexception.exception_handeling import *
from util import *
from entity import *
from datetime import date

print("...Welcome to the student information system....")

student = Student_management()  
course = Course_management()  
enrollment = Enrollment_management()  
teacher = Teacher_management()  
payment = Payment_management()  
sis = SIS_management()  

while True:
            print("\nMain Menu:")
            print("1. Student Operations")
            print("2. Course Operations")
            print("3. Enrollment Operations")
            print("4. Teacher Operations")
            print("5. Payment Operations")
            print("6. SIS Operations")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")
        
            if choice == '1':
                while True:
                        print("\nStudent Operations:")
                        print("1. Enroll in Course")
                        print("2. Update Student Info")
                        print("3. Make Payment")
                        print("4. Display Student Info")
                        print("5. Get Enrolled Courses")
                        print("6. Get Payment History")
                        print("7. Back to Main Menu")
                        student_choice = input("Enter your choice (1-7): ")
                        if student_choice == '1':
                            student.enroll_in_course()
                        elif student_choice == '2':
                            student.update_student()
                        elif student_choice == '3':
                            student.make_payment()
                        elif student_choice == '4':
                            student.display_student_info()
                        elif student_choice == '5':
                            student.get_enrolled_courses()
                        elif student_choice == '6':
                            student.get_payment_history()
                        elif student_choice == '7':
                            break
                        else:
                            print("Invalid choice. Please try again.")
            
            elif choice == '2':
                while True:
                    print("\nCourse Operations:")
                    print("1. Assign Teacher")
                    print("2. Update Course Info")
                    print("3. Display Course Info")
                    print("4. Get Enrollments")
                    print("5. Get Teacher")
                    print("6. Back to Main Menu")
                    course_choice = input("Enter your choice (1-6): ")
                    if course_choice == '1':
                        course.assign_teacher()
                    elif course_choice == '2':
                        course.update_course_info()
                    elif course_choice == '3':
                        course.display_course_info()
                    elif course_choice == '4':
                        course.get_enrollments()
                    elif course_choice == '5':
                        course.get_teacher()
                    elif course_choice == '6':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
            elif choice == '3':
                while True:
                    print("\nEnrollment Operations:")
                    print("1. Get Student")
                    print("2. Get Course")
                    print("3. Back to Main Menu")
                    enrollment_choice = input("Enter your choice (1-3): ")
                    if enrollment_choice == '1':
                        enrollment.get_student()
                    elif enrollment_choice == '2':
                        enrollment.get_course()
                    elif enrollment_choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
            elif choice == '4':
                while True:
                    print("\nTeacher Operations:")
                    print("1. Update Teacher Info")
                    print("2. Display Teacher Info")
                    print("3. Get Assigned Courses")
                    print("4. Back to Main Menu")
                    teacher_choice = input("Enter your choice (1-4): ")
                    if teacher_choice == '1':
                        teacher.update_teacher()
                    elif teacher_choice == '2':
                        teacher.display_teacher_info()
                    elif teacher_choice == '3':
                        teacher.get_assigned_courses()
                    elif teacher_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
            elif choice == '5':
                while True:
                    print("\nPayment Operations:")
                    print("1. Get Student")
                    print("2. Get Payment Amount")
                    print("3. Get Payment Date")
                    print("4. Back to Main Menu")
                    payment_choice = input("Enter your choice (1-4): ")
                    if payment_choice == '1':
                        payment.get_student()
                    elif payment_choice == '2':
                        payment.get_payment_amount()
                    elif payment_choice == '3':
                        payment.get_payment_date()
                    elif payment_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
            elif choice == '6':
                while True:
                    print("\nSIS Operations:")
                    print("1. Enroll Student in Course")
                    print("2. Assign Teacher to Course")
                    print("3. Record Payment")
                    print("4. Generate Enrollment Report")
                    print("5. Generate Payment Report")
                    print("6. Calculate Course Statistics")
                    print("7. Back to Main Menu")
                    sis_choice = input("Enter your choice (1-7): ")
                    if sis_choice == '1':
                        sis.enroll_in_course()
                    elif sis_choice == '2':
                        sis.assign_teacher()
                    elif sis_choice == '3':
                        sis.get_payment_amount()
                    elif sis_choice == '4':
                        sis.get_enrollments()
                    elif sis_choice == '5':
                        sis.get_payment_history()
                    elif sis_choice == '6':
                        sis.calculate_course_statistics()
                    elif sis_choice == '7':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
            elif choice == '7':
                print("Exiting the program!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    print("Good day😊😊")    







    

    