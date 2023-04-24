import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()
x = np.linspace(0, 3)
plt.figure(figsize=(12,6))
plt.plot(x, x**3 + x**2 -3*x -3)
plt.plot([0,3], [0,0], 'g')
plt.grid(True)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Root by Halving Intervals '+r'$x**3 + x**2 - 3*x - 3$')
plt.show()
#plt.savefig('../../figures/half.png')