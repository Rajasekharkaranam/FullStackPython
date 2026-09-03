# Day 11 - For Loop with Else and While Loop with Else


# 1. Search for a product
products = ["Laptop", "Mobile", "Tablet", "Headphones"]

search = input("Enter product to search: ")

for product in products:
    if product.lower() == search.lower():
        print("Product found!")
        break
else:
    print("Product not found.")


# 2. Search for a student
students = ["Rahul", "Priya", "Arjun", "Sneha"]

name = input("\nEnter student name: ")

for student in students:
    if student.lower() == name.lower():
        print("Student found.")
        break
else:
    print("Student not found.")


# 3. ATM PIN verification
correct_pin = 1234
attempts = 3

while attempts > 0:
    pin = int(input("\nEnter ATM PIN: "))

    if pin == correct_pin:
        print("PIN correct. Access granted.")
        break

    attempts -= 1
    print("Incorrect PIN.")
else:
    print("Account temporarily locked.")


# 4. Find a number in a list
numbers = [10, 20, 30, 40, 50]

search_number = int(input("\nEnter number to search: "))

for number in numbers:
    if number == search_number:
        print("Number found.")
        break
else:
    print("Number not found.")