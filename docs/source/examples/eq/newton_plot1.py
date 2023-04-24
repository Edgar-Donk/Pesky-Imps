import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()


def deriv(f,x):
    h = 1e-9                 #step-size
    return (f(x+h) - f(x))/h        #definition of derivative

def tangent_line(f,x_0,a,b):
    x = np.linspace(a,b,200)
    y = f(x)
    y_0 = f(x_0)
    y_tan = deriv(f,x_0) * (x - x_0) + y_0
    return x, y, y_tan

f = lambda x: x**3 + x**2 - 3*x - 3

x0, y, y0 = tangent_line(f,1.5,1,2)


#plotting
plt.plot(x0,y,'c-', label='function')
plt.hlines(0, 1, 2, 'g', label='x-axis')

plt.scatter([1.5], [0], fc='none', ec='g', label='guess')
plt.annotate('initial guess', xy=(1.5, 0), xytext=(1.5,0.25),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='black') )
plt.vlines(1.5, 0, f(1.5), 'k', linestyles='dotted', label='guess step')
plt.scatter([1.5], [f(1.5)], fc='none', ec='m', label='1st point')

plt.plot(x0,y0,'m--', label='1st tangent')
plt.scatter([1.78], [0], fc='none', ec='g', label='1st x-axis intercept')
plt.annotate('1st x-axis intercept', xy=(1.78, 0), xytext=(1.78,-0.25),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='black') )
plt.vlines(1.78, 0, f(1.78), 'k', linestyles='dotted', label='1st step')
plt.axis([1,2,-3,1])
x1, y, y1 = tangent_line(f,1.78,1,2)

plt.scatter([1.78], [f(1.78)], fc='none', ec='r', label='next point')

plt.plot(x1,y1,'r--', label='2nd tangent')
plt.scatter([1.73], [0], fc='none', ec='b', label='2nd x-axis intercept')

plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Root by Newton-Raphson '+r'$x**3 + x**2 - 3*x - 3$')
plt.show()
#plt.savefig('../../figures/Newton-Raphson_root.png')

