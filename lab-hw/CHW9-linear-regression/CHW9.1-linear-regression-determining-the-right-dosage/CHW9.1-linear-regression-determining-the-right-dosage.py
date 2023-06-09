import numpy as np
import numpy.linalg as la
import scipy.linalg as sla
import matplotlib.pyplot as plt

A = np.column_stack((np.ones_like(trial_data[0]), trial_data[0]))
beta1, beta2 = la.lstsq(A, trial_data[1])[0]
beta = np.array((beta1, beta2)).T
dosage = (23 - beta1) / beta2

# Uncomment to display least squares line
#display_regression(beta)