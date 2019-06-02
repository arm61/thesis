import MDAnalysis as mda
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
mpl.rcParams["grid.linestyle"] = ""
mpl.rcParams["legend.fontsize"] = 10
mpl.rcParams["legend.facecolor"] = [1, 1, 1]
mpl.rcParams["legend.framealpha"] = 0.75
mpl.rcParams["axes.labelsize"] = 10
mpl.rcParams["axes.linewidth"] = 1
mpl.rcParams["axes.edgecolor"] = "k"
mpl.rcParams["axes.titlesize"] = 10

import sys

sp = sys.argv[1]

data = np.loadtxt('../output/reflectometry2/dspc_{}/waters_slipids_{}.txt'.format(sp, sp))
data_h = np.loadtxt('../output/reflectometry2/dspc_{}/heads_slipids_{}.txt'.format(sp, sp))
data_t = np.loadtxt('../output/reflectometry2/dspc_{}/tails_slipids_{}.txt'.format(sp, sp))
def get_value(file):
    f = open(file, "r")
    for line in f:
        k = line
    if "^" in k:
        l = k.split("$")[1].split("^")[0]
    else:
        l = k.split("$")[1].split("\\pm")[0]
    return float(l)

dh = get_value('../output/reflectometry2/dspc_{}/dspc_{}-d_h_{}.tex'.format(sp, sp, sp))
phih = get_value('../output/reflectometry2/dspc_{}/dspc_{}-phih_{}.tex'.format(sp, sp, sp))
from scipy.optimize import curve_fit

def rough(x, a):
    l1 = np.array([a, 0, 0, 0])
    l2 = np.array([dh, 0.03283*phih/100, 0, 0])
    l3 = np.array([0, 0.03283, 0, 0])
    layers = np.array([l1, l2, l3])
    from scipy.stats import norm
    # work out the step in SLD at an interface
    delta_rho = layers[1:, 1] - layers[:-1, 1]
    sld = np.ones_like(x, dtype=float) * layers[0, 1]
    # the roughness of each step
    sigma = np.clip(layers[1:, 3], 1e-3, None)
    zed = np.asfarray(x)
    dist = np.cumsum(layers[:-1, 0])
    # accumulate the SLD of each step.
    for i in range(np.size(layers, 0) - 2 + 1):
        sld += delta_rho[i] * norm.cdf(zed, scale=sigma[i], loc=dist[i])
    return sld


dd, ss = curve_fit(rough, data[0], data[1], bounds=((-25), (15)))

fig, ax2 = plt.subplots(figsize=(4.13, 3.51))
ax2.errorbar(data_h[0], data_h[1], yerr=data_h[2], marker='o', color=sns.color_palette()[2])
ax2.errorbar(data_t[0], data_t[1], yerr=data_t[2], marker='o', color=sns.color_palette()[3])
ax = ax2.twinx()
ax.errorbar(data[0], data[1], yerr=data[2], marker='o', color=sns.color_palette()[0])
x = np.linspace(data[0][0], data[0][-1], 10000)
ax.plot(x, rough(x, dd[0]), color=sns.color_palette()[1])
plt.xlim([-50, 50])
ax.set_ylabel('Intrinsic density of water/Å$^{-3}$')
ax2.set_ylabel('Intrinsic density of lipid/Å$^{-3}$')
ax.set_ylim([0, 0.04])
ax2.set_ylim([0, 0.0025])
ax2.set_xlabel('$z$/Å')
plt.tight_layout()
plt.savefig('../reports/figures/reflectometry2/water_{}.pdf'.format(sp))
