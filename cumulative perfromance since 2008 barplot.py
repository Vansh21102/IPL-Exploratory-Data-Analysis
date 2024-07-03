import pandas as pd
import os
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

GT_pts = 0
MI_pts = 0
CSK_pts = 0
SRH_pts = 0
RCB_pts = 0
LSG_pts = 0
PK_pts = 0
DC_pts = 0
KKR_pts = 0
RR_pts = 0
KXIP_pts = 0
DD_pts = 0
RPS_pts = 0
GL_pts = 0
PW_pts = 0
DCH_pts = 0
KTK_pts = 0
abandoned_match = 0

cumulative_pts_array = []

df = pd.read_csv('ipl_matches.csv')
to_drop = ['umpire1','umpire2','umpire3','id','date','city']
df.drop(to_drop, inplace = True, axis = 1)

df['winner'].fillna('abandoned', inplace = True )
df['winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants', inplace = True)

teams = df['winner'].unique()
teams = np.array(teams)

print(teams)


for i in df['winner']:
    if i == 'Chennai Super Kings':
        CSK_pts = CSK_pts + 1

    elif i == 'Gujarat Titans':
        GT_pts = GT_pts + 1
    
    elif i == 'Mumbai Indians':
        MI_pts = MI_pts + 1

    elif i == 'Lucknow Super Giants':
        LSG_pts = LSG_pts +1

    elif i == 'Rajasthan Royals':
        RR_pts = RR_pts + 1

    elif i == 'Royal Challengers Bangalore':
        RCB_pts = RCB_pts + 1
    
    elif i == 'Delhi Capitals':
        DC_pts = DC_pts + 1

    elif i == 'Kolkata Knight Riders':
        KKR_pts = KKR_pts + 1

    elif i == 'Punjab Kings':
        PK_pts = PK_pts + 1
    
    elif i == 'Sunrisers Hyderabad':
        SRH_pts = SRH_pts + 1

    elif i == 'abandoned':
        abandoned_match = abandoned_match + 1

    elif i == 'Kings XI Punjab':
        KXIP_pts = KXIP_pts + 1

    elif i == 'Delhi Daredevils':
        DD_pts = DD_pts + 1
    
    elif i == 'Rising Pune Supergiants':
        RPS_pts = RPS_pts + 1
    
    elif i == 'Gujarat Lions':
        GL_pts = GL_pts + 1

    elif i == 'Pune Warriors':
        PW_pts = PW_pts + 1

    elif i == "Deccan Chargers":
        DCH_pts = DCH_pts + 1

    elif i == 'Kochi Tuskers Kerala':
        KTK_pts = KTK_pts + 1

cumulative_pts_array.append([CSK_pts, GT_pts, MI_pts, LSG_pts, RR_pts, RCB_pts, DC_pts, KKR_pts, PK_pts, SRH_pts, abandoned_match, KXIP_pts, DD_pts, RPS_pts, GL_pts, PW_pts, DCH_pts, KTK_pts])

cumulative_pts_array = np.array(cumulative_pts_array[0])

# HISTORICAL CHART OF MATCHES ONE BY EACH TEAM SINCE 2008

sns.barplot(x = cumulative_pts_array, y = teams).set_title('IPL team wise match wins since 2008')
plt.show()