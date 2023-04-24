
# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.04-Lagrange-Polynomial-Interpolation.html

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import seaborn as sns

# numpy polynomials in reverse order
# ax³ + bx² + c
# coefficients polynomials a, b c
# a = np.array([3,7,2])
# p = np.poly1d(a)
# 3 x² + 7 x + 2

sns.set_theme()

x = [0, 1, 2]
y = [1, 3, 2]
P1_coeff = [1,-1.5,.5]
P2_coeff = [0, 2,-1]
P3_coeff = [0,-.5,.5]

# get the polynomial function
P1 = poly.Polynomial(P1_coeff)
P2 = poly.Polynomial(P2_coeff)
P3 = poly.Polynomial(P3_coeff)

x_new = np.arange(-1.0, 3.1, 0.1)

fig = plt.figure(figsize = (10,8))
plt.plot(x_new, P1(x_new), 'b', label = 'P1')
plt.plot(x_new, P2(x_new), 'y', label = 'P2')
plt.plot(x_new, P3(x_new), 'g', label = 'P3')

L = P1*y[0] + P2*y[1] + P3*y[2]


plt.plot(x, np.ones(len(x)), 'ko', x, np.zeros(len(x)), 'ko', label='Basis Polynomials')
plt.plot(x_new, L(x_new), 'r', x, y, 'ro', label='Interpolation')
plt.scatter(0, 1, fc='r', ec='k', s=60, label='P1 and Interpolation')
plt.title('Lagrange Basis and Interpolation Polynomials')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()
#plt.savefig('../../figures/lagrange_basis.png')


'''
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, L(x_new), 'b', x, y, 'ro')
plt.title('Lagrange Interpolation Polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
#plt.show()
plt.savefig('lagrange_poly.png')


from scipy.interpolate import lagrange

f = lagrange(x, y)

fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial scipy')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
#plt.show()
'''