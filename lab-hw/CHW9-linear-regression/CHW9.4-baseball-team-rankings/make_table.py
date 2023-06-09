

import numpy as np
import pandas as pd
from collections import OrderedDict

data = pd.read_csv('GL2021.csv')
data=data.drop(labels=['Game_Date','Game_Number','Day_of_Week','Visiting_League','Visiting_Game_Number','Home_League','Home_Game_Number','Day_Night','Game_Length'],axis=1)
df=pd.DataFrame(data)
VT=df['Visiting_Team'].tolist()
VisitingTeams=list(OrderedDict.fromkeys(VT))
HT=df['Home_Team'].tolist()
HomeTeams=list(OrderedDict.fromkeys(HT))
Teams= VisitingTeams
Table = np.array(df)
for i in range(len(Table)):
	Table[i,0] = Teams.index(data['Visiting_Team'][i])
	Table[i,1] = Teams.index(data['Home_Team'][i])