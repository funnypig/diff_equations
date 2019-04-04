import numpy as np
import matplotlib.pyplot as plt


f = lambda x,y: y**2-3*y+x-2
vf = np.vectorize(f)

def vector_field():
    m = np.arange(-3, 4)
    n = np.arange(0, 7) *0.5

    x, y = np.meshgrid(n, m)
    fxy = vf(x,y)

    q,w = np.meshgrid(x, fxy)

    plt.quiver(x, y,  units='xy', width=0.04, scale=8)

vector_field()

plt.show()