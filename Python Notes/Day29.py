#Example 1: try and except
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter numbers only.")
#Example 2: try, except, else, finally
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")
#Example 3: Raising an Exception
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("Eligible")