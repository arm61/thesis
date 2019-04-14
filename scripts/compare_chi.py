import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette="colorblind")
import matplotlib.gridspec as gridspec

import matplotlib as mpl
import pandas as pd

mpl.rcParams["xtick.labelsize"] = 10
mpl.rcParams["ytick.labelsize"] = 10
mpl.rcParams["axes.facecolor"] = "w"
mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["xtick.top"] = False
mpl.rcParams["xtick.bottom"] = True
mpl.rcParams["ytick.left"] = True
mpl.rcParams["grid.linestyle"] = ""
mpl.rcParams["legend.fontsize"] = 10
mpl.rcParams["legend.facecolor"] = [1, 1, 1]
mpl.rcParams["legend.framealpha"] = 0.75
mpl.rcParams["axes.labelsize"] = 10
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["axes.edgecolor"] = "k"
mpl.rcParams["axes.titlesize"] = 10

which = ['real', 'real_rand']
#
plt.figure(figsize=(4.13, 3.51*0.5))
gs = gridspec.GridSpec(1, 1)
ax = plt.subplot(gs[0, 0])
for k, a in enumerate(which):
    for i in range(1, 6):
        if a == 'real_rand_em' and i == 2:
            continue
        if a == 'real_em' and i == 3:
            continue
        if 'em' in a:
            ss = 107
        else:
            ss = 106
        data3 = pd.read_csv('../data/smallangle/best_real/{}/best{}.out'.format(a, i), delim_whitespace=True, header=None, skiprows=ss)
        h = np.array([])
        b = np.array([])
        for j in range(data3[3].size-2):
            h = np.append(h, float(data3[3][j][:-1]))
            b = np.append(b, float(data3[0][j]))
        if i == 1:
            ax.plot(b+1, h, '-', c=sns.color_palette()[k], label=a)
        else:
            ax.plot(b+1, h, '-', c=sns.color_palette()[k])
        print(a, i, b[0], h[0])
ax.set_xlabel('Iterations')

ax.set_xlim([1, 500])
ax.set_ylim([2000, 5000])
ax.set_xscale('log')
ax.set_ylabel('$\zeta$')
plt.tight_layout()
plt.savefig("../reports/figures/smallangle/comparechi.pdf")
plt.close()
