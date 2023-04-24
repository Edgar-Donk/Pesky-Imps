# https://www.delftstack.com/howto/python/logarithmic-and-exponential-curve-fitting-python/

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

x = np.linspace(0.1, 10, 101)
y = 2*x**0.3 + 0.1*np.random.random(len(x))

log_x = np.log(x)
log_y = np.log(y)

pcoeffs = poly.polyfit(log_x, y, 1)
pc = pcoeffs[1] * log_x + pcoeffs[0]

plt.plot(log_x, y, "o", label='log data points')
plt.plot(log_x, pc, 'r', label='log linear fit')

plt.plot(x, y, "co", label='data points')
plt.plot(x, pc, 'm', label='linear fit')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting Linear Regression to \n$2 x^{0.3x}$ plus some noise')
plt.legend()
plt.show()





