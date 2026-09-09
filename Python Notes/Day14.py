#1. Create and Call a Function
def greet():
    print("Hello! Welcome to Python Functions")

greet()

#2. Function Without Parameters
def show_message():
    print("This function has no parameters")

show_message()

#3. Function With Parameters
def greet(name):
    print("Hello", name)

greet("Raj")

#4. Parameters and Arguments
def add(a, b):  # a and b are parameters
    print("Sum =", a + b)

add(10, 20)  # 10 and 20 are arguments

#5. Function to Check Even or Odd
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check_even_odd(10)


#6. Function to Find the Largest Number
def find_largest(a, b):
    if a > b:
        print(a, "is the largest")
    else:
        print(b, "is the largest")

find_largest(25, 40)

#7. Function to Find Factorial
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial =", fact)

factorial(5)


#8. Function to Check Prime Number
def check_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")

check_prime(7)

#9. Function With a Local Variable
def student():
    name = "Raj"  # Local variable
    print("Name:", name)

student()

#Here, name can only be accessed inside the function.

#10. Function With Global and Local Scope
name = "Python"  # Global variable

def display():
    language = "Programming"  # Local variable

    print(name)
    print(language)

display()

print(name)
#11. Function With Default Parameter
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Raj")

#Output:

#Hello Guest
#Hello Raj

#12. Simple Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))