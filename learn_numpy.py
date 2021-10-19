import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from seaborn.categorical import boxplot as bxp
from datetime import datetime as dt

plt.figure(figsize=(12,6))
ax = plt.subplot()

tl = pd.read_excel('.\\data\\TL Brawl.xls', index_col=0)

#g = sbn.countplot(x='Univers', data=tl)
g = sbn.countplot(x='Tier Brawl', data=tl, order=["SS", "S", "A+", "A-", "B", "C+", "C", "C-", "D", "E", "F"])

#tl = tl.dropna(how='any', subset=['Position 64']).T.iloc[9:]
#tl.loc['Position 64'] = tl.loc['Position 64'] / 12
#tl.loc['Position Melee'] = tl.loc['Position Melee'] / 26
#tl.loc['Position Brawl'] = tl.loc['Position Brawl'] / 38
#tl.loc['Position Smash 4'] = tl.loc['Position Smash 4'] / 55
#tl.loc['Position Ultimate'] = tl.loc['Position Ultimate'] / 81

#col = tl.columns
#ax.plot(tl, 'o-')
#ax.set_ylim(1, 0)
#plt.xlabel("Jeux")
#plt.ylabel("Position globale")
#plt.legend(col)

#g = bxp(x="Univers", y=dt(2008, 9, 1), data=tl)

plt.show()
