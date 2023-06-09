import numpy as np
import numpy.linalg as la

def pow_itr(M, x):
    xc = x.copy()
    while 1:
        if np.array_equal(M @ xc, xc):
            return xc
        else:
            xc = M @ xc
            
markov_matrix = np.array([
    [0.85, 0.2, 0.1, 0.05],
    [0.01, 0.6, 0.05, 0.1],
    [0.05, 0.1, 0.75, 0.15],
    [0.09, 0.1, 0.1, 0.7]])
x0 = [1,0,0,0]
steady_state = pow_itr(markov_matrix, x0)
x1 = [1,0,0,0]
for i in range(3):
    x1 = markov_matrix @ x1
prob_stark = x1[1]