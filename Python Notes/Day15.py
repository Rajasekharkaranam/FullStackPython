#1. Scope of Variables
x = 10  # Global variable

def display():
    y = 20  # Local variable
    print("Inside function:", x)
    print("Local variable:", y)

display()

print("Global variable:", x)

#2. LEGB Rule

#LEGB = Local → Enclosing → Global → Built-in

x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()

#Output:

#Local

#3. Global Variable
number = 10

def change_number():
    global number
    number = 50

print("Before:", number)

change_number()

print("After:", number)

#4. Call by Value – Immutable Example

#Python uses object references rather than traditional C-style "call by value/reference." With immutable objects such as integers, changing the parameter doesn't change the original variable.

def change_value(x):
    x = 100
    print("Inside function:", x)

num = 10

change_value(num)

print("Outside function:", num)

#Output:

#Inside function: 100
#Outside function: 10

#5. Mutable Object Example

#Lists can be modified inside a function because both references point to the same list object.

def add_item(numbers):
    numbers.append(40)

my_list = [10, 20, 30]

add_item(my_list)

print(my_list)

#Output:

#[10, 20, 30, 40]

#6. Recursive Function – Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#Output:

#120

#7. Recursive Function – Sum of Numbers

def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

#Output:

#15

#8. Lambda Function

#A lambda is a small anonymous function.

square = lambda x: x * x

print(square(5))

#Output:

#25

#9. Lambda With Two Arguments
add = lambda a, b: a + b

print(add(10, 20))

#Output:

#30

#10. Map Function

#map() applies a function to every item in an iterable.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

#Output:

#[1, 4, 9, 16, 25]

#11. Map to Double Numbers
numbers = [10, 20, 30, 40]

result = list(map(lambda x: x * 2, numbers))

print(result)

#Output:

#[20, 40, 60, 80]

#12. Map With a Normal Function
def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4]

result = list(map(cube, numbers))

print(result)

#Output:

#[1, 8, 27, 64]