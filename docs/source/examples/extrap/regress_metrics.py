# https://www.dataquest.io/blog/understanding-regression-error-metrics/

import pandas as pd

df = pd.read_csv("../../csv/Video_Games_Sales_as_at_22_Dec_2016.csv")
df = df[df['Critic_Score'].notna()]
df = df[df['User_Score'].notna()]
# user score has 'tbd' entries
df.isnull().sum()
df.info()
# User_Score showed as object
df['User_Score'] = pd.to_numeric(df['User_Score'], errors='coerce')
# showed warning
df.loc[pd.to_numeric(df['User_Score'], errors='coerce').isna(), 'User_Score']
df.info()
#print(df.head)
from sklearn import linear_model
lm = linear_model.LinearRegression()
# clean up data before linear regression
# only keep those that are complete

df.isnull().sum()
X = (df.Critic_Score, df.User_Score)
sales = df.Global_Sales
# Found input variables with inconsistent numbers of samples: [2, 8099]
lm.fit(X, sales)

# MAE mean absolute error, residual
# regression line
# yhat = a + bx
# actual y
# residual = y - yhat

mae_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mae_sum += abs(sale - prediction)
mae = mae_sum / len(sales)

print(mae)

# mse mean squared errors

mse_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mse_sum += (sale - prediction)**2
mse = mse_sum / len(sales)

print(mse)
>>> [ 3.53926581 ]

# mape mean absolute percentage errors
# residual / actual

mape_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mape_sum += (abs((sale - prediction))/sale)
mape = mape_sum/len(sales)

print(mape)
>>> [ 5.68377867 ]

# mpe mean percentage error

mpe_sum = 0
for sale, x in zip(sales, X):
    prediction = lm.predict(x)
    mpe_sum += ((sale - prediction)/sale)
mpe = mpe_sum/len(sales)

print(mpe)
>>> [-4.77081497]


