import numpy as np
import matplotlib.pyplot as plt

# Get gaussian distribution samples
gauss1 = np.random.normal(-10, 5, 1000)
gauss2 = np.random.normal(10, 5, 1000)

# Get the sum of the two gaussian distribution samples
result = np.add(gauss1, gauss2)

# Plot the histogram of the sum
_= plt.hist(result, bins=100, color='red', alpha=0.5)
plt.show()
