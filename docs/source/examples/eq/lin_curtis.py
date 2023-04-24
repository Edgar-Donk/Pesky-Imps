# linear root finding
from prettytable import PrettyTable
from numpy import sign

print('linear root finding - curtis')
x = PrettyTable(['step', 'a', 'b', 'x1', 'f(a)', 'f(b)', 'f(x1)', '|f(x1)|'])

a = 1.5
b = 2.0
def f(x):
    return x**3 + x**2 - 3*x - 3
fa = f(a)
fb = f(b)
step = 0
emax = min(fa,fb)

x.add_row([step, a, b, None, fa, fb, None, abs(b-a)])
while abs(emax) >= 5e-5:
    step += 1
    x1 = a - fa * (b - a) / (fb - fa)
    f1 = f(x1)

    if sign(fa) != sign(fb): # fa*f1 < 0
        b = x1
        fb = f1
    else:
        a = x1
        fa = f1

    emax = abs(f1)
    x.add_row([step, round(a,7), round(b,7), round(x1,7), round(fa,7), round(fb,7), round(f1,7), round(abs(f1),7)])

    if step > 19:
        break

print(x)
print(f'Root found : {x1:.7} in {step} interpolations')
