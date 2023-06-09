import numpy as np
import scipy.linalg as sla

#Step 0: Modify the vector E by appending a zero, so that it looks like the vector E~ above.
E = np.append(E, [0])
# print(E.shape)
#Step 1: Create the matrix A.
A = np.zeros((N+1, N+1))
for i in range(N):
    A[i][i] = R[i]
    A[i][-1] = 1
    A[-1][i] = 1
#Step 2: Solve the system AI = E.
P, L, U = sla.lu(A)
c = sla.solve_triangular(L, P.T @ E, lower=True)
I = sla.solve_triangular(U, c, lower=False)