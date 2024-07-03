import pandas as pd
import os
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ipl_matches.csv')
to_drop = ['umpire1','umpire2','umpire3','id','date','city']
df['winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants', inplace = True)

df2 = df.where(df['toss_winner'] == 'Chennai Super Kings')
df2.dropna(inplace = True)
df3 = df2.where(df2['winner'] == 'Chennai Super Kings')
df3.dropna(inplace = True)

df4 = df.where(df['toss_winner'] == 'Delhi Capitals')
df4.dropna(inplace = True)
df5 = df4.where(df4['winner'] == 'Delhi Capitals')
df5.dropna(inplace = True)

df6 = df.where(df['toss_winner'] == 'Deccan Chargers')
df6.dropna(inplace = True)
df7 = df6.where(df6['winner'] == 'Deccan Chargers')
df7.dropna(inplace = True)

df8 = df.where(df['toss_winner'] == 'Delhi Daredevils')
df8.dropna(inplace = True)
df9 = df8.where(df8['winner'] == 'Delhi Daredevils')
df9.dropna(inplace = True)

df10 = df.where(df['toss_winner'] == 'Gujarat Lions')
df10.dropna(inplace = True)
df11 = df10.where(df10['winner'] == 'Gujarat Lions')
df11.dropna(inplace = True)

df12 = df.where(df['toss_winner'] == 'Gujarat Titans')
df12.dropna(inplace = True)
df13 = df12.where(df12['winner'] == 'Gujarat Titans')
df13.dropna(inplace = True)

df14 = df.where(df['toss_winner'] == 'Kolkata Knight Riders')
df14.dropna(inplace = True)
df15 = df14.where(df14['winner'] == 'Kolkata Knight Riders')
df15.dropna(inplace = True)

df16 = df.where(df['toss_winner'] == 'Kochi Tuskers Kerala')
df16.dropna(inplace = True)
df17 = df16.where(df16['winner'] == 'Kochi Tuskers Kerala')
df17.dropna(inplace = True)

df18 = df.where(df['toss_winner'] == 'Kings XI Punjab')
df18.dropna(inplace = True)
df19 = df18.where(df18['winner'] == 'Kings XI Punjab')
df19.dropna(inplace = True)

df20 = df.where(df['toss_winner'] == 'Lucknow Super Giants')
df20.dropna(inplace = True)
df21 = df20.where(df20['winner'] == 'Lucknow Super Giants')
df21.dropna(inplace = True)

df22 = df.where(df['toss_winner'] == 'Mumbai Indians')
df22.dropna(inplace = True)
df23 = df22.where(df22['winner'] == 'Mumbai Indians')
df23.dropna(inplace = True)

df24 = df.where(df['toss_winner'] == 'Punjab Kings')
df24.dropna(inplace = True)
df25 = df24.where(df24['winner'] == 'Punjab Kings')
df25.dropna(inplace = True)

df26 = df.where(df['toss_winner'] == 'Pune Warriors')
df26.dropna(inplace = True)
df27 = df26.where(df26['winner'] == 'Pune Warriors')
df27.dropna(inplace = True)

df28 = df.where(df['toss_winner'] == 'Royal Challengers Bangalore')
df28.dropna(inplace = True)
df29 = df28.where(df28['winner'] == 'Royal Challengers Bangalore')
df29.dropna(inplace = True)

df30 = df.where(df['toss_winner'] == 'Rajasthan Royals')
df30.dropna(inplace = True)
df31 = df30.where(df30['winner'] == 'Rajasthan Royals')
df31.dropna(inplace = True)

df32 = df.where(df['toss_winner'] == 'Rising Pune Supergiants')
df32.dropna(inplace = True)
df33 = df32.where(df32['winner'] == 'Rising Pune Supergiants')
df33.dropna(inplace = True)

df34 = df.where(df['toss_winner'] == 'Sunrisers Hyderabad')
df34.dropna(inplace = True)
df35 = df34.where(df34['winner'] == 'Sunrisers Hyderabad')
df35.dropna(inplace = True)

fig, axes = plt.subplots(4,5, sharey= True)
fig.suptitle('wins based on toss decisions', fontsize = 15)
fig.tight_layout(h_pad = 0.7, w_pad = 0.4)
fig.delaxes(axes[3,2])
fig.delaxes(axes[3,3])
fig.delaxes(axes[3,4])



sns.countplot(ax = axes[0,0], data = df3, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[0,0].set_title('Chennai Super Kings', fontsize = 9)

sns.countplot(ax = axes[0,1], data = df5, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[0,1].set_title('Delhi Capitals', fontsize = 9)

sns.countplot(ax = axes[0,2], data = df7, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[0,2].set_title('Deccan Chargers', fontsize = 9)

sns.countplot(ax = axes[0,3], data = df9, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[0,3].set_title('Delhi Daredevils', fontsize = 9)

sns.countplot(ax = axes[0,4], data = df11, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[0,4].set_title('Gujrat Lions', fontsize = 9)

sns.countplot(ax = axes[1,0], data = df13, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[1,0].set_title('Gujrat Titans', fontsize = 9)

sns.countplot(ax = axes[1,1], data = df15, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[1,1].set_title('Kolkata Knight Riders', fontsize = 9)

sns.countplot(ax = axes[1,2], data = df17, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[1,2].set_title('Kochi Tuskers kerala', fontsize = 9)

sns.countplot(ax = axes[1,3], data = df19, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[1,3].set_title('Kings XI Punjab', fontsize = 9)

sns.countplot(ax = axes[1,4], data = df21, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[1,4].set_title('Lucknow Super Giants', fontsize = 9)

sns.countplot(ax = axes[2,0], data = df23, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[2,0].set_title('Mumbai Indians', fontsize = 9)

sns.countplot(ax = axes[2,1], data = df25, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[2,1].set_title('Punjab Kings', fontsize = 9)

sns.countplot(ax = axes[2,2], data = df27, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[2,2].set_title('Pune Warriors', fontsize = 9)

sns.countplot(ax = axes[2,3], data = df29, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[2,3].set_title('Royal Challengers Bangalore', fontsize = 9)

sns.countplot(ax = axes[2,4], data = df31, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[2,4].set_title('Rajasthan Royals', fontsize = 9)

sns.countplot(ax = axes[3,0], data = df33, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[3,0].set_title('Rising Pune Supergiants', fontsize = 9)

sns.countplot(ax = axes[3,1], data = df35, x = 'toss_decision', hue = 'toss_decision').set_ylabel('wins')
axes[3,1].set_title('Sunrisers Hyderabad', fontsize = 9)

plt.show()