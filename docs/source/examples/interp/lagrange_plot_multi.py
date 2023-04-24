# https://stackoverflow.com/questions/4003794/lagrange-interpolation-in-python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

class LagrangePoly:

    def __init__(self, X, Y):
        self.n = len(X)
        self.X = np.array(X)
        self.Y = np.array(Y)

    def basis(self, x, j):
        b = [(x - self.X[m]) / (self.X[j] - self.X[m])
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.Y[j]

    def interpolate(self, x):
        b = [self.basis(x, j) for j in range(self.n)]
        return np.sum(b, axis=0)

X  = [-9, -4, -1, 7]
Y  = [5, 2, -2, 9]

lp = LagrangePoly(X, Y)
xx = np.arange(-100, 100) / 10

fig = plt.figure(figsize = (10,8))
plt.plot(xx, lp.basis(xx, 0), 'b', label = 'P1 $basis\,poly$')
plt.plot(xx, lp.basis(xx, 1), 'y', label = 'P2 $basis\,poly$')
plt.plot(xx, lp.basis(xx, 2), 'g', label = 'P3 $basis\,poly$')
plt.plot(xx, lp.basis(xx, 3), 'm', label = 'P4 $basis\,poly$')
plt.scatter(X, np.zeros(len(X)), fc='none', ec='k', label='basis points')
plt.plot(xx, lp.interpolate(xx), 'r', X, Y, 'ro', label='Interpolation')

plt.ylim(-5, 15)
plt.legend()
plt.title('Lagrange Basis and Interpolation Polynomials $4\,points$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()
#plt.savefig('../../figures/lag_interp_multi.png')