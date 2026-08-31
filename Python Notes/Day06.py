# Taking Input
name = input("Enter your name: ")

print("Hello", name)

#Example:

#Enter your name: Raj
#Hello Raj

 #Input with Type Casting

#Remember that input() normally returns a string, so we can convert it:

age = int(input("Enter your age: "))

print("Your age is", age)

#Output Formatting using f-strings
name = "Raj"
age = 22
course = "Python Full Stack"
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I am learning {course}")