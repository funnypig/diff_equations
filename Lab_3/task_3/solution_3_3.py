import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,12))

f = lambda x,y: y**2-3*y+x-2
vf = np.vectorize(f)

"""
    
    f(x,y) = k
    
    y^2-3y+x-2 = k  =>  x = -(y^2-3y-2)-k

"""

y = np.linspace(0,6, 300)

iso = lambda y,k: -(y**2-3*y-2)-k
iso = np.vectorize(iso)

plt.title("Isoclines")

for k in range(1,4):
    plt.plot(iso(y,k), y, label="k = {}".format(k))

plt.legend()
plt.show()