import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

def lin_interp(x0, y0, x1, y1, x):
    return y0 + (x - x0)*(y1 - y0)/(x1 - x0)

x = [2, 4, 6,  8,  10, 12, 14, 16, 18, 20]
y = [4, 7, 11, 16, 22, 29, 38, 49, 63, 80]

xi = 13
yi = lin_interp(x[5],y[5],x[6],y[6], xi)

#create plot of x vs. y
plt.plot(x, y, '-ob')
plt.plot(xi, yi, 'or')
plt.text(xi * (1 + 0.02), yi * (1 - 0.04), (xi, yi), c='r')
plt.text(x[5] * (1 + 0.02), y[5] * (1 - 0.05), (x[5], y[5]), c='b')
plt.text(x[6] * (1 + 0.02), y[6] * (1 - 0.03), (x[6], y[6]), c='b')

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Linear Interpolation')

plt.show()
#plt.savefig('../../figures/lin_interp.png')

