import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.DataFrame({'year':['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000'],
                   'count':[96,184,148,154,160,149,124,274,322,301,300]})
df['year'] = df['year'].astype(float)
X = sm.add_constant(df['year'].values)
ols_model = sm.OLS(df['count'].values, X)
est = ols_model.fit()
out = est.conf_int(alpha=0.05, cols=None)

fig, ax = plt.subplots()
df.plot(x='year',y='count',linestyle='None',marker='s', ax=ax)
y_pred = est.predict(X)
x_pred = df.year.values
ax.plot(x_pred,y_pred)

pred = est.get_prediction(X).summary_frame()
ax.plot(x_pred,pred['mean_ci_lower'],linestyle='--',color='blue')
ax.plot(x_pred,pred['mean_ci_upper'],linestyle='--',color='blue')

# Alternative way to plot
def line(x,b=0,m=1):
    return m*x+b

ax.plot(x_pred,line(x_pred,est.params[0],est.params[1]),color='blue')

plt.show()