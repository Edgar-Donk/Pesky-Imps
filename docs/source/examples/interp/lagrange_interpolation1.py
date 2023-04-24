# https://lampx.tugraz.at/~hadley/num/ch3/3.php

#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme()
data_fname = 'knot_points2.csv'
# x1,y1
# x2,y2
# ...

def read_data(fname):
    X = []
    Y = []
    with open(fname, 'r') as f:
        for line in f:
            (x, y) = line.split(',')
            X.append(float(x))
            Y.append(float(y))
    return (X, Y)

def lagrange_polynomial(X, Y):
    def L(i):
        return lambda x: np.prod([(x-X[j])/(X[i]-X[j]) for j in range(len(X)) if i != j]) * Y[i]
    Sx = [L(i) for i in range(len(X))]  # summands
    return lambda x: np.sum([s(x) for s in Sx])

# F = lagrange_polynomial(*read_data(data_fname))
(X, Y) = read_data(data_fname)
#print('X, Y', X, Y )
F = lagrange_polynomial(X, Y)


x_range = np.linspace(X[0], X[-1], 100)
#print(map(F, x_range))
#plt.rcParams.update({"text.usetex" : True})
plt.plot(X, Y, 'ro')
plt.plot(x_range, list(map(F, x_range)))
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.title('Lagrange polynomial interpolation\n'+str(data_fname))
plt.grid(True)
plt.show()
#plt.savefig('../../figures/lag_interp_knot_points2.png')