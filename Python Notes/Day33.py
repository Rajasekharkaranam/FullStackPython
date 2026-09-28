#Example: Line Chart
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [65, 70, 75, 85, 90]

plt.plot(days, marks)

plt.title("Student Performance")
plt.xlabel("Days")
plt.ylabel("Marks")

plt.show()
#Example: Bar Chart
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "SQL", "HTML"]
marks = [90, 75, 85, 80]

plt.bar(subjects, marks)

plt.title("Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()