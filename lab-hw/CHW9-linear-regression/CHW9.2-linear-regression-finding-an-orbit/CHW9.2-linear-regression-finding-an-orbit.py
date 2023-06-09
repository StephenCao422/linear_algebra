import numpy as np
import numpy.linalg as la
import scipy.linalg as sla
import matplotlib.pyplot as plt

r, theta = observation_data[0], observation_data[1]
x = r * np.cos(theta)
A = np.column_stack((np.ones_like(x), x))
beta, e = la.lstsq(A, r)[0]
distance = beta / (1 - e * np.cos(4.92))

# Uncomment to plot estimated orbit
#display_regression(beta,e)