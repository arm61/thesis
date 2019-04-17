import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette="colorblind")
import matplotlib.gridspec as gridspec

import matplotlib as mpl

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

import pandas as pd

import sys

num = sys.argv[1]
which = sys.argv[2]

data = pd.read_csv('../data/smallangle/best_real/{}/best{}.fit'.format(which, num), delim_whitespace=True, header=None, skiprows=2)
data2 = pd.read_csv('../data/smallangle/best_real/{}/best{}.xyz'.format(which, num), delim_whitespace=True, header=None, skiprows=2)
data3 = np.loadtxt('../data/smallangle/sans2d.txt', unpack=True)


qs = data[0]
bis = np.array([])
bjs = np.array([])
xs = np.array([])
ys = np.array([])
zs = np.array([])
for m in range(0, data2[1].size-1):
    print(m)
    for n in range(m+1, data2[1].size):
        bis = np.append(bis, data.values[data[2] == data2[0][m]][0][5])
        bjs = np.append(bjs, data.values[data[2] == data2[0][n]][0][5])
        xs = np.append(xs, data2[1][n] - data2[1][m])
        ys = np.append(ys, data2[2][n] - data2[2][m])
        zs = np.append(zs, data2[3][n] - data2[3][m])

intensity = np.zeros_like(qs)
for e, q in enumerate(qs):
    print(q, 'doing')
    r_mn = np.sqrt(np.square(xs) + np.square(ys) + np.square(zs))
    intensity[e] = np.sum(bis * bjs * np.sin(
        r_mn * q) / (r_mn * q))
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
    size=8,
)

ax.errorbar(data3[0], data3[1], marker='o', ls='', yerr=data3[2])

ax.set_xscale('log')

plt.tight_layout()
plt.savefig("../reports/figures/smallangle/{}_assess{}.pdf".format(which, num), bbox_inches='tight', pad_inches=0.1)
plt.close()
