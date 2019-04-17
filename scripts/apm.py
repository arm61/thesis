import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(palette="colorblind")
import matplotlib as mpl
import pandas as pd

data = pd.read_csv('../data/reflectometry2/surf_iso.csv')

data_sorted = data.sort_values(['apm'])

mpl.rcParams["xtick.labelsize"] = 10
mpl.rcParams["ytick.labelsize"] = 10
mpl.rcParams["axes.facecolor"] = "w"
mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["xtick.top"] = False
mpl.rcParams["xtick.bottom"] = True
mpl.rcParams["ytick.left"] = True
mpl.rcParams["grid.linestyle"] = "--"
mpl.rcParams["legend.fontsize"] = 10
mpl.rcParams["legend.facecolor"] = [1, 1, 1]
mpl.rcParams["legend.framealpha"] = 0.75
mpl.rcParams["axes.labelsize"] = 10
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["axes.edgecolor"] = "k"
mpl.rcParams["axes.titlesize"] = 10

plt.figure(figsize=(4.13, 3.51*0.5))
plt.plot(data_sorted['apm'], data_sorted['sp'])
plt.ylim([0, 80])
#plt.xticks([40, 50, 60, 70, 80])
plt.ylabel('$\pi$/mNm$^{-1}$')
plt.xlabel('Area per molecule/Å$^{2}$')
plt.tight_layout()
plt.savefig('../reports/figures/reflectometry2/apm.pdf', bbox_inches='tight', pad_inches=0.1)
#plt.show()
