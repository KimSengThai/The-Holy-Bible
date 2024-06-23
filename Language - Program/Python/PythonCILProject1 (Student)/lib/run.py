from config import session
from models import Student, Course, Enrolment
from colorama import Back, Fore, Style
import os #command line system

# Command line to clear, posix for linux or mac and the rest is window
def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('nt')       

# Start menu function
def main_men():
    print(f"⭐"*20)
    print("MENU OPTIONS:")
    print(f"⭐"*20)

    print(Back.GREEN + "add" + Style.RESET_ALL + "\t\tAdd a new student to the app")   
    print(Back.GREEN + "students" + Style.RESET_ALL + "\tDisplay all students")  
    print(Back.GREEN + "courses" + Style.RESET_ALL + "\t\tDisplay a student to a course")
    print(Back.RED + "quit/exit" + Style.RESET_ALL + "\tExit this program")

    print(f"="*40)  

# Function for adding student
def add_student():
    loop = True

    while loop:
        clear()

        print("-"*30)
        print("ADD STUDENT")
        print("-"*30)

        print("\nPlease enter the student\'s name:")
        name = input()
        print("\nPlease enter the student\'s degree:")
        degree = input()

        new_student = Student(name=name, degree=degree)
        session.add(new_student)
        session.commit()

        print(Fore.GREEN + f"\n{new_student.name}" + Style.RESET_ALL + " is successfully added!")

        while True:
            print("\nDo you want to add another student (yes/no)?")
            choice = input()

            if choice.lower() == "yes":
                break
            elif choice.lower() == "no":
                loop = False
                clear()
                break
            else:
                print(Fore.RED + "Invalid Input!" + Style.RESET_ALL)

def display_students():
    clear()
    loop = True

    while loop:
        print("-"*30)
        print("STUDENTS")
        print("-"*30)
        
        students = session.query(Student).all()

        # print(f"ID\tNAME\t\tDEGREE")
        for student in students:
            print(student)

        student_loop = True
        while student_loop:
            print("\nEnter the student's ID to view student's enrolment:")
            student_id = int( input())
            student = session.query(Student).filter(Student.id == student_id).first()
            
            if student:
                if (len(student.courses)) > 0:
                    print(f"{student.name}'s enrolled courses:")

                    count = 1
                    for course in student.courses:
                        print(f"{count}. {course.title}")
                        count = count + 1
                else:
                    print(f"{student.name} is not enrolled in any course")
            else:
                print(Fore.RED + f"No student hfound with the id {student_id}")

            while True:
                print("\nDo you want to add another student (yes/no)?")
                choice = input()

                if choice.lower() == "yes":
                    break
                elif choice.lower() == "no":
                    loop = False
                    student_loop = False                    
                    clear()
                    break
                else:
                    print(Fore.RED + "Invalid Input!" + Style.RESET_ALL)   

def enrol_student():
    print("-"*30)
    print("STUDENTS")
    print("-"*30)

    courses = session.query(Course).all()
    for c in courses:
        print(c)

    print("\nPlease enter the course ID where you want to add a student:")
    course_id = int(input())
    course = session.query(Course).filter(Course.id==course_id).first()

    if course:
        print("\nPlease enter the student's ID to enrol:")
        student_id = int(input())
        new_enrolment = Enrolment(course_id=course.id, student_id=student_id)
        session.add(new_enrolment)
        session.commit()
        print(f"{new_enrolment}")
    else:
        print("Invalid course ID!")

# looping when user select options
def start():
    app_loop = True

    while app_loop:
        main_men() 
        option_loop = True
        while option_loop:
            print("Please select an option")
            choice = input()

            if choice.lower() == "add":
                option_loop = False
                add_student()
            elif choice.lower() == "students":
                option_loop = False
                display_students()
            elif choice.lower() == "courses":
                option_loop = False
                enrol_student()
            elif choice.lower() == "quit" or choice.lower() == "exit":
                app_loop = False
                option_loop = False
            else:
                print(Fore.RED + "Invalid Input!" + Style.RESET_ALL)

    print(Back.RED + "Thank you for using the app" + Style.RESET_ALL)        

def greet():
    clear()
    print(Back.YELLOW + "Welcome to the School Mgt App!" + Style.RESET_ALL)

if __name__ == "__main__":
    greet()
    start()
