import numpy as np

# Estimate the mean and standard deviation from 1 dimensional data:
# generate 25,000 samples from a Gaussian distribution with mean 0 and standard deviation 5.
samples = np.random.normal(0, 5, 25000)

# Then estimate the mean and standard deviation of this gaussian using elementary numpy commands, i.e., addition,
# multiplication, division (do not use a command that takes data and returns the mean or standard deviation)
mean = np.sum(samples) / len(samples)
print("Mean: ", mean)

stdeviation = np.sqrt(np.sum((samples - mean) ** 2) / len(samples))
print("Standard Deviation: ", stdeviation)
