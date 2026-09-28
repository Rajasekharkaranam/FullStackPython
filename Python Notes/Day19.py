#Example 1: User-Defined Module

'''calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b'''

#main.py
'''
import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))'''

'''Output:

Addition: 15
Subtraction: 5
Multiplication: 50'''

#Example 2: Built-in math Module
import math

number = 25

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
 
 #💻 Example 3: Built-in random Module
import random

print("Random number:", random.randint(1, 100))

numbers = [10, 20, 30, 40, 50]
print("Random choice:", random.choice(numbers))
#💻 Example 4: Built-in datetime Module
from datetime import datetime

current_time = datetime.now()

print("Current Date and Time:", current_time)
print("Date:", current_time.date())
print("Time:", current_time.time())
#💻 Example 5: Built-in os Module
import os

print("Current Directory:", os.getcwd())

print("Files and Folders:")
print(os.listdir())