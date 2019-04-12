import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(palette="colorblind")
import matplotlib as mpl

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

lipids = ['dppc', 'dmpc', 'dlpc']#, 'dmpg']
tail_l = {'dppc': 15, 'dmpc': 13, 'dlpc': 11, 'dmpg': 13.5}
sp = {'dppc': [15, 20, 25, 30],
      'dmpc': [20, 25, 30, 40],
      'dlpc': [20, 25, 30, 35],
      'dmpg': [15, 20, 25, 30]}

pear = {'dppc': np.zeros(4), 'dmpc': np.zeros(4),
        'dlpc': np.zeros(4), 'dmpg': np.zeros(4)}

for i in lipids:
    for j in range(len(sp[i])):
        file_name = '../output/reflectometry1/{}_xray/{}_p_sum_sp{}.txt'.format(i, i, sp[i][j])
        file_open = open(file_name, 'r')
        for line in file_open:
            pear[i][j] = float(line)
        file_open.close()

coloring = {15:0, 20:1, 25:2, 30:3, 35:4, 40:5}

fig = plt.figure(figsize=(4.13, 3.51/2))
gs = mpl.gridspec.GridSpec(1, 1)
ax1 = plt.subplot(gs[0, 0])
for j, i in enumerate(lipids):
    plt.plot([tail_l[i]]*4, pear[i], 'o', c=sns.color_palette()[j])

plt.xticks([11, 13, 15])
ax1.set_xticklabels(['DLPC', 'DMPC', 'DPPC'])
ax1.set_ylabel('Total Pearson\ncorrelation\ncoefficient')
ax1.set_xlabel('Phospholipid')
plt.tight_layout()
plt.savefig('../reports/figures/reflectometry1/pear.pdf')
