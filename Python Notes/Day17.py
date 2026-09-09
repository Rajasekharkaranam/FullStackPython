#1. Create a List Using List Comprehension
from ast import List


numbers = [x for x in range(1, 11)]

print(numbers)

#Output:

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#2. Square of Numbers
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

#Output:

#[1, 4, 9, 16, 25]

#3. Even Numbers Using List Comprehension
numbers = range(1, 11)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

#Output:

#[2, 4, 6, 8, 10]

#4. List Comprehension with Strings
names = ["raj", "python", "codegnan"]

upper_names = [name.upper() for name in names]

print(upper_names)

#Output:

#['RAJ', 'PYTHON', 'CODEGNAN']

#5. List Comprehension with Multiple Data Types
data = [10, "Python", 20, "Codegnan", 30]

strings = [x for x in data if isinstance(x, str)]

print(strings)

#Output:

#['Python', 'Codegnan']

#6. Nested List Comprehension

#A nested list comprehension can be used to flatten a nested list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [num for row in matrix for num in row]

print(result)

#Output:

#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#7. Nested List Comprehension – Matrix
matrix = [[i * j for j in range(1, 4)]
          for i in range(1, 4)]

print(matrix)

#Output:

#[[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#8. Generator Function
def numbers():
    for i in range(1, 6):
        yield i


for num in numbers():
    print(num)

#Output:

#1
#2
#3
#4
#5

#9. Generator vs Normal Function

#Normal function using return:

def get_numbers():
    return [1, 2, 3, 4, 5]


numbers = get_numbers()

print(numbers)

#Generator using yield:

def generate_numbers():
    for i in range(1, 6):
        yield i


numbers = generate_numbers()

for num in numbers:
    print(num)