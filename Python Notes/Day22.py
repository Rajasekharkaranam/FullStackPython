#Example: Class, Object and Variables
class Student:
    college = "ABC College"   # Class variable

    def __init__(self, name, age):
        self.name = name       # Instance variable
        self.age = age

student1 = Student("Raj", 22)
student2 = Student("Kiran", 21)

print(student1.name)
print(student1.age)
print(student1.college)

print(student2.name)
print(student2.age)