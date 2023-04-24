import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

a = np.array([6, 12, 18, 24, 30])
b = np.array([4, 8, 12, 16, 20])
a_new = np.linspace(a[0], a[-1], num=len(a)*10)

log_a = np.log(a)
log_b = np.log(b)

coefficients = np.polyfit(a, log_b, 1)
pcoefs = poly.polyfit(a, log_b, 1)
print(coefficients, pcoefs)
c = np.exp(1.17) * np.exp(0.06*a)
pc = np.exp(pcoefs[0]) * np.exp(pcoefs[1]*a_new)
plt.plot(a, b, "o")
plt.plot(a, c)
plt.plot(a_new, pc, 'y')

plt.show()