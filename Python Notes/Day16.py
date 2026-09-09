#1. Recursive Function – Simple Example
def count_down(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    count_down(n - 1)


count_down(5)

#5. Pass by Value – Immutable Object

#Python technically uses pass-by-object-reference (also called pass-by-assignment), rather than traditional C-style pass-by-value.

#With an immutable integer:

def change_value(x):
    x = 100
    print("Inside function:", x)


num = 10

change_value(num)

print("Outside function:", num)

#6. Pass by Reference – Mutable Object

#With a mutable list, the function can modify the same list object:

def add_number(numbers):
    numbers.append(50)


my_list = [10, 20, 30]

add_number(my_list)

print(my_list)

# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Sum of Natural Numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


print("Factorial:", factorial(5))

print("Fibonacci Series:")
for i in range(7):
    print(fibonacci(i), end=" ")

print("\nSum of Natural Numbers:", sum_natural(10))