#Example 1: Shallow Copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print("Original:", original)
print("Shallow:", shallow)

#Because the nested list is shared, changing it can also affect the original.

#Example 2: Deep Copy
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print("Original:", original)
print("Deep Copy:", deep)

#Here, the nested objects are copied independently.

#Example 3: zip()
names = ["Raj", "Kiran", "Arjun"]
marks = [85, 90, 78]

students = zip(names, marks)

for name, mark in students:
    print(name, mark)

'''Output:

Raj 85
Kiran 90
Arjun 78'''

#Example 4: List Input
numbers = list(map(int, input("Enter numbers: ").split()))

print("Numbers:", numbers)
print("Sum:", sum(numbers))

'''Input:

10 20 30 40 50

Output:

Numbers: [10, 20, 30, 40, 50]
Sum: 150'''

#Example 5: Dictionary Input
student = {}

n = int(input("How many details? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    student[key] = value

print("Student Details:")
print(student)