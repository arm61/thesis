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

import pandas as pd

import sys

num = sys.argv[1]

data = pd.read_csv('../data/smallangle/best_real/best{}.fit'.format(num), delim_whitespace=True, header=None, skiprows=2)
data2 = pd.read_csv('../data/smallangle/best_real/best{}.xyz'.format(num), delim_whitespace=True, header=None, skiprows=2)

qs = np.linspace(0.3, 1.5, 100)

intensity = np.zeros_like(qs)
for e, q in enumerate(qs):
    for m in range(0, data2[1].size-1):
        for n in range(m+1, data2[1].size):
            bi = data.values[data[1] == data2[0][m]][0][5]
            bj = data.values[data[1] == data2[0][n]][0][5]
            xdist = data2[1][n] - data2[1][m]
            ydist = data2[2][n] - data2[2][m]
            zdist = data2[3][n] - data2[3][m]
            r_mn = np.sqrt(np.square(xdist) + np.square(ydist) + np.square(zdist))
            intensity[e] += bi * bj * np.sin(
                r_mn * q) / (r_mn * q)
    if intensity[e] < 0:
        intensity[e] = 0

plt.figure(figsize=(5, 25 / 11))
gs = gridspec.GridSpec(1, 1)
ax = plt.subplot(gs[0, 0])
ax.plot(qs, intensity, '-')
ax.set_xlabel('$q$/Å$^{-1}$')
ax.set_ylabel('$I(q)$')

ax.text(
    0.95,
    0.90,
    r"run {}".format(num),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax.transAxes,
    size=12,
)

data3 = np.loadtxt('../data/smallangle/sans2d.txt', unpack=True)

ax.errorbar(data3[0], data3[1], marker='o', ls='', yerr=data3[2])

ax.set_xscale('log')

plt.tight_layout()
plt.savefig("../reports/figures/smallangle/real_assess{}.pdf".format(num))
plt.close()
