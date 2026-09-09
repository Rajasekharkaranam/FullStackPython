

#2. Import Specific Functions
#from calculator import add, multiply

#print(add(10, 20))
#print(multiply(5, 4))

#3. Using an Alias
#import calculator as cal

#print(cal.add(10, 20))
#print(cal.multiply(5, 4))

#4. Built-in math Module
import math

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Value of Pi:", math.pi)

#Output:

#Square Root: 5.0
#Power: 8.0
#Factorial: 120
#Value of Pi: 3.141592653589793

#5. Built-in random Module
import random

print("Random Number:", random.randint(1, 100))

#6. Built-in datetime Module
import datetime

today = datetime.datetime.now()

print("Current Date and Time:", today)

#7. Built-in os Module
import os

print("Current Directory:")
print(os.getcwd())

#8. Simple User-Defined Module — Student

#student.py

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

#main.py

#import student

#student.student_details("Raj", 22, "Python")