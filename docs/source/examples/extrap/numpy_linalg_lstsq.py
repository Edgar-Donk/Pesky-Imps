
import numpy as np
import matplotlib.pyplot as plt

# Fit a line, y = mx + c, through some noisy data-points:

x = np.array([0, 1, 2, 3])

y = np.array([-1, 0.2, 0.9, 2.1])

# We can rewrite the line equation as y = Ap, where A = [[x 1]] and p = [[m], [c]].
# Now use lstsq to solve for p:

A = np.vstack([x, np.ones(len(x))]).T
'''
A
array([[ 0.,  1.],
       [ 1.,  1.],
       [ 2.,  1.],
       [ 3.,  1.]])
'''
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# m, c
# (1.0 -0.95) # may vary

_ = plt.plot(x, y, 'o', label='Original data', markersize=10)

_ = plt.plot(x, m*x + c, 'r', label='Fitted line')

_ = plt.legend()

plt.show()