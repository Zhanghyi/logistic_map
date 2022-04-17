import numpy as np
from matplotlib import pyplot as plt

u_min = 0
u_max = 4
u_step = 0.001

x0 = 0.1
iterations = 1000
num_plot = 100


def logistic(xk, u):
    return u * xk * (1 - xk)


if __name__ == '__main__':
    x = np.array([])
    y = np.array([])
    for u in np.arange(u_min, u_max, u_step):
        xk = x0
        for i in range(iterations):
            xk = logistic(xk, u)
            if i > iterations - num_plot:
                x = np.append(x, np.array([u]))
                y = np.append(y, np.array([xk]))
    plt.plot(x, y, '.', ms=0.1)
    plt.ylim(0, 1)
    plt.xlim(u_min, u_max)
    plt.savefig('images/logistic.png')
