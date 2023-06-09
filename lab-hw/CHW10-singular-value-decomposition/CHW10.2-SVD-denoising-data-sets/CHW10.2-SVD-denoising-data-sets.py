import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from matplotlib import cm

U, S, Vt = la.svd(measurement, full_matrices=False)
r = len(S)
Bk = np.zeros((U.shape[0], Vt.shape[1]))
differences = np.zeros(r)
for i in range(r):
    Bk += S[i] * np.outer(U[:,i], Vt[i])
    differences[i] = la.norm(Bk - exact_data)
num_layers = np.argmin(differences)
denoised_data = np.zeros(Bk.shape)
for i in range(num_layers + 1):
    denoised_data += S[i] * np.outer(U[:,i], Vt[i])

# Plot the data
display_plot(measurement)
display_plot(denoised_data)
display_plot(exact_data)

#uncomment to plot differences
#plt.figure()
#plt.plot(differences, 'r.')