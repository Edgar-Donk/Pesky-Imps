import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


languages = ['C#', 'Go', 'Ruby', 'SQL']
avg_salary = [78, 83, 84, 75]
candidates = [80,87,79, 75]

# Define Dataframe
hr = pd.DataFrame(dict(language =languages,avg_salary=avg_salary, candidates=candidates  ))

# Define variables for chart
languages = hr['language']
avg_salary = hr['avg_salary']
candidates = hr['candidates']
'''
# Draw the graph
plt.scatter(avg_salary, candidates);

# Loop through the data points
for i, language in enumerate (languages):
    plt.text(avg_salary[i]+0.2, candidates[i]+0.2, language)

plt.xlim (70, 90)
plt.ylim (70, 90)
'''
# Keyword arguments for styling the plot
kwargs = dict (linestyle='--', color='b', marker ='o', linewidth=1.2, markersize=13)

# Draw the plot
line = sns.lineplot(x = 'avg_salary', y = 'candidates', data=hr,**kwargs)

# Annotate label points
for i, language in enumerate (languages):
    plt.annotate(language, (avg_salary[i]+0.7, candidates[i]+0.5) )
line.set_xlim (70, 90)
line.set_ylim (70, 90)


plt.show()