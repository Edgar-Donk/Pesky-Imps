import numpy as np
from scipy import stats
import sys

# This reads in the weight and mortality data to two arrays.
arr = np.loadtxt(sys.argv[1])
Weight = arr[:,-2]
Mortality = arr[:,-1]

# This calculates the regression equation.
slope, intercept, r_value, p_value, std_err = stats.linregress(x=Weight,y=Mortality)

# This calculates the predicted value for each observed value
obs_values = Mortality
pred_values = slope * Weight + intercept

# This prints the residual for each pair of observations
Residual = obs_values - pred_values
print(Residuals)