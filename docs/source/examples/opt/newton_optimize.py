'''
uses The central problem of optimization is minimization of functions. Let us
first consider the case of univariate functions, i.e., functions of a single real
variable.

xk+1 = xk - f´(xk)/f´´(xk)

using first and second derivatives
'''

# find minimum area given volume of a cylinder

'''
V = π r² h
A = 2 π r h + 2 π r²
A = 2 π r (h + r) = 2 π r (r + V / π r²) = 2 π r² + 2 V / r
'''
from math import pi
from prettytable import PrettyTable

f = lambda r: 2 * (pi*r**2 + 50/r)
df = lambda r: 4*pi*r -100/r**2
d2f = lambda r: 4*pi + 200/r**3
t = PrettyTable(['step', 'x0', 'df', 'd2f', 'error'])

def newtonOpt(df, d2f, x0, tol=1e-5, stepsmax=20):
    df0 = df(x0)
    d2f0 = d2f(x0)
    h = df0/d2f0
    steps=0
    t.add_row([steps, round(x0,7), round(df0,7), round(d2f0,7), round(h,7)])
    while abs(h) >= tol:
        x0 = x0 - h
        df0 = df(x0)
        d2f0 = d2f(x0)
        h = df0/d2f0

        steps += 1
        t.add_row([steps, round(x0,7), round(df0,7), round(d2f0,7), round(h,7)])
        if steps > stepsmax:
            return x0, steps

    return x0, steps

fn, steps = newtonOpt(df, d2f, 1)

print(t)
print("The approximate value of x is: "+str(fn))
print('Made in '+str(steps)+' iterations')











