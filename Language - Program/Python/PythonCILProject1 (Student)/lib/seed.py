from config import session
from models import Course

# data to be added to the database
COURSES = ["Biology", "Art", "Physic", "Math", "Engineer"]

# function to create course
# initialise data, creating data when starting the app
def create_course(course_list):
    for c in course_list:
        new_course = Course(title=c)
        session.add(new_course)
        session.commit()

if __name__ == "__main__":
    create_course(COURSES)
    print(f"Seeding compelte...")