# https://towardsdatascience.com/weighted-linear-regression-2ef23b12a6d7
# and https://gist.github.com/rvaghefi

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the datasets
homoscedastic = pd.read_csv('https://gist.githubusercontent.com/rvaghefi/cb9c3b213e7ec9bc3501eed68aa8dc3f/raw/af218cf7ac0770eefe167a6796c29ab871e83079/homoscedastic.csv')
heteroscedastic = pd.read_csv('https://gist.githubusercontent.com/rvaghefi/cb9c3b213e7ec9bc3501eed68aa8dc3f/raw/af218cf7ac0770eefe167a6796c29ab871e83079/heteroscedastic.csv')

# Generate bias vector
b = np.ones(homoscedastic.shape[0])

# solve linear regression and find residuals
X1 = np.c_[b, homoscedastic[['X1', 'X2', 'X3']].values]
y1 = homoscedastic['y'].values
w1 = np.linalg.inv(X1.T @ X1) @ X1.T @ y1
y_pred1 = X1 @ w1
res1 = y1 - y_pred1

# solve linear regression and find residuals
X2 = np.c_[b, heteroscedastic[['X1', 'X2', 'X3']].values]
y2 = heteroscedastic['y'].values
w2 = np.linalg.inv(X2.T @ X2) @ X2.T @ y2
y_pred2 = X2 @ w2
res2 = y2 - y_pred2

# plot the results
plt.figure(figsize=(10,3.75))
plt.subplot(1,2,1)
plt.plot([0,8], [0, 0], '--', color='salmon')
plt.plot(y_pred1, res1, '.', color="#A3A500")
plt.title('Homoscedasticity')
plt.grid(linestyle=':')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.xlim([0, 8])
plt.ylim([-.2, .2])
plt.subplot(1,2,2)
plt.plot([0,8], [0, 0], '--', color='salmon')
plt.plot(y_pred2, res2, '.',color="#00BF7D")
plt.title('Heteroscedasticity')
plt.grid(linestyle=':')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.xlim([0, 8])
plt.ylim([-.2, .2])
plt.show()