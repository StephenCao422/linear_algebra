import numpy as np
import matplotlib.pyplot as plt

def draw_slinky(x, ys, radius):
    x_vals = []
    y_vals = []
    for i in range(len(ys)):
        y = ys[i]
        if i == 0 or i == len(ys) - 1:
            x_vals.append(x - radius); x_vals.append(x + radius)
            y_vals.append(ys[i]); y_vals.append(ys[i])
        if i < len(ys) - 1:
            if i % 2 != 0:
                x_vals.append(x - radius); x_vals.append(x + radius)
                y_vals.append(ys[i]); y_vals.append(ys[i+1])
            else:
                x_vals.append(x + radius); x_vals.append(x - radius)
                y_vals.append(ys[i]); y_vals.append(ys[i+1])
    y_vals = np.array(y_vals)
    plt.plot(x_vals, -y_vals, '-');
    
