# linear root finding
from prettytable import PrettyTable
from numpy import sign, sin

print('linear root finding - curtis')

def check_linear(f, a, b, verbose = True):
    t = PrettyTable(['step', 'a', 'b', 'x1', 'f(a)', 'f(b)', 'f(x1)', '|f(x1)|'])
    fa = f(a)
    fb = f(b)
    step = 0
    emax = min(fa,fb)
    t.add_row([step, a, b, None, round(fa,7), round(fb,7), None, abs(b-a)])

    while abs(emax) >= 5e-5 and step < 19:
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
        t.add_row([step, round(a,7), round(b,7), round(x1,7), round(fa,7), round(fb,7), round(f1,7), round(abs(f1),7)])

    return x1, step, t


A = 1.5
B = 2.0

f = lambda x: sin(x) - x/2

x1, step, t = check_linear(f, A, B)

print(f'Linear root finding on function sin(x) - x/2')
print(t)
print(f'Root found : {x1:.7} in {step} interpolations')
