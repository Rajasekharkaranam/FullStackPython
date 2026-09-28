#Example Code
import pandas as pd

data = {
    "Name": ["Raj", "Kiran", "Arjun"],
    "Age": [22, 21, 23],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
#Accessing Data
print(df["Name"])

print(df["Marks"])

print("Average Marks:", df["Marks"].mean())
#Filtering Data
high_marks = df[df["Marks"] > 80]

print(high_marks)