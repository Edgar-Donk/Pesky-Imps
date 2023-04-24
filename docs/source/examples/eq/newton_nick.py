# https://nickcdryan.com/2017/09/13/root-finding-algorithms-in-python-line-search-bisection-secant-newton-raphson-boydens-inverse-quadratic-interpolation-brents/
from __future__ import division

from prettytable import PrettyTable

def discrete_method_approx(f, x, h=.00000001):
    return (f(x+h) - f(x)) / h

t = PrettyTable(['steps', 'x', 'df', 'f(x)', 'tolerance'])
def newton_raphson(f, x, tolerance=1e-5):
    steps_taken = 0
    df = discrete_method_approx(f, x)
    fx = f(x)
    t.add_row([steps_taken, round(x,7), round(df,7), round(fx,7),\
            tolerance])
    while abs(f(x)) > tolerance:
        x = x - fx/df
        fx = f(x)
        df = discrete_method_approx(f, x)
        steps_taken += 1
        t.add_row([steps_taken, round(x,7), round(df,7), round(fx,7),\
            tolerance])
    return x, steps_taken

f = lambda x: x**3 + x**2 - 3*x - 3

root, steps = newton_raphson(f, 1)
print(t)
print (f"root is: {root:.7} in {steps} interpolations")