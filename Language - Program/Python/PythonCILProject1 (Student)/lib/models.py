from sqlalchemy import Column, String, Integer, ForeignKey          #table database attribute
from sqlalchemy.orm import declarative_base, relationship           #create base class and relationship between tables
from sqlalchemy.ext.associationproxy import association_proxy       #

Base = declarative_base()           #base class from which all ORM models will inherit, parent

class Student(Base):                
    __tablename__ = "students"      #name of the table

    #query create table column
    id = Column(Integer, primary_key=True)      #column of table = attribute of each column
    name = Column(String, nullable=False)
    degree = Column(String)

    #reference to other table 
    # enrolements and courses (=) are Student class attribute
    # relationship(A,B) = function to define relationship between databases table. Student can have many Enrolment
    # A = name of the related class 'Enrolment'. Define as 1 to many relationship. 
    # back_populates='student': Indicates that Enrolment has a reciprocal attribute named student that references back to Student.
    # association_proxy allow you to create a proxy for indirect associations. Access course through enrolments
    # enrolments = refer to Student attribute 
    # creator=lambda c: Enrolment(course=c)) = hdefines how to create Enrolement object. DOing this allow you to access from student to course without having to manually navigate through Enrolment objects.
    enrolments = relationship('Enrolment', back_populates='student')    
    courses = association_proxy('enrolments', 'course', creator=lambda c: Enrolment(course=c))  #

    # __repr__: A special method that returns a string representation of a Student object, useful for debugging and logging.
    def __repr__(self):
        return f"{self.id}: {self.name} - {self.degree}"
    
class Course(Base):
    __tablename__ = "courses"

    #query create table column
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    #reference to other table
    enrolments = relationship('Enrolment', back_populates='course')
    students = association_proxy('enrolments', 'student', creator=lambda s: Enrolment(student=s))
    
    def __repr__(self):
        return f"{self.id}: {self.title}"

class Enrolment(Base):
    __tablename__ = "enrolments"

    #query create table column
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))       #foreign key to courses table
    student_id = Column(Integer, ForeignKey('students.id'))     #foreign key to student table
    
    #reference to other table
    course = relationship('Course', back_populates='enrolments')
    student = relationship('Student', back_populates='enrolments')

    def __repr__(self):
        return f"{self.student.name} is enrolled in {self.course.title}"


