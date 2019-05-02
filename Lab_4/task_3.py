
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def integrate(f, a, b, step = 0.001):
    integral_sum = 0

    i = a+step

    while i<=b:
        integral_sum += (f(i)+f(i-step)) * step / 2

        i+=step

    return integral_sum

def Pikar_method(f, a, b, x0, y0, n = 3):
    """

    dy/dx = f(x,y)      -
                        |-  (1)
    y(x0) = y0          -

    P = { (x,y) : |x-x0|<=a, |y-y0|<=b }

    y_i = x0 + integral (from x0 to x) y_(i-1) (s) ds

    :param f: function f(x,y)
    :param a: vertical range of the rectangle
    :param b: horizontal range of the rectangle
    :param x0: point
    :param y0: point
    :param n: number of calculations
    :return: function to calculate solution of (1) at each point
    """

    y_0 = x0

    def _solution(k):
        if k == 1:
            y = lambda x: x0
        else:
            y =  lambda x: x0 + integrate(_solution(k-1), x0, x)

        y = np.vectorize(y)

        return y

    solution = lambda x: _solution(n)(x)

    return solution



def Miln_method(f, a, b, x0, y0, n):
    h = (b-a)/n

    t = np.linspace(a,b,n)

    # first 4 points
    x = list(odeint(f, y0, t[:4]))

    for i in range(3, n-1):
        _x_next = x[i-3] + (4*h/3) *  (2*f(t[i-2], x[i-2]) - f(t[i-1], x[i-1]) +2*f(t[i], x[i]))

        x_next = x[i-1] + (h/3) * ( f(t[i-1], x[i-1])+4*f(t[i],x[i])+f(t[i+1],_x_next))

        x.append(x_next)

    return np.array(x)



def test():
    f = lambda x,y: x**2+y**2+2
    a = 2
    b =1

    solution = lambda x: x**15 / 59535 + 2*x**13/12285 + 586*x**11/51975+20*x**9/189+\
                            173*x**7/315+4*x**5/3+5*x**3/3+2*x
    solution = np.vectorize(solution)


    arr = np.linspace(0,1, 1000)

    sol = solution(arr)

    calc = Miln_method(f, 0, 1, 0, 0, 1000)

    ar = [sol[i]-calc[i] for i in range(len(arr))]
    print(max(ar))

    plt.plot(arr, sol)
    plt.plot(arr, ar)
    plt.show()

#test()

def T3():
    f = lambda x,y: y + 2*x-x**2
    f = np.vectorize(f)

    lagrange_solution = lambda x: (x*x-x**3/3+1)*np.exp(x)
    lagrange_solution = np.vectorize(lagrange_solution)
    LS = lagrange_solution

    arr = np.linspace(0,1,1000)

    analytic_solution = LS(arr)

    miln_solution = Miln_method(f, 0, 1, 0, 1, 1000)

    max_error = max([analytic_solution[i]-miln_solution[i] for i in range(len(miln_solution))])
    print('CALCULATION ERROR:',max_error)

    plt.plot(arr, analytic_solution, label='Analytic solution')
    plt.plot(arr, miln_solution, label="Miln's method")

    plt.title('CALCULATION ERROR: '+str(max_error))

    plt.legend()
    plt.show()


T3()