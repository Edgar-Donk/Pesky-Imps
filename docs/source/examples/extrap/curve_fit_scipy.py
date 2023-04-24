# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    y = a*x + b
    return y

sns.set_theme()

# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))

alpha = curve_fit(func, xdata = x, ydata = y)[0]
print('slope m :', alpha[0], 'intercept c:', alpha[1])
'''
# plot the results
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''

def func(x, a, b, c, d):
  return a + b * x + c * x ** 2 + d * x ** 3

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

print('numpy', np.polyfit(x, y, 3))

popt, _ = curve_fit(func, x, y)
print('scipy', popt, 'order reversed')

# constrained so 3rd term in polyfit becomes 2, 2nd term scipy
popt_cons, _ = curve_fit(func, x, y, bounds=([-np.inf, 2, -np.inf, -np.inf], [np.inf, 2.001, np.inf, np.inf]))
print('constrained scipy', popt_cons)

xnew = np.linspace(x[0], x[-1], 1000)

plt.plot(x, y, 'bo', label='original data')
plt.plot(xnew, func(xnew, *popt), 'k-', label='normal scipy')
plt.plot(xnew, func(xnew, *popt_cons), 'r-', label='constrained scipy')
plt.legend()
plt.show()