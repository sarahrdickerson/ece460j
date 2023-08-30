import numpy as np
import matplotlib.pyplot as plt

# Create 1000 samples from a Gaussian distribution with mean -10 and standard deviation 5.
s1 = np.random.normal(-10, 5, 1000)

# Create another 1000 samples from another independent Gaussian with mean 10 and standard deviation 5
s2 = np.random.normal(10, 5, 1000)

# (a) Take the sum of 2 these Gaussians by adding the two sets of 1000 points, point by point,
#     and plot the histogram of the resulting 1000 points. What do you observe?
s = s1 + s2
plt.hist(s, bins=50)
plt.title("Problem 1 Histogram")
plt.show()

# (b) Estimate the mean and the variance of the sum
print("Mean: ", np.mean(s))
print("Variance: ", np.var(s))
