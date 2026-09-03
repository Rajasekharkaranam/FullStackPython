# Day 10 - Control Statements and Conditional Statements


# 1. Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 2. Exam Result
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Result: Fail")


# 3. ATM Withdrawal
balance = 10000

amount = int(input("\nEnter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount <= balance:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient balance")


# 4. Movie Ticket Price
age = int(input("\nEnter your age: "))

if age < 5:
    print("Ticket is Free")
elif age <= 12:
    print("Ticket Price: ₹100")
elif age <= 59:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹120")


# 5. Login Check
correct_username = "admin"
correct_password = "1234"

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid username or password")