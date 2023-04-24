# https://discuss.codecademy.com/t/how-to-create-a-custom-legend-seaborn/548571
import matplotlib.pyplot as plt
import seaborn as sns

scat=sns.regplot(
        x='age',
        y='charges',
        data=ages_charges,
        truncate=False,
        scatter_kws={'facecolors':color},
        line_kws={
            'alpha':0.8,
            'linewidth':2,
            'label':lin_reg
        } #gives me what I want
    )

#using existing points to put in the legend
dot=scat.scatter(20,562857.83475,edgecolors='#4890c1')
dot2=scat.scatter(39,252568.341850,edgecolors='#4890c1')
dot3=scat.scatter(57,427626.816500,edgecolors='#4890c1')

scat.set(
    title='The Correlation between Age and Charge Amount',
    xlabel='Age',
    ylabel='Amount in Charges (Dollars)'
)



first_legend=plt.legend(
        title='Linear Regression Equation',
        loc='upper right'
    )

ax=plt.gca().add_artist(first_legend)

plt.legend(
  (dot,dot2,dot3),
  ('18-34','35-49','50+'),
  loc='lower right',
  title='Legend'
)

plt.show()