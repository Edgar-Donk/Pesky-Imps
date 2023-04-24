import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme()

def quad_interp(x0, y0, x1, y1, x2, y2, x):
    y = y0 * (x - x1)*(x - x2)/((x0 - x1)*(x0 - x2)) + \
            y1 * (x - x0)*(x - x2)/((x1 - x0)*(x1 - x2)) + \
            y2 * (x - x0)*(x - x1)/((x2 - x0)*(x2 - x1))
    return y


x = [1, 2, 4]
y = [2, 3, -1]

xs = np.linspace(0,5,100)

ys = quad_interp(x[0],y[0],x[1],y[1],x[2],y[2], xs)
#print(ys)

#create plot of x vs. y
plt.plot(x, y, 'or', label='three points')
plt.plot(xs, ys, '-b', label='interpolation')

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Quadratic Interpolation')
plt.legend()

plt.show()
#plt.savefig('../../figures/quad_interp.png')
