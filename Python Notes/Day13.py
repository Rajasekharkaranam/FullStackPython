#basic nested lopps
for i in range(1, 4):       # Outer loop
    for j in range(1, 4):   # Inner loop
        print(i, j)

#Square Star Pattern ⭐
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()


#Right Triangle Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#Number Triangle 🔢
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Repeated Number Pattern
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

#Multiplication Tables Using Nested Loops
for i in range(1, 4):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()