import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

plt.figure(figsize=(8,12))

f = lambda x,y: y**2-3*y+x-2
vf = np.vectorize(f)

def vector_field():
    m = np.linspace(-3, 3, 15)
    n = np.linspace(-0, 6, 30)

    x, y = np.meshgrid(m,n)
    fxy = vf(x,y)

    plt.quiver(m, n, x, fxy,  units='xy', width=0.01, scale=10)
vector_field()

"""
    "розрахунки" з цієї частини ви можете знайти в solutions.pdf
"""

x = np.linspace(-3, 3, 100)
y = np.linspace(0, 6, 100)

m1 = lambda x,y: 1.5+np.sqrt(9-4*(x-2))/2
m2 = lambda x,y: 1.5-np.sqrt(9-4*(x-2))/2

m1 = np.vectorize(m1)
m2 = np.vectorize(m2)

plt.plot(x, m1(x,y), color="grey", label="y=3+-sqrt(...)")
plt.plot(x, m2(x,y), color="grey")

# boundary
def xbound(x, condition, setLabel = False):
    y = np.linspace(0, 6, 500)

    ny = []

    for _y in y:
        if condition(x,  _y):
            ny.append(_y)

    if setLabel:
        plt.plot([x for _ in range(len(ny))], ny, color="blue", linestyle='--', label="boundary")
    else:
        plt.plot([x for _ in range(len(ny))], ny, color="blue", linestyle='--')

condition = lambda x,y: (2*y-3)*(y-m1(x,y))*(y-m2(x,y)) <= -1

for _x in np.arange(-3,3,0.1):
    xbound(_x, condition)
xbound(-3, condition, True)

# solutions

x = np.arange(-1,3,0.25)

for x0 in x:
    _x = np.arange(x0, x0+0.5, 0.05)
    plt.plot(_x, odeint(f, 1.4-np.sqrt(9-4*(x0-2))/2, _x), color = 'red', linewidth=0.8)
    plt.plot(_x, odeint(f, 1.6+np.sqrt(9-4*(x0-2))/2, _x), color = 'red', linewidth=0.8)


plt.plot(_x, odeint(f, 1.6+np.sqrt(9-4*(x0-2))/2, _x), color = 'red', linewidth=0.8, label="solution y'=f(x,y)")

plt.legend()
plt.show()