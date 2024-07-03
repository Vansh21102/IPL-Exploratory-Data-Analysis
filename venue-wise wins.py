import pandas as pd
import os
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ipl_matches.csv')

print(df['venue'].unique())

to_drop = ['umpire1','umpire2','umpire3','id','date','city']

df.drop(to_drop, inplace = True, axis = 1)

plt.subplots_adjust(left= 0.3, right= 0.9, bottom=0.1, top=0.9)

plot = sns.histplot(data = df, y = 'venue', kde = True, hue = 'winner')
plot.set_title('venue-wise wins for all teams')
plot.set_xlabel('wins')
plot.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
plt.show()