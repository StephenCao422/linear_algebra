import numpy as np
import numpy.linalg as la

M = A.copy()
for i in range(M.shape[1]):
    col = M[:,i]
    if np.all(col == 0):
        col.fill(1)
    col /= np.sum(col)
alpha = 0.85
N = M.shape[0]
G = alpha * M + (1 - alpha) / N * np.ones(M.shape)
x0 = np.random.rand(N)
x0 /= np.sum(x0)
x = power_iteration(G, x0)
protagonist = names[np.argmax(x)]

# uncomment below to print name of the protagonist
print(protagonist)