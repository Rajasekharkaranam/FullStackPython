#Example 1: File Handling
# Writing to a file
file = open("student.txt", "w")
file.write("Name: Raj\n")
file.write("Course: Python Full Stack\n")
file.close()

# Reading the file
file = open("student.txt", "r")
print(file.read())
file.close()

# Appending data
file = open("student.txt", "a")
file.write("Learning Python OOPs\n")
file.close()

#Example 2: Using with open()
with open("data.txt", "w") as file:
    file.write("Python Full Stack Journey")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

#Example 3: Sending Email using smtplib
import smtplib

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password"

message = """Subject: Python Learning

Hello,
This email was sent using Python.
"""

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

print("Email sent successfully!")