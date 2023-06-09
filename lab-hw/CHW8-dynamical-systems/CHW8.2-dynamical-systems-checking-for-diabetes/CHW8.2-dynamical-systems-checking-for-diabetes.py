import numpy as np
import numpy.linalg as la

transition_matrix = np.array([[-0.9, -0.22], [0.8, -0.2]])
eigvals, eigvecs = la.eig(transition_matrix)
x_0 = [100, 0]
c = la.solve(eigvecs, x_0)
c1, c2 = c[0], c[1]

# uncomment below to plot g(x) and h(x)
plot_functions(c1, c2, eigvals, eigvecs)
hours = 3