# https://towardsdatascience.com/weighted-linear-regression-2ef23b12a6d7
# and https://gist.github.com/rvaghefi

import matplotlib.pyplot as plt
import numpy as np

# set the seed
np.random.seed(125)

# generate a single feature randomly
X0 = np.random.rand(500)

# actual interception and slope of linear regression
intercept = 2
slope = 5

# generate random observation noise (error)
noise = np.random.randn(X0.shape[0])
noise = 0.05*noise/np.std(noise)

# generate outlier
outlier = 0.20*np.random.randn(X0.shape[0]) * (np.random.rand(X0.shape[0]) > 0.97)

# generate the response variable
y = slope*X0 + intercept + noise + outlier

# generate the augmented feature matrix (bias + feature)
X = np.c_[np.ones(X0.shape[0]),X0]

# calcualte leverage values hii
H = X @ np.linalg.inv(X.T @ X) @ X.T

# solution of linear regression
w = np.linalg.inv(X.T @ X) @ X.T @ y

# predicted values
y_pred = X @ w

# calcualte residuals
res = y - y_pred

# calculate MSE
mse = np.mean(res**2)

# calculate standardized residuals
res_std = res/np.sqrt(mse*(1-np.diag(H)))

# plot the results
plt.figure(figsize=(10,3.75))
plt.plot([2,7], [0, 0], '--', color='salmon')
plt.plot(y_pred[abs(res_std) < 3], res_std[abs(res_std) < 3], '.',color=[0.57960784, 0.77019608, 0.87372549, .8])
plt.plot(y_pred[abs(res_std) > 3], res_std[abs(res_std) > 3], '.',color='red')
plt.subplots_adjust(left=.285, right=0.715, top=.93, bottom=0.12)
plt.title('Outlier Detection', fontsize=10)
plt.grid(linestyle=':')
plt.xlabel('Predicted Values')
plt.ylabel('Standardized Residuals')
plt.xlim([2, 7])
plt.ylim([-6, 6])
plt.show()