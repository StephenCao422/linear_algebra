import numpy as np
import matplotlib.pyplot as plt

# Write your code to calculate denoised audio signal 
D = create_dct_basis(audio_signal.shape[0])
coordinates = D.T @ audio_signal
print(coordinates.shape)
coordinates_filtered = coordinates.copy()
for i in range(coordinates.shape[0]):
    if abs(coordinates[i]) < 1:
        coordinates_filtered[i] = 0.
denoised = D @ coordinates_filtered


# Uncomment below to plot 
#fig, ax = plt.subplots()
#plt.plot(audio_signal)
#plt.plot(denoised)