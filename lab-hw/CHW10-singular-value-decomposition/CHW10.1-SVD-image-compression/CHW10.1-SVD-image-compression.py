import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(altgeld, cmap='gray')

# Compute the SVD and compress the image

U, S, Vt = la.svd(altgeld, full_matrices=False)
num_layers = 0
Sigma = np.zeros((U.shape[1], Vt.shape[0]))
np.fill_diagonal(Sigma, S)
cur_sum = 0
diag_sum = np.sum(S)
altgeld_compressed = np.zeros((U.shape[0], Vt.shape[1]))
for i in range(len(S)):
    if cur_sum > diag_sum * 0.79:
        break
    else:
        cur_sum += S[i]
        altgeld_compressed += S[i] * np.outer(U[:,i], Vt[i])
        num_layers = i


# Plot the final image

plt.figure()
plt.imshow(altgeld_compressed, cmap='gray')