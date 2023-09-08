import numpy as np
import matplotlib.pyplot as plt


def problem2():
    x = np.random.binomial(1, 0.5, 1000)
    for i in range(0,1000):
        if x[i] == 0:
            x[i] = -1

    print(x)

    dataZ = []
    sigmaXi = 0
#    for n in range(1, 1000):
#        for i in range(0, n):
#            sigmaXi += x[i]
#        dataZ.append(sigmaXi / np.sqrt(n))
#        sigmaXi = 0

    for n in range(1, 1000):
        sigmaXi += x[n]
        dataZ.append(sigmaXi / np.sqrt(n))
        print(sigmaXi)
    
    _= plt.hist(dataZ[1:1000], bins=100, color='red', alpha=0.5)
    plt.show()
    return 


problem2()