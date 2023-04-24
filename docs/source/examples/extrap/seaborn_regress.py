# https://seaborn.pydata.org/tutorial/regression.html

# The two functions that can be used to visualize a linear fit are regplot() and lmplot().

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# In the simplest invocation, both functions draw a scatterplot of two variables,
# x and y, and then fit the regression model y ~ x and plot the resulting regression
# line and a 95% confidence interval for that regression

#tips = sns.load_dataset("tips")
#sns.regplot(x="total_bill", y="tip", data=tips)
# interchangeable
# sns.lmplot(x="total_bill", y="tip", data=tips)

#plt.show()

# These functions draw similar plots, but regplot() is an axes-level function,
# and lmplot() is a figure-level function. Additionally, regplot() accepts the
# x and y variables in a variety of formats including simple numpy arrays, pandas.
# Series objects, or as references to variables in a pandas.DataFrame object passed
# to data. In contrast, lmplot() has data as a required parameter and the
# x and y variables must be specified as strings. Finally, only lmplot() has hue
# as a parameter.

# sns.lmplot(x="size", y="tip", data=tips);

# It’s possible to fit a linear regression when one of the variables takes
# discrete values, however, the simple scatterplot produced by this kind of
# dataset is often not optimal

#sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05)

#plt.show()

# A second option is to collapse over the observations in each discrete bin to
# plot an estimate of central tendency along with a confidence interval

#sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)
#plt.show()

# The Anscombe’s quartet dataset shows a few examples where simple linear
# regression provides an identical estimate of a relationship where simple visual
# inspection clearly shows differences. For example, in the first case, the
# linear regression is a good model

anscombe = sns.load_dataset("anscombe")
# no confidence limits
# ci=None

#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           #ci=None, scatter_kws={"s": 80});
# not a good fit
#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           #ci=None, scatter_kws={"s": 80})
# In the presence of these kind of higher-order relationships, lmplot() and
# regplot() can fit a polynomial regression model to explore simple kinds of
# nonlinear trends in the dataset
#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           #order=2, ci=None, scatter_kws={"s": 80})
# A different problem is posed by “outlier” observations that deviate for some
# reason other than the main relationship under study:

#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           #ci=None, scatter_kws={"s": 80})
# In the presence of outliers, it can be useful to fit a robust regression,
# which uses a different loss function to downweight relatively large residuals
#sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           #robust=True, ci=None, scatter_kws={"s": 80})
# The residplot() function can be a useful tool for checking whether the simple
# regression model is appropriate for a dataset. It fits and removes a simple
# linear regression and then plots the residual values for each observation.
# Ideally, these values should be randomly scattered around y = 0

# sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              #scatter_kws={"s": 80})
# If there is structure in the residuals, it suggests that simple linear
# regression is not appropriate:

sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
              scatter_kws={"s": 80})
plt.show()