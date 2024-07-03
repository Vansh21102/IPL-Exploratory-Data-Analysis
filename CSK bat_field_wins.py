import pandas as pd
import os
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ipl_matches.csv')

df2 = df.where(df['winner'] == 'Chennai Super Kings')

pd.options.display.max_columns = None
pd.options.display.max_rows = None

to_drop = ['umpire1','umpire2','umpire3','id','date','city']
df2.drop(to_drop, inplace = True, axis = 1)
df2.dropna(inplace = True)


plot = sns.countplot(data = df2, x = 'toss_decision', hue = 'winner')
plot.set_title('CSK wins based on toss decision')
plot.set_ylabel('wins')
plt.show()