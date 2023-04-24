import numpy as np
from sympy import *
from prettytable import PrettyTable

# define what is the variable
x = symbols('x')

# define the function
f = x**3 + x**2 -3*x - 3

# find the first derivative
fderivative = f.diff(x)

# get a value of the derivative for a specific x
# let's say f'(0)

xn = 1
t = PrettyTable(['steps', 'x', 'f(x)', 'tolerance'])

fx = float(f.evalf(subs= {x:xn}))

step = 0
tol = 1e-5
t.add_row([step, round(xn,8), round(fx,8), tol])

while abs(fx) > tol and step < 19:
    xn = xn - fx/float(fderivative.evalf(subs= {x:xn}))
    fx = float(f.evalf(subs= {x:xn}))

    step +=1
    t.add_row([step, round(xn,8), round(fx,8), tol])

print(t)
print (f"root is: {xn} in {step} interpolations")