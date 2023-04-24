# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.04-Least-Squares-Regression-in-Python.html
# https://stackoverflow.com/questions/18767523/fitting-data-with-numpy

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
x_new = np.linspace(x[0], x[-1], num=len(x)*10)
'''
# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T

# turn y into a column vector
y = y[:, np.newaxis]

# Direct least square regression
#alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
alpha = np.linalg.lstsq(A, y, rcond=None)[0]
print('m: ',alpha[0],' c: ',alpha[1])
'''
coefs = poly.polyfit(x, y, 1)
#print(coefs)

# ffit = poly.polyval(x_new, coefs)
# plt.plot(x_new, ffit, 'r')

ffit = poly.Polynomial(coefs)

yhat = coefs[1] * x + coefs[0]
R = yhat - y

plt.figure(2)
plt.plot(x, R, 'b.', label='residuals')
plt.hlines(0,x[0],x[-1], colors='green', linestyle='dashed', label='$y = 0$')
plt.xlabel('x')
plt.ylabel('Residual $\hat{y} - y$')
plt.legend()
plt.title('Residuals \nshould be random either side')

plt.figure(1)
plt.plot(x_new, ffit(x_new), 'r',label=f'linear fit \n{coefs[1]:.4} x + {coefs[0]:.4}')
#print(ffit)

# plot the results
plt.plot(x, y, 'b.', label='data points')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression using Numpy polyfit \n$ y = 1.5\,x + 1$')

plt.show()
