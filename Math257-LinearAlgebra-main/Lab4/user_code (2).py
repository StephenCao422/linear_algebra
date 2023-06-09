import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

N = 100
Ls = 10   # (cm)      Length of the slinky
Ks = 700  # (N/cm)     Stiffness
M = 170  # (grams)    Total mass


def solve_slinky(N, M, Ks, Ls, plot=True):

    m = M/(N+1)  # each individual mass
    k = Ks*(N)  # each individiual spring stiffness
    l = Ls/(N)   # each individual spring length
    g = 9.81*10**2  # 386 #(in/s^2)

    k_array = k*np.ones(N)

    # TODO: obtain the stiffness matrix
    stiffness = get_stiffness(k_array)
    # TODO: obtain the force vector
    force = get_force(m,g,N)
    # TODO: solve for the displacement
    displacement = np.linalg.solve(stiffness, force)
    # TODO: modify the code below to get correct values of coord and utotal
    coord = np.array([l*i for i in range(N+1)])
    utotal = np.append(0, displacement)

    def_coord = coord + utotal

    # plot the slinky
    if plot:
        plt.figure()
        plt.axis('equal')
        draw_slinky(-5, coord, 2)
        draw_slinky(5, def_coord, 2)
        plt.show()
    return coord, utotal

# Uncomment the line below to plot the results to help you debug
# _ = solve_slinky(100, M, Ks, Ls)

# The code below plots the convergence of displacement of the mass.
# You can remove """ to uncomment the code and run it after you finish the implementation of solve_slinky.
"""
plt.figure(figsize=(10, 8))

coord, utotal = solve_slinky(2, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'ro-', label='N = 2')

coord, utotal = solve_slinky(3, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'bs-', label='N = 3')

coord, utotal = solve_slinky(5, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'gd-', label='N = 5')

coord, utotal = solve_slinky(10, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'mx-', label='N = 10')

coord, utotal = solve_slinky(20, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'o-', label='N = 20')

coord, utotal = solve_slinky(30, M, Ks, Ls, plot=False)
plt.plot(coord, utotal, 'k-', label='N = 30')

plt.legend()
plt.xlabel('Mass positions')
plt.ylabel('Displacement')
plt.show()
"""