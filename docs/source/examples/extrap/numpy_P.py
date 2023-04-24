# https://numpy.org/doc/stable/reference/routines.polynomials.classes.html

from numpy.polynomial import Polynomial as P

p = P([1,2,3])

# Note that there are three parts to the long version of the printout. The first
# is the coefficients, the second is the domain, and the third is the window

p
# Polynomial([1., 2., 3.], domain=[-1,  1], window=[-1,  1], symbol='x')
p.coef
# array([1., 2., 3.])

p.domain
# array([-1,  1])

p.window
# array([-1,  1])

print(p)
# 1.0 + 2.0 x**1 + 3.0 x**2

print(f"{p:unicode}")
# 1.0 + 2.0·x¹ + 3.0·x²

# Fitting is the reason that the domain and window attributes are part of the
# convenience classes. To illustrate the problem, the values of the Chebyshev
# polynomials up to degree 5 are plotted below

import matplotlib.pyplot as plt

from numpy.polynomial import Chebyshev as T

x = np.linspace(-1, 1, 100)

for i in range(6):

    ax = plt.plot(x, T.basis(i)(x), lw=2, label=f"$T_{i}$")


plt.legend(loc="upper left")

plt.show()

# In the range -1 <= x <= 1 they are nice, equiripple functions lying between
# +/- 1. The same plots over the range -2 <= x <= 2 look very different

import matplotlib.pyplot as plt

from numpy.polynomial import Chebyshev as T

x = np.linspace(-2, 2, 100)

for i in range(6):

    ax = plt.plot(x, T.basis(i)(x), lw=2, label=f"$T_{i}$")


plt.legend(loc="lower right")

plt.show()

'''
As can be seen, the “good” parts have shrunk to insignificance. In using Chebyshev
 polynomials for fitting we want to use the region where x is between -1 and 1
 and that is what the window specifies. However, it is unlikely that the data to
 be fit has all its data points in that interval, so we use domain to specify the
 interval where the data points lie. When the fit is done, the domain is first
 mapped to the window by a linear transformation and the usual least squares fit
 is done using the mapped data points. The window and domain of the fit are part
 of the returned series and are automatically used when computing values,
 derivatives, and such. If they aren’t specified in the call the fitting routine
 will use the default window and the smallest domain that holds all the data points.
 This is illustrated below for a fit to a noisy sine curve.
'''

import matplotlib.pyplot as plt

from numpy.polynomial import Chebyshev as T

np.random.seed(11)

x = np.linspace(0, 2*np.pi, 20)

y = np.sin(x) + np.random.normal(scale=.1, size=x.shape)

p = T.fit(x, y, 5)

plt.plot(x, y, 'o')

xx, yy = p.linspace()

plt.plot(xx, yy, lw=2)

p.domain
# array([0.        ,  6.28318531])

p.window
# array([-1.,  1.])

plt.show()