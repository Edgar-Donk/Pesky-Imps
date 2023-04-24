# halving intervals
from prettytable import PrettyTable

x = PrettyTable(['step', 'a', 'b', 'x1', 'f(a)', 'f(b)', 'f(x1)', 'emax'])

a = 1.5
b = 2.0

f = lambda x: x**3 + x**2 - 3*x - 3

Fa = f(a)
Fb = f(b)
step = 0

x.add_row([step, a, b, None, Fa, Fb, None, abs(b - a)/2])
while abs(b - a)/2 >= 5e-5 and step < 19:
    step += 1
    x1 = (a+b)/2
    F1 = f(x1)

    if Fa*F1 < 0:
        b = x1
        Fb = F1
    else:
        a = x1
        Fa = F1

    x.add_row([step, round(a,7), round(b,7), round(x1,7), round(Fa,7), round(Fb,7), round(F1,7), round(abs(b - a)/2,7)])


print(x)
print (f"Root is: {(a+b)/2:.7} found in {step} iterations")