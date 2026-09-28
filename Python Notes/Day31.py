#Example Code
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

#2D Array
#import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(data)

print("First row:", data[0])
print("First element:", data[0][0])
print("Shape:", data.shape)