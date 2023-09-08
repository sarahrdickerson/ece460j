import numpy as np
import matplotlib.pyplot as plt

# Get gaussian distribution samples
gauss1 = np.random.normal(-10, 5, 1000)
gauss2 = np.random.normal(10, 5, 1000)

# Get the sum of the two gaussian distribution samples
result = np.add(gauss1, gauss2)

# Calculate the mean of the sum
mean_sum = 0
for i in range(0, 1000):
    mean_sum += result[i]

mean_estimate = mean_sum / 1000

# Calculate the standard deviation of the sum
std_sum = 0
for i in range(0, 1000):
    std_sum += (result[i] - mean_estimate) ** 2

std_estimate = np.sqrt(std_sum / 1000)


print("The mean estimate is: ", mean_estimate)
print("The mean of the sum is: ", np.mean(result))
print("The standard deviation estimate of the sum is: ", std_estimate)
print("The standard deviation of the sum is: ", np.std(result))