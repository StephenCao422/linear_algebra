import numpy as np
import numpy.linalg as la

def create_dct_basis(N):
    D = np.zeros((N, N))
    x = ((np.arange(N) + 0.5) / N) * np.pi
    for k in range(N):
        D[:,k] = np.cos(x * k)
        D[:,k] /= la.norm(D[:,k])
    return D