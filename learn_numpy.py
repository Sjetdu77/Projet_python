import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from seaborn.categorical import boxplot as bxp
from datetime import datetime as dt
from random import randrange as rdrg
from cycler import cycler

plt.figure(figsize=(12,6))
ax = plt.subplot()

tl = pd.read_excel('.\\data\\TL Brawl.xls', index_col=0)

# Diagramme données continues
#tl = tl[tl['Univers'] == 'Zelda']
#tl = tl.T.iloc[:8]
#col = tl.columns
#ax.plot(tl, 'o-')
#ax.set_ylim(39, 0)
#plt.xlabel("Tier lists")
#plt.ylabel("Position")
#plt.legend(col)

# Diagrammes données discrètes
#a = []
#while len(a) < 10:
#    b = rdrg(37)
#    if b not in a:
#        a.append(b)

#tl = tl.iloc[a].T.iloc[:8]
#col = tl.columns
#ax.plot(tl, 'o-')
#ax.set_ylim(39, 0)
#plt.xlabel("Tier Lists")
#plt.ylabel("Position")
#plt.legend(col)

tl = tl.dropna(how='any', subset=['Position 64']).T.iloc[9:-1]
tl.loc['Position 64'] /= 12
tl.loc['Position Melee'] /= 26
tl.loc['Position Brawl'] /= 38
tl.loc['Position Smash 4'] /= 55
tl.loc['Position Ultimate'] /= 81
col = tl.columns
ax.plot(tl, 'o-')
ax.set_ylim(1, 0)
plt.xlabel("Jeux")
plt.ylabel("Position globale")
plt.legend(col)

# Graphiques à données catégoriques
#g = sbn.countplot(x='Univers', data=tl) # Combien sont-ils représentés

#g = sbn.countplot(x='Tier Brawl', data=tl, order=["SS", "S", "A+", "A-", "B", "C+", "C", "C-", "D", "E", "F"])
# Combien y a-t-il de personnages par tier

#tl = tl[(tl['Univers'] == 'Mario') | (tl['Univers'] == 'Pokémon') | (tl['Univers'] == 'Zelda')]

#g = bxp(x="Univers", y=dt(2013, 4, 25), data=tl)
#plt.ylabel("Position")
#ax.set_ylim(39, 0)

plt.show()
