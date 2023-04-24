# optimize non-convex objective function
from numpy import arange
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# objective function
def objective(x):
 return (x - 2.0) * x * (x + 2.0)**2.0

# minimize the function
result = minimize_scalar(objective, method='brent')
# summarize the result
opt_x, opt_y = result['x'], result['fun']
print('Optimal Input x: %.6f' % opt_x)
print('Optimal Output f(x): %.6f' % opt_y)
print('Total Evaluations n: %d' % result['nfev'])
# define the range
r_min, r_max = -3.0, 2.5
# prepare inputs
inputs = arange(r_min, r_max, 0.1)
# compute targets
targets = [objective(x) for x in inputs]
# plot inputs vs target
plt.plot(inputs, targets, '--', label='function')
# plot the optima
plt.plot([opt_x], [opt_y], 's', color='r', label='result')

plt.title('Non-Convex Univariate Function \n $x(x - 2.0)(x+2.0)^2$')
plt.xlabel(r'$x$')
plt.ylabel(r'$F(x)$')
plt.legend()
# show the plot
#plt.show()
plt.savefig('../../figures/non_convex_plot.png')