import pandas as pd
import os
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('ipl_matches.csv')

df.replace('MA Chidambaram Stadium, Chepauk, Chennai','MA Chidambaram Stadium, Chepauk', inplace = True)
df.replace('MA Chidambaram Stadium','MA Chidambaram Stadium, Chepauk', inplace = True)

df.replace('Rajiv Gandhi International Stadium, Uppal, Hyderabad','Rajiv Gandhi International Stadium, Uppal', inplace = True)
df.replace('Rajiv Gandhi International Stadium','Rajiv Gandhi International Stadium, Uppal', inplace = True)

df.replace('Punjab Cricket Association IS Bindra Stadium','Punjab Cricket Association stadium, Mohali', inplace = True)
df.replace('Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh','Punjab Cricket Association stadium, Mohali', inplace = True)
df.replace('Punjab Cricket Association Stadium, Mohali','Punjab Cricket Association stadium, Mohali', inplace = True)
df.replace('Punjab Cricket Association IS Bindra Stadium, Mohali','Punjab Cricket Association stadium, Mohali', inplace = True)

df.replace('Arun Jaitley Stadium, Delhi','Arun Jaitley Stadium', inplace = True)

df.replace('Brabourne Stadium','Brabourne Stadium, Mumbai', inplace = True)

df.replace('Dr DY Patil Sports Academy','Dr DY Patil Sports Academy, Mumbai', inplace = True)

df.replace('Eden Gardens, Kolkata','Eden Gardens', inplace = True)

df.replace('Himachal Pradesh Cricket Association Stadium, Dharamsala','Himachal Pradesh Cricket Association Stadium', inplace = True)

df.replace('M Chinnaswamy Stadium, Bengaluru','M Chinnaswamy Stadium', inplace = True)
df.replace('M.Chinnaswamy Stadium','M Chinnaswamy Stadium', inplace = True)

df.replace('Maharashtra Cricket Association Stadium, Pune','Maharashtra Cricket Association Stadium', inplace = True)

df.replace('Sawai Mansingh Stadium, Jaipur','Sawai Mansingh Stadium', inplace = True)

df.replace('Wankhede Stadium, Mumbai','Wankhede Stadium', inplace = True)


df['winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants', inplace = True)

df2 = df.where(df['winner'] == 'Rising Pune Supergiants')
df2.dropna(inplace = True)

pd.options.display.max_columns = None
pd.options.display.max_rows = None

to_drop = ['umpire1','umpire2','umpire3','id','date','city']
df2.drop(to_drop, inplace = True, axis = 1)

plt.subplots_adjust(left= 0.3, right= 0.9, bottom=0.1, top=0.9)

plot = sns.histplot(data = df2, y = 'venue', kde = True, hue = 'winner')
plot.set_xlabel('wins')
plot.set_title('venue-wise wins for RPS')
plt.show()