# Day 9 - Sets and Dictionaries


# 1. Remove duplicate products
products = ["Apple", "Banana", "Apple", "Mango", "Banana"]

unique_products = set(products)

print("Unique Products:", unique_products)


# 2. Common interests between two friends
friend1 = {"Cricket", "Movies", "Music", "Travel"}
friend2 = {"Music", "Travel", "Gaming", "Movies"}

print("\nCommon Interests:")
print(friend1.intersection(friend2))


# 3. All interests
print("\nAll Interests:")
print(friend1.union(friend2))


# 4. Student information using dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("\nStudent Name:", student["name"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# 5. Update student marks
student["marks"] = 92

print("\nUpdated Marks:", student["marks"])


# 6. Simple Contact Book
contacts = {
    "Rahul": "9876543210",
    "Priya": "9123456780",
    "Arjun": "9988776655"
}

name = input("\nEnter contact name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact not found")