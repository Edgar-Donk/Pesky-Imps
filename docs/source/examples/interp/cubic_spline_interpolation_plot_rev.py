import matplotlib.pyplot as plt
import numpy as np
#from cub_spline_interp_rev import cubic_interpolate
from scipy.interpolate import CubicSpline
from math import sin
import seaborn as sns

sns.set_theme()

x = [0.7, 2.8, 4.95, 2*np.pi+0.7]
y = [np.sin(0.7), np.sin(2.8), np.sin(4.95), np.sin(2*np.pi+0.7)]

# show the four given points
plt.scatter(x, y, fc='none', ec='k')

x_new= np.linspace(min(x), max(x), 10000)
#print(x_new)
#y_new = cubic_interpolate(x_new, x, y)
#plt.plot(x_new, y_new, 'y', label='bespoke')

plt.plot(x_new, np.sin(x_new), label='sine')
fk = CubicSpline(x, y, bc_type='not-a-knot')
plt.plot(x_new, fk(x_new), label='not-a-knot')
fp = CubicSpline(x, y, bc_type='periodic')
plt.plot(x_new, fp(x_new), label='periodic')
fc = CubicSpline(x, y, bc_type='clamped')
plt.plot(x_new, fc(x_new), label='clamped')
fn = CubicSpline(x, y, bc_type='natural')
plt.plot(x_new, fn(x_new), label='natural')

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Cubic Spline Interpolation Types')
plt.legend()
plt.show()
#plt.savefig('../../figures/cubic_spline_interp.png')