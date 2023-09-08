import numpy as np


def problem4():
    sampleNum = 10000
    mean = [-5, 5]
    cov = [[20, 0.8],[0.8, 30]]
    x, y = np.random.multivariate_normal(mean, cov, sampleNum).T

    # Mean of X and Y
    meanX = sum(x) / sampleNum
    meanY = sum(y) / sampleNum

    meanData = [meanX, meanY]

    print("The mean of X and Y is: ", meanData)

    # Covariant Matrix
    S = 0
    for i in range(1, sampleNum):
        S += (x[i] - meanX) * (y[i] - meanY)

    covXY = S / (sampleNum - 1)

    varX = 0
    for i in range(1, sampleNum):
        varX += (x[i] - meanX) ** 2

    varX = varX / (sampleNum - 1)

    varY = 0
    for i in range(1, sampleNum):
        varY += (y[i] - meanY) ** 2

    varY = varY / (sampleNum - 1)

    covMatrix = [[varX, covXY], [covXY, varY]]



    print("The covariant matrix is: ", np.cov(x, y))
    print("The covariant matrix estimate is: ", covMatrix)



    


problem4()