# https://towardsdatascience.com/weighted-linear-regression-2ef23b12a6d7
# and https://gist.github.com/rvaghefi

import numpy as np
import matplotlib.pyplot as plt

# set the seed
np.random.seed(561)

# generate a single feature randomly
X0 = np.random.rand(100)

# actual interception and slope of linear regression
intercept = 2
slope = 5

# generate random observation noise (error)
# noise variance is a function of the feature (heteroscedastic noise)
noise = 3*np.abs(X0)*np.random.randn(X0.shape[0])

# generate the response variable
y = slope*X0 + intercept + noise

# generate the augmented feature matrix (bias + feature)
X = np.c_[np.ones(X0.shape[0]),X0]

# solution of linear regression
w_lr = np.linalg.inv(X.T @ X) @ X.T @ y

# calculate residuals
res = y - X @ w_lr

# estimate the covariance matrix
C = np.diag(res**2)

# solution of weighted linear regression
w_wlr = np.linalg.inv(X.T @ np.linalg.inv(C) @ X) @ (X.T @ np.linalg.inv(C) @ y)

# generate the feature set for plotting
X_p = np.c_[np.ones(2), np.linspace(X0.min(), X0.max(), 2)]

# plot the results
plt.plot(X0, y, 'b.', label='Observations')
plt.plot(X_p[:,1], X_p @ w_lr, 'r-', label='Linear Regression')
plt.plot(X_p[:,1], X_p @ w_wlr, 'g-', label='Weighted Linear Regression')
plt.plot(X_p[:,1], X_p @ [intercept, slope], 'm--', label='Actual Regression')
plt.grid(linestyle=':')
plt.ylabel('Response')
plt.xlabel('Feature')
plt.legend()
plt.show()