# halving intervals

from numpy import linspace, pi
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

f = lambda x: 2 * (pi*x**2 + 50/x) # (x-4)**2 #

x = PrettyTable(['step', 'a', 'b', 'x1', 'f(a)', 'f(b)', 'f(x1)', 'emax'])

a = 1 # 1 # 2
b = 5 # 4 # 5
Fa = f(a)
Fb = f(b)
step = 0
xp = linspace(a,b)

while abs(b - a)/2 >= 5e-5:

    x1=(a+b)/2
    F1 = f(x1)
    # check whether the limits bracket the minimum
    if Fa >= F1 and Fb >= F1:
        pass
    elif x1 <= a + Fa * (b - a)/(Fb - Fa):
        pass
    else:
        linear = a + Fa * (b - a)/(Fb - Fa)
        print('Limits not bracketing minimum, lower {}, calculated {}, upper {}'.format(a,x1,b))
        print(f'Values lower {Fa:.4f}, calculated {F1:.4f}, upper {Fb:.4f}')
        print(f'Linear position {linear:.4f}')
        break

    x.add_row([step, round(a,7), round(b,7), round(x1,7), round(Fa,7), round(Fb,7), round(F1,7), round(abs(b - a)/2,7)])

    if Fa < Fb:
        b = x1
        Fb = F1
    else:
        a = x1
        Fa = F1

    step += 1
    if step > 19:
        break

print(x)
print(f'Minimum found : at {(a+b)/2:.7f} value {F1:.7f} in {step-1} steps')

plt.plot(xp, f(xp), label='function')
plt.scatter((a+b)/2, F1 , marker='P', color='r', label='minimum')
plt.text((a+b)/2-0.38, F1+5, (round((a+b)/2,2), round(F1,4)))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Optimisation by Interval Halving \n on function $2\cdot(\pi\cdot r^2 + 50/r)$')
plt.legend()
plt.show()
#plt.savefig('../../figures/half_opt.png')
