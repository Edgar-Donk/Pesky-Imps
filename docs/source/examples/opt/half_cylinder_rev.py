# https://arxiv.org/ftp/arxiv/papers/1903/1903.07117.pdf
# find minimum area given volume of a cylinder

'''
V = π r² h
A = 2 π r h + 2 π r²
A = 2 π r (h + r) = 2 π r (r + V / π r²) = 2 π r² + 2 V / r
'''

from math import pi
from prettytable import PrettyTable

f = lambda r: 2 * (pi*r**2 + 50/r) # (r-4)**2 #

x = PrettyTable(['step', 'a', 'x1', 'x2', 'b', 'f(x1)', 'f(x2)', 'emax'])

a = 1 # 2
b = 5 # 5.0

x2 = (a + b)/2
F2 = f(x2)

step = 0

while abs(b - a)/2 >= 5e-5:

    x1 = (a + x2)/2
    F1 = f(x1)
    x.add_row([step, round(a,7), round(x1,7), round(x2,7), round(b,7), round(F1,7), round(F2,7), round(abs(b - a)/2,7)])
    if F1 <= F2:
        b = x2
        x2 = x1
        F2 = F1
    else:
        x3 = (x2 + b)/2
        F3 = f(x3)
        if F2 <= F3:
            a = x1
            b = x3
        else:
            a = x2
            x2 = x3
            F2 = F3

    step += 1

    if step > 19:
        break

print(x)
print(f'Minimum found : at {(a+b)/2:.7f} value {F1:.7f} in {step} steps')


