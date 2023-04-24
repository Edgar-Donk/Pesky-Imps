import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

f = lambda r: 2 * (np.pi*r**2 + 50/r)
df = lambda r:  4*np.pi*r -100/r**2

x = np.linspace(1.5,2.5)

plt.plot(x, f(x), 'c-', label='function')
plt.plot(x, df(x), 'm-', label='1st derivative')
plt.hlines(0, 1.5,2.5,'g', label='x-axis')

plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

plt.show()
