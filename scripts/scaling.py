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

# strong scaling

N = np.array([1, 2, 4, 8, 16, 32, 64, 128])
t1 = 27651.24
t2 = 13701.68
t4 = 7143.24
t8 = 3684.95
t16 = 1911.52
t32 = 951.98
t64 = 535.78
t128 = 257.43
tN = np.array([t1, t2, t4, t8, t16, t32, t64, t128])

def speed_up(x, p):
    s = 1 - p
    return 1 / (s + p / x)

su = t1 / tN
from scipy.optimize import curve_fit
x = N

plt.figure(figsize=(5, 25 / 11))
gs = gridspec.GridSpec(1, 1)
ax = plt.subplot(gs[0, 0])
popt, pcov = curve_fit(speed_up, x, su)
ax.plot(x, su, 'o', c=sns.color_palette()[0])
ax.plot(x, x, '-', c=sns.color_palette()[1])
x2 = np.linspace(1, 128, 100)

ax.plot(x2, speed_up(x2, popt[0]), c=sns.color_palette()[0])
ax.set_xlabel('Cores')
ax.set_ylabel('Speedup')
plt.tight_layout()
plt.savefig("../reports/figures/smallangle/speedup.pdf")
plt.close()


y = t1 / (N * tN)

plt.figure(figsize=(4.13, 3.51))
gs = gridspec.GridSpec(2, 1)
ax = plt.subplot(gs[0, 0])

ax.plot(x, y, 'o')
ax.set_xlabel('Cores')
ax.set_ylabel('Strong Parallel Efficiency/cores$^{-1}$')
ax.set_xscale('log', basex=2)
ax.set_xticks(N)
ax.set_xticklabels(N)
ax.text(
    0.97,
    0.92,
    "(a)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=8,
)
ax.set_ylim([0.7, 1.1])

# weak scaling

N = np.array([1, 2, 4, 8, 16, 32, 64, 128])
t1 = 218.91
t2 = 212.54
t4 = 223.56
t8 = 231.41
t16 = 235.34
t32 = 250.09
t64 = 253.38
t128 = 257.43
tN = np.array([t1, t2, t4, t8, t16, t32, t64, t128])

x = N
y = t1 / tN

ax = plt.subplot(gs[1, 0])
ax.plot(x, y, 'o')
ax.set_xlabel('Cores')
ax.set_ylabel('Weak Parallel Efficiency')
ax.set_xscale('log', basex=2)
ax.set_xticks(N)
ax.set_xticklabels(N)
ax.text(
    0.97,
    0.92,
    "(b)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=8,
)
ax.set_ylim([0.7, 1.1])
plt.tight_layout()
plt.savefig("../reports/figures/smallangle/scaling.pdf")
plt.close()
