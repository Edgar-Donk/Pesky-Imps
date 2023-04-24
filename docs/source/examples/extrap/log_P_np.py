import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25])
y = np.array([3, 6, 9, 12, 15 ])

log_x = np.log(x)
log_y = np.log(y)

coefs = np.polyfit(log_x, y, 1)
#print(coefs)
pcoeffs = poly.polyfit(log_x, y, 1)

c = 7.26 * log_x - 9.64
pc = pcoeffs[1] * log_x + pcoeffs[0]
plt.plot(log_x, y, "o")
plt.plot(log_x, c)
plt.plot(log_x, pc, 'y')

plt.show()


