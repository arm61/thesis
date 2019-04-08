import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette="colorblind")
import matplotlib.gridspec as gridspec

import matplotlib as mpl

mpl.rcParams["xtick.labelsize"] = 8
mpl.rcParams["ytick.labelsize"] = 8
mpl.rcParams["axes.facecolor"] = "w"
mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["xtick.top"] = False
mpl.rcParams["xtick.bottom"] = True
mpl.rcParams["ytick.left"] = True
mpl.rcParams["grid.linestyle"] = ""
mpl.rcParams["legend.fontsize"] = 8
mpl.rcParams["legend.facecolor"] = [1, 1, 1]
mpl.rcParams["legend.framealpha"] = 0.75
mpl.rcParams["axes.labelsize"] = 8
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["axes.edgecolor"] = "k"
mpl.rcParams["axes.titlesize"] = 8


data = np.loadtxt('../data/smallangle/sans2d.txt', unpack=True)

plt.figure(figsize=(5, 25 / 11))
gs = gridspec.GridSpec(1, 1)
ax = plt.subplot(gs[0, 0])
ax.errorbar(data[0], data[1], marker='o', ls='', yerr=data[2])
ax.set_xscale('log')
ax.set_xlabel('$q$/Å$^{-1}$')
ax.set_ylabel('$I(q)$')
plt.tight_layout()
plt.savefig("../reports/figures/smallangle/exp_data.pdf")
plt.close()