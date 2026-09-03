# Day 12 - Number Programs Using Loops


# 1. Reverse a Number
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number:", reverse)


# 2. Count Digits
num = int(input("\nEnter a number: "))

count = 0
temp = abs(num)

if temp == 0:
    count = 1

while temp > 0:
    count += 1
    temp //= 10

print("Number of Digits:", count)


# 3. Sum of Digits
num = int(input("\nEnter a number: "))

total = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of Digits:", total)


# 4. Palindrome Number
num = int(input("\nEnter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 5. Factorial
num = int(input("\nEnter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)


# 6. Prime Number
num = int(input("\nEnter a number: "))

if num < 2:
    print("Not a Prime Number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


# 7. Armstrong Number
num = int(input("\nEnter a number: "))

original = num
temp = num
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")