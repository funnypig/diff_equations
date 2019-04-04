from scipy.integrate import odeint
from scipy.optimize import minimize
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np

g = lambda x, y: y**2+3*y+2

plt.figure(figsize=(6,10))
plt.tight_layout()


# Task 2.1

plt.subplot(2,1,1)

vg = np.vectorize(g)
x = np.arange(-4,5)
x, y = np.meshgrid(x, vg(0,x))

plt.quiver(x, y)
plt.title("Vector field")

# Task 2.2

# g(y0) = 0
y0 = float(minimize(lambda y: abs(g(0, y)), 0).x)

x = np.linspace(-3, 3, 100)
y = odeint(g, y0, x)

plt.subplot(2,1,2)

plt.plot(x, y)
plt.title("Integral curve")

legend = ['y0 = {}'.format(y0)]

for y0 in [-4,-2,2,4]:
    plt.plot(x, odeint(g, y0, x))
    legend.append('y0 = {}'.format(y0))

plt.legend(legend)
plt.show()