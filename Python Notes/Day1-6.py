# Student Details Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))

skills = {"Python", "HTML", "CSS"}

student = {
    "name": name,
    "age": age,
    "skills": skills
}

print("\n--- Student Details ---")
print(f"Name   : {student['name']}")
print(f"Age    : {student['age']}")
print(f"Skills : {student['skills']}")