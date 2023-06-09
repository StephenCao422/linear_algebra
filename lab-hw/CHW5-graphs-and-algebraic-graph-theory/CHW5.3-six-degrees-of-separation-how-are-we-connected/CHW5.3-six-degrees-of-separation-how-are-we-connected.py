import numpy as np
import numpy.linalg as la

def connected(network, degree):
    # network is a network (given as an adjacency matrix) and degree is the degree of separation you want to check
    A = np.eye(network.shape[0])
    for i in range(1, degree + 1):
        A += la.matrix_power(network, i)
    return np.all(A > 0)