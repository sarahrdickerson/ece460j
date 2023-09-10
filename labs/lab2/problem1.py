import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# When given a data matrix, an easy way to tell if any two columns are correlated is to look
# at a scatter plot of each column against each other column. For a warm up, do this: Look
# at the data in DF1 in Lab2 Data.zip. Which columns are (pairwise) correlated? Figure out
# how to do this with Pandas, and also how to do this with Seaborn

df = pd.read_csv("DF1")
# drop label column
df = df.drop("Unnamed: 0", axis=1)

# pandas
pd.plotting.scatter_matrix(df, alpha=0.3)
plt.suptitle("Pandas Scatter Matrix")
plt.show()

# seaborn
sns.pairplot(df)
plt.suptitle("Seaborn Pairplot")
plt.show()


# Compute the covariance matrix of the data. Write the explicit expression for what this is,
# and then use any command you like (e.g., np.cov) to compute the 4 × 4 matrix. Explain why
# the numbers that you get fit with the plots you got.
cov_matrix = np.cov(df.T)
print(cov_matrix)


# The above problem in reverse.
# Generate a zero-mean multivariate Gaussian random variable in 3 dimensions, Z = (X1, X2, X3) so that (X1, X2) and (X1, X3) are uncorrelated, but
# (X2, X3) are correlated. Specifically: choose a covariance matrix that has the above correlations structure, and write this down.

# Generate zero-mean multivariate Gaussian 3D random variable with uncorrelated (X1, X2) and (X1, X3) and correlated (X2, X3)
mean = [0, 0, 0]
cov = [[1, 0, 0], [0, 1, 0.5], [0, 0.5, 1]]

s = np.random.multivariate_normal(mean, cov, size=1000)


# Then find a way to generate samples from this Gaussian.
# Choose one of the non-zero covariance terms (Cij , if C denotes your covariance matrix) and
# plot it vs the estimated covariance term, as the number of samples you use scales. The goal
# is to get a visual representation of how the empirical covariance converges to the true (or
# family) covariance.
n_vals = [10, 100, 1000, 10000]
cov_vals = []

for n in n_vals:
    s = np.random.multivariate_normal(mean, cov, size=n)
    cov_vals.append(np.cov(s.T)[1, 2])

plt.plot(n_vals, cov_vals)
plt.title("Covariance vs. Number of Samples")
plt.xlabel("Number of Samples")
plt.ylabel("Covariance")
plt.show()
