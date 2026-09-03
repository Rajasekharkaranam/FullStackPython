# Day 8 - Lists and Tuples

# 1. Shopping Cart
cart = ["Laptop", "Mouse", "Keyboard"]

print("Shopping Cart:", cart)

cart.append("Headphones")
print("After adding item:", cart)

cart.remove("Mouse")
print("After removing item:", cart)


# 2. Grocery Shopping List
groceries = ["Rice", "Milk", "Eggs"]

groceries.insert(1, "Bread")

print("\nGrocery List:", groceries)


# 3. Student Marks
marks = [85, 72, 91, 68, 88]

print("\nMarks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

marks.sort()
print("Sorted Marks:", marks)


# 4. Count repeated product
products = ["Pen", "Book", "Pen", "Bag", "Pen"]

print("\nNumber of Pens:", products.count("Pen"))


# 5. Tuple - Days of the Week
days = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday")

print("\nDays of the Week:", days)
print("First Day:", days[0])
print("Last Day:", days[-1])