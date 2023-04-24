# https://stackoverflow.com/questions/4003794/lagrange-interpolation-in-python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

class LagrangePoly:

    def __init__(self, X, Y):
        self.n = len(Y)
        self.X = np.array(X)
        self.Y = np.array(Y)

    def basis(self, y, j):
        b = [(y - self.Y[m]) / (self.Y[j] - self.Y[m])
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.X[j]

    def interpolate(self, y):
        b = [self.basis(y, j) for j in range(self.n)]
        return np.sum(b, axis=0)

f = lambda x: x**3 + x**2 - 3*x - 3

X  = [1.5, 1.75, 2]
f0 = f(X[0])
f1 = f(X[1])
f2 = f(X[2])
Y  = [f0, f1, f2]

lp = LagrangePoly(X, Y)
yy = np.linspace(min(Y), max(Y))
xx = np.linspace(min(X), max(X))

#fig = plt.figure(figsize = (10,8))
plt.plot(lp.basis(yy, 0), yy, 'b', label = 'P1 $basis\,poly$')
plt.plot(lp.basis(yy, 1), yy, 'g', label = 'P2 $basis\,poly$')
plt.plot(lp.basis(yy, 2), yy, 'y', label = 'P3 $basis\,poly$')
plt.scatter(np.zeros(len(Y)), Y, fc='none', ec='k', label='basis other points')
plt.plot(xx, f(xx), 'r', label='function')
plt.plot(lp.interpolate(yy), yy, 'm:', X, Y, 'mo', label='Interpolation')
plt.plot(lp.interpolate(0), 0, 'rP', label='1st estimate root')

plt.ylim(-2.1, 3.1)
plt.legend()
plt.title('Root finding with Inverse Quadratic\nLagrange Basis and Interpolation Polynomials $3\,points$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

#print('1st estimate root:', lp.interpolate(0))
plt.show()
#plt.savefig('../../figures/iqi_root.png')