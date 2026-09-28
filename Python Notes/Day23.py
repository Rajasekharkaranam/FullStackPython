#Example: Types of Methods
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display(self):
        print("Name:", self.name)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to Python OOP!")


student = Student("Raj")

student.display()
Student.show_college()
Student.welcome()