import numpy as np
import numpy.linalg as la

def spring_state(k, m, s0, t):
    #complete the function
    A = np.array([[0,1],[-k/m,0]])
    eigvals, eigvecs = la.eig(A)
    c = la.solve(eigvecs, s0)
    c1, c2 = c[0], c[1]
    x1, x2 = eigvecs[:,0], eigvecs[:,1]
    return c1 * x1 * np.exp(eigvals[0] * t) + c2 * x2 * np.exp(eigvals[1] * t)