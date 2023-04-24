# https://www.terrychan.org/2023/03/how-to-calculate-confidence-intervals-in-python/
import numpy as np
from scipy import stats
# smaller sized samples use bootstrap

# Generate some example data
data = np.random.normal(size=100)

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std = np.std(data, ddof=1)

# Calculate the 95% confidence interval
n = len(data)
se = std / np.sqrt(n)
z = stats.norm.ppf(0.975)
ci = (mean - z * se, mean + z * se)

print("Sample mean:", mean)
print("Standard deviation:", std)
print("95% Confidence interval:", ci)