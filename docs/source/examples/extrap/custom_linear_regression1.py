import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
y = a + bx

b = (nsumxy - sumx sumy)/(nsumx² - (sumx)²)
a = (sumy- bsumx)/n
'''

def lin_regress(X, Y):
    n = X.shape[0]
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X*Y)
    sum_X2 = np.sum(X*X)
    b = (n * sum_XY - sum_X * sum_Y)/(n * sum_X2 - sum_X * sum_X)
    a = (sum_Y - b * sum_X)/n
    return a, b

sns.set_theme()

X = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8,
              2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8])
Y = np.array([5.06, 5.01, 5.12, 5.13, 5.14, 5.16, 5.25, 5.17, 5.24, 5.46,
              5.40, 5.57, 5.47, 5.53, 5.61, 5.59, 5.61, 5.75, 5.68, 5.80])

a, b = lin_regress(X, Y)
print(a,b)
xnew = np.linspace(X[0], X[-1], len(X)*10)
yhat = b * xnew + a
yh = b * X + a
R = yh - Y

plt.figure(2)
plt.plot(X, R, 'b.', label='residuals')
plt.hlines(0,X[0],X[-1], colors='green', linestyle='dashed', label='$y = 0$')
plt.xlabel('x')
plt.ylabel('Residual $\hat{y} - y$')
plt.legend()
plt.title('Residuals\n', fontsize=18)
plt.suptitle('should be random either side', fontsize=12, y=0.92)

plt.figure(1)
plt.plot(X, Y, 'b.', label='data points')
plt.plot(xnew, yhat, 'r', label='custom fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(f'Custom Linear Regression\n$ y = {b:.4}\,x + {a:.4}$')



#plt.show()


