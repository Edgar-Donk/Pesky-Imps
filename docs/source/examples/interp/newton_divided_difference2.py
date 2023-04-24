# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

    return coef

def newton_poly(coef, x_data, x):
    '''
    evaluate the newton polynomial
    at x
    '''
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

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

x = np.array([-5, -1, 0, 2])
y = np.array([-2, 6, 1, 3])
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.linspace(max(x), min(x), int((max(x)-min(x))*10)) # -5, 2.1, .1
y_new = newton_poly(a_s, x, x_new)

lp = LagrangePoly(x, y)


plt.figure(figsize = (12, 8))
plt.plot(x, y, 'ro', label='data points')
plt.plot(x_new, y_new, 'y', label='Newton poly')
plt.plot(x_new, lp.interpolate(x_new), 'k', linestyle=':', label='Lagrange')
plt.legend()
plt.title('Newton Interpolation Polynomial\nCoincides with Lagrange Polynomial')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

plt.show()
#plt.savefig('../../figures/newton_interp.png')