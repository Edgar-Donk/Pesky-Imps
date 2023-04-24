# https://ece.uwaterloo.ca/~dwharder/NumericalAnalysis/06LeastSquares/extrapolation/complete.html

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

data = np.array([(0.3, 0.7), (0.5, 0.6), (0.8, 0.4), (1.2, 0.2), (1.6, -0.1)])

fit1 = np.polyfit(data[:,0], data[:,1] ,1)
fitp = np.polyfit(data[:,0], data[:,1] ,4)

line = np.poly1d(fit1)
poly = np.poly1d(fitp)
new_points = np.linspace(0.2,2)
y_line = line(new_points)
y_poly = poly(new_points)
e_point = line(2)

plt.plot(new_points, y_line, 'g', label='least squares fit')
plt.plot(new_points, y_poly, 'r', label='polynomial fit')
plt.scatter(data[:,0], data[:,1], fc='none', ec='k', label='data points')
plt.scatter(2, e_point, fc='none', ec='g', label='projected point')


plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title('Compare Polynomial and \nLeast Squares Fit')
plt.legend()

plt.show()
#plt.savefig('../../figures/extrap_intro.png')

'''
min and max x-values
min(data[:,0])
max(data[:,0])
'''
