# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

import numpy as np

import matplotlib.pyplot as plt

from scipy import stats

rng = np.random.default_rng()

# Generate some data:

x = rng.random(10)

y = 1.6*x + rng.random(10)

# Perform the linear regression:

res = stats.linregress(x, y)

# Coefficient of determination (R-squared):

print(f"R-squared: {res.rvalue**2:.6f}")
# R-squared: 0.717533

# Plot the data along with the fitted line:

plt.plot(x, y, 'o', label='original data')

plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')

plt.legend()

plt.show()