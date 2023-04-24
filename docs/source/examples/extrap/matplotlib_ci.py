# https://discuss.python.org/t/whats-the-meaning-of-this-confidence-bands/14445/3

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve and estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
# 1 standard error --> 68% confidence limits
# 1.96 standard errors --> 95% confidence limits (1.96 times y_err)
y_err = (np.array(y)-y_est).std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

#some confidence interval
ci = 1.96 * np.std(y)/np.sqrt(len(x))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, color='magenta', alpha=0.2)
ax.fill_between(x, (y-ci), (y+ci), color='b', alpha=.1)
sns.regplot(x, y)
ax.plot(x, y, 'o', color='tab:brown')

plt.show()