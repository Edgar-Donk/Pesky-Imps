from math import pi, sqrt
from prettytable import PrettyTable

x = PrettyTable(['step', 'a', 'x1', 'x2', 'b', 'f(a)', 'f(x1)', 'f(x2)', 'f(b)', 'emax'])

f = lambda r: 2 * (pi*r**2 + 50/r)

def golden(f, a, b, tol):
    step = 0
    d = (sqrt(5) - 1)/2 * (b - a)
    x2 = a + d
    x1 = b - d
    F1 = f(x1)
    F2 = f(x2)
    Fa = f(a)
    Fb = f(b)
    x.add_row([step, round(a,5), round(x1,5), round(x2,5), round(b,5), \
            round(Fa,5), round(F1,5), round(F2,5), round(Fb,5), round(abs(a-b),5)])

    while abs(F1 - F2) >= tol and step < 19:

        if F1 < F2:
            b, x2 = x2, x1
            Fb, F2 = F2, F1
            d = b - x2
            x1 = a + d
            F1 = f(x1)
        else:
            a, x1 = x1, x2
            Fa, F1 = F1, F2
            d = x1 - a
            x2 = b - d
            F2 = f(x2)

        step += 1
        x.add_row([step, round(a,5), round(x1,5), round(x2,5), round(b,5), \
            round(Fa,5), round(F1,5), round(F2,5), round(Fb,5), round(abs(a-b),5)])

    return(x1, F1, step)

A = 1
B = 5

Tol = 1e-4

x1, F1, step = golden(f, A, B, Tol)

print(x)
print(f'Minimum found : at {x1:.7f} value {F1:.7f} in {step} steps')



