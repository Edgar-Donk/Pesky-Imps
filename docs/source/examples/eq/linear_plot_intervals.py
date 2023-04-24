import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

f = lambda x: x**3 + x**2 -3*x -3
pt1 = [1.5,0]
pt2 = [1.5,-1.875]
pt3 = [2,0]
pt4 = [2,3]
pt5 = [1.69,0]
pt6 = [1.69, -0.366]

x = np.linspace(1.4, 2.1)
plt.figure(figsize=(12,6))
plt.plot(x, f(x), label='function')
plt.plot([0,3], [0,0], 'g', label='x-axis')

plt.scatter(pt1[0], pt1[1], fc='none', ec='k')
plt.scatter(pt2[0], pt2[1], fc='none', ec='k')
plt.scatter(pt3[0], pt3[1], fc='none', ec='k')
plt.scatter(pt4[0], pt4[1], fc='none', ec='k')
plt.scatter(pt5[0], pt5[1], fc='none', ec='k')
plt.scatter(pt6[0], pt6[1], fc='none', ec='k')

plt.plot([pt2[0], pt3[0]], [pt2[1], pt2[1]], 'r--')
plt.plot([pt4[0], pt3[0]], [pt4[1], pt2[1]], 'r--')
plt.plot([pt5[0], pt3[0]], [pt5[1], pt3[1]], 'r--')
plt.plot([pt2[0],pt4[0]], [pt2[1],pt4[1]], 'k-', label='secant')

plt.text(pt1[0]-0.01, pt1[1]+0.2, "x1")
plt.text(pt2[0]-0.01, pt2[1]-0.4, "f(x1)")
plt.text(pt3[0]+0.01, pt3[1]+0.2, "x2")
plt.text(pt4[0]-0.01, pt4[1]+0.4, "f(x2)")
plt.text(pt5[0]-0.01, pt5[1]+0.2, "x3")
plt.text(pt6[0]-0.01, pt6[1]-0.5, "f(x3)")
plt.plot(1.732, 0, 'rP', label='root')

plt.ylim((-3,4))
plt.xlim((1.45,2.05))
plt.grid(True)
plt.title('Root by Linear Interpolation Solution '+r'$x^3 + x^2 - 3*x - 3$')
plt.xlabel(r'$x$', color='#1C2833')
plt.ylabel(r'$f(x)$', color='#1C2833')

plt.legend()
plt.show()
#plt.savefig('../../figures/linear_intervals.png')
