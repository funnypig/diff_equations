
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def adams_method(f, a, b, n, x0):
    h = (b-a)/n

    x = [x0]

    t = [a+(i-1)*h for i in range(n+1)]

    for i in range(1,4):
        k1 = f(t[i-1], x[i-1])
        k2 = f(t[i-1] + h/2, x[i-1]+h/2 * k1)
        k3 = f(t[i-1]+h/2, x[i-1]+h/2 * k2)
        k4 = f(t[i-1]+h, x[i-1] + h * k3)

        d = h/6 * (k1+2*k2+2*k3+k4)
        x.append(
            x[-1] + d
        )

    x = list(odeint(f, x0, t[:4]))

    for i in range(3, n):
        in_brackets = -9*f(t[i-3], x[i-3]) + \
         37 * f(t[i-2],x[i-2]) -  59*f(t[i-1], x[i-1]) + 55 * f(t[i], x[i])


        in_brackets = -9*f(x[i-3],t[i-3]) + \
         37 * f(x[i-2],t[i-2]) -  59*f(x[i-1],t[i-1]) + 55 * f(x[i],t[i])

        xp = x[i] + (h/24) * in_brackets

        in_brackets = f(x[i-2],t[i-2]) - 5*f( x[i-1],t[i-1]) +\
         19 * f(x[i],t[i]) + 9*f(xp,t[i+1])

        new_x = x[i] + (h/24) * in_brackets

        x.append(new_x)

    return x, t

def f(x,y):
    try:
        return y**2-3*y+x-2
    except:
        print(x,y)

x, t = adams_method(f, -0.5, 0.5, 20, 0)

plt.plot(t, x, label = "adams method")

t = np.linspace(-0.5, 0.5, 100)
plt.plot(t, odeint(f, 0 , t)+0.03, label="built-in method")

plt.title("i added 0.03 to built-in method plot to look at the difference")
plt.legend()
plt.show()