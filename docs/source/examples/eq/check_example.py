import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

f = lambda x: x**3 + x**2 - 3*x - 3

xx = np.linspace(-2.5, 2.5)
yy = f(xx)

plt.plot(xx, f(xx), 'c-', label='f(x)')
plt.hlines(0, -2.5, 2.5, 'g', label='x-axis')
plt.scatter([-1.732, -1.0, 1.732], [0, 0, 0], fc='none', ec='r', label='roots')
plt.text(-1.732-0.9, 0.3, '(-1.732,0)')
plt.text(1.732-0.8, 0.3, '(1.732,0)')
plt.text(-1.0+0.2, 0.3, '(-1.0,0)')

plt.legend()
plt.title('Example Function for Root Finding\n$x^3 + x^2 - 3x -3$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()
#plt.savefig('../../figures/function_root.png')

