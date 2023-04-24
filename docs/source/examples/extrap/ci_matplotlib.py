from matplotlib import pyplot as plt
import numpy as np
# 95% confidence is x¯±1.96∗√(s/n)
#some example data
x = np.linspace(0.1, 9.9, 20)
y = 3.0 * x
#some confidence interval
ci = 1.96 * np.std(y, dtype=np.float64)/np.sqrt(len(x))
#ci = 0.1 * np.std(y) / np.mean(y)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.fill_between(x, (y-ci), (y+ci), color='b', alpha=.1)

plt.show()