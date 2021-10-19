import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from seaborn.categorical import boxplot as bxp

plt.figure(figsize=(12,6))
#ax = plt.subplot()

tl = pd.read_excel('.\\data\\TL Brawl.xls', index_col=0)

#tl = tl.iloc[:10].T.iloc[:8]
#col = tl.columns

#ax.plot(tl, 'o-')
#ax.set_ylim(39, 0)
#plt.xlabel("Tier lists")
#plt.ylabel("Position")
#plt.legend(col)

g = sbn.countplot(x='Univers', doc=tl)
g = bxp(x="Univers", y='2008-09-01 00:00:00', doc=tl)

plt.show()
