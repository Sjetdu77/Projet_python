import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from seaborn.categorical import boxplot as bxp
from datetime import datetime as dt

plt.figure(figsize=(12,6))
ax = plt.subplot()

tl = pd.read_excel('.\\data\\TL Brawl.xls', index_col=0)

#g = sbn.countplot(x='Univers', data=tl)

tl = tl[tl['Univers'] == 'Mario'].T.iloc[:8]

col = tl.columns

ax.plot(tl, 'o-')
ax.set_ylim(39, 0)
plt.xlabel("Tier lists")
plt.ylabel("Position")
plt.legend(col)

#g = bxp(x="Univers", y=dt(2008, 9, 1), data=tl)

plt.show()
