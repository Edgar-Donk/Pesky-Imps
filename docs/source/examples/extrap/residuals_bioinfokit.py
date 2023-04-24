# https://github.com/reneshbedre/bioinfokit
# https://www.reneshbedre.com/blog/learn-to-calculate-residuals-regression.html
from bioinfokit.analys import stat, get_data
import numpy as np
import pandas as pd

df = get_data('plant_richness_lr').data
df.head(2)
'''
   ntv_rich      area
0  1.897627  1.602060
1  1.633468  0.477121
'''
X = df['area']   # independent variable
y = df['ntv_rich']   # dependent variable

from sklearn.linear_model import LinearRegression

X = np.array(X).reshape(-1, 1) # sklearn requires in 2D array
y = np.array(y)
reg = LinearRegression().fit(X, y)

# get regression coefficient (slope)
reg.coef_
# output
#array([0.35573936])

# get y intercept
reg.intercept_
# output
#1.33604

# predict y (y hat) when X 2.5
reg.predict([[2.5]])
# output
#array([2.22539668])


