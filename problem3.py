import numpy as np


def problem3():
    gauss = np.random.normal(0, 5, 25000)

    # Calculate mean
    mean_sum = 0
    for i in range(0, 25000):
        mean_sum += gauss[i]

    mean_estimate = mean_sum / 25000

    # Calculate standard deviation
    std_sum = 0
    for i in range(0, 25000):
        std_sum += (gauss[i] - mean_estimate) ** 2

    std_estimate = np.sqrt(std_sum / 25000)

    print("The mean estimate is: ", mean_estimate)
    print("The mean of the sum is: ", np.mean(gauss))
    print("The standard deviation estimate of the sum is: ", std_estimate)
    print("The standard deviation of the sum is: ", np.std(gauss))



problem3()