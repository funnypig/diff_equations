import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,12))

f = lambda x,y: y**2-3*y+x-2
vf = np.vectorize(f)