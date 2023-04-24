# https://web.stanford.edu/class/stats110/notes/Chapter7/Inference.html

import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
from scipy.stats import t as t_dbn
from scipy.stats import norm as normal_dbn

def fit_least_squares(X, Y):
    '''
    linear regression gives line as y = a + bx
    a is beta_hat_0
    b is beta_hat_1
    sigma_hat is
    '''
    X = np.asarray(X)
    n = X.shape[0]
    Y = np.asarray(Y)
    X_bar = np.mean(X)
    Y_bar = np.mean(Y)

    beta_hat_1 = (np.sum((X - X_bar) * (Y - Y_bar)) /
                  np.sum((X - X_bar)**2))
    beta_hat_0 = Y_bar - beta_hat_1 * X_bar

    resid = Y - beta_hat_0 - beta_hat_1 * X
    sigma_hat = np.sqrt(np.sum(resid**2) / (n - 2))

    return np.array([beta_hat_0, beta_hat_1]), sigma_hat, resid

X = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8,
              2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8])
Y = np.array([5.06, 5.01, 5.12, 5.13, 5.14, 5.16, 5.25, 5.17, 5.24, 5.46,
              5.40, 5.57, 5.47, 5.53, 5.61, 5.59, 5.61, 5.75, 5.68, 5.80])
f = plt.figure(figsize=(8,8))
ax = f.gca()
ax.scatter(X, Y)
ax.set_xlabel('Weight')
ax.set_ylabel('Length')

results = fit_least_squares(X, Y)
#print(results[0], results[1])

X_min, X_max = X.min(), X.max()
beta_hat_0, beta_hat_1 = results[0]
Y_max = beta_hat_0 + beta_hat_1 * X_max
Y_min = beta_hat_0 + beta_hat_1 * X_min
#print('X_min, X_max, Y_min, Y_max', X_min, X_max, Y_min, Y_max)
ax.plot([X_min, X_max], [Y_min, Y_max], 'k--')

#plt.show()

