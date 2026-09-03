# Day 7 - Strings and String Methods

# 1. Format a customer's name
name = input("Enter your full name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())


# 2. Remove extra spaces from a username
username = input("\nEnter username: ")

username = username.strip()

print("Clean Username:", username)


# 3. Check whether an email contains @
email = input("\nEnter your email: ")

if "@" in email:
    print("Valid email format")
else:
    print("Invalid email format")


# 4. Replace spaces with underscores
city = input("\nEnter your city: ")

print("Formatted City:", city.replace(" ", "_"))


# 5. Check whether a word exists in a message
message = input("\nEnter a message: ")
word = input("Enter word to search: ")

if word.lower() in message.lower():
    print("Word found")
else:
    print("Word not found")