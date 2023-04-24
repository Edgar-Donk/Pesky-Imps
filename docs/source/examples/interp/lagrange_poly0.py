import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme()

def quad_interp(x0, y0, x1, y1, x2, y2, x):
    y = y0 * (x - x1)*(x - x2)/((x0 - x1)*(x0 - x2)) + \
            y1 * (x - x0)*(x - x2)/((x1 - x0)*(x1 - x2)) + \
            y2 * (x - x0)*(x - x1)/((x2 - x0)*(x2 - x1))
    return y

x = [0, 1, 2]
y = [1, 3, 2]

xs = np.arange(-1.0,3.1,0.1)
ys0 = quad_interp(x[0],1,x[1],0,x[2],0, xs)
ys1 = quad_interp(x[0],0,x[1],1,x[2],0, xs)
ys2 = quad_interp(x[0],0,x[1],0,x[2],1, xs)

fig = plt.figure(figsize = (10,8))
plt.plot(xs, ys0, 'b', label = 'P1 $basis\,poly$')
plt.plot(xs, ys1, 'y', label = 'P2 $basis\,poly$')
plt.plot(xs, ys2, 'g', label = 'P3 $basis\,poly$')

L = ys0*y[0] + ys1*y[1] + ys2*y[2]
#print(L)

plt.plot(x, np.ones(len(x)), 'ko', x, np.zeros(len(x)), 'ko', label='basis points')
plt.plot(xs, L, 'r', x, y, 'ro', label='Interpolation')
plt.scatter(0, 1, fc='r', ec='k', s=60, label='P1 and Interpolation')

plt.legend()

plt.title('Lagrange Basis and Interpolation Polynomials')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

plt.show()
#plt.savefig('../../figures/lag_interp.png')