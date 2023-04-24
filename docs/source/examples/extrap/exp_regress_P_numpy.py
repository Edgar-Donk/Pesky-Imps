# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions.html
# https://www.delftstack.com/howto/python/logarithmic-and-exponential-curve-fitting-python/

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# let's generate x and y, and add some noise into y
x = np.linspace(0.1, 10, 101)
y = 0.1*np.exp(0.3*x) + 0.1*np.random.random(len(x))

log_x = np.log(x)
log_y = np.log(y)

'''
A = np.vstack([x, np.ones(len(x))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond = None)[0]
alpha = np.exp(log_alpha)
print(f'alpha={alpha}, beta={beta}')
'''

coefs = poly.polyfit(x, log_y, 1)
#print(coefs)

c = np.exp(coefs[0]) * np.exp(coefs[1]*x)

# Let's have a look of the data
#plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.', label='data points')
#plt.plot(x, alpha*np.exp(beta*x), 'r')
plt.plot(x, c, 'r', label='polynomial fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting Linear Regression to \n$0.1 e^{0.3x} + 0.1$ plus some noise')
plt.legend()
plt.show()
