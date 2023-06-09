import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def rk4(A, y, dt):
    # https://en.wikipedia.org/wiki/Runge–Kutta_method
    h = dt
    h2 = h/2
    k1 = A @ y
    k2 = A @ (y + h2 * k1)
    k3 = A @ (y + h2 * k2)
    k4 = A @ (y + h * k3)
    return y + h * (k1 + 2 * k2 + 2 * k3 + k4)/6

def euler(A, y, dt):
    # https://en.wikipedia.org/wiki/Euler_method#Example
    return y + dt * A@y

def solve_ode(t, A, x0, integrator=rk4):
    n = len(t)
    x = np.zeros((len(x0), n))
    x[:,0] = x0
    for i in range(1, n):
        x[:,i] = integrator(A, x[:,i-1], t[i] - t[i-1])
    return x

def plot_vecfield(xlim, ylim, n, A):
    R = np.linspace(xlim[0], xlim[1], n)
    J = np.linspace(ylim[0], ylim[1], n)

    rr, jj = np.meshgrid(R, J)
    rr = rr.flatten()
    jj = jj.flatten()
    u, v = A @ np.array([rr, jj])

    plt.quiver(rr, jj, u, v, pivot='mid', color='red')

def plot_vecfield_linear(xlim, ylim, n, c):
    R = np.linspace(xlim[0], xlim[1], n)
    J = np.linspace(ylim[0], ylim[1], n)

    rr, jj = np.meshgrid(R, J)
    rr = rr.flatten()
    jj = jj.flatten()
    u = np.ones_like(rr)
    v = c * jj

    plt.quiver(rr, jj, u, v, pivot='mid', color='red')

def plot_vecfield_constant(xlim, ylim, n, slope):
    R = np.linspace(xlim[0], xlim[1], n)
    J = np.linspace(ylim[0], ylim[1], n)

    rr, jj = np.meshgrid(R, J)
    rr = rr.flatten()
    jj = jj.flatten()
    u = np.ones_like(rr)
    v = slope * np.ones_like(rr)

    plt.quiver(rr, jj, u, v, pivot='mid', color='red')

def plot_vecspan(v, **kwargs):
    n = la.norm(v, np.inf)
    plt.plot(v[0] / [-n, n], v[1] / [-n, n], **kwargs)
