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

data = pd.read_csv('../data/smallangle/cta_fake.fit', delim_whitespace=True, header=None)

data[2] = data[2] - data[2].min()
data[3] = data[3] - data[3].min()
data[4] = data[4] - data[4].min()

def rotation(a, b, c, d, e, f, data):
    l = np.sin(a) * np.cos(b)
    m = np.sin(a) * np.sin(b)
    n = np.cos(a)
    k = c
    rm = np.zeros((3,3))
    rm[0][0] = l * l + (m * m + n * n) * np.cos(k)
    rm[0][1] = l * m * (1 - np.cos(k)) - n * np.sin(k)
    rm[0][2] = n * l * (1 - np.cos(k)) + m * np.sin(k)
    rm[1][0] = l * m * (1 - np.cos(k)) + n * np.sin(k)
    rm[1][1] = m * m + (n * n + l * l) * np.cos(k)
    rm[1][2] = m * n * (1 - np.cos(k)) - l * np.sin(k)
    rm[2][0] = n * l * (1 - np.cos(k)) - m * np.sin(k)
    rm[2][1] = m * n * (1 - np.cos(k)) + l * np.sin(k)
    rm[2][2] = n * n + (l * l + m * m) * np.cos(k)
    x = rm[0][0] * data[2] + rm[0][1] * data[3] + rm[0][2] * data[4] + d
    y = rm[1][0] * data[2] + rm[1][1] * data[3] + rm[1][2] * data[4] + e
    z = rm[2][0] * data[2] + rm[2][1] * data[3] + rm[2][2] * data[4] + f
    return x, y, z


file_open = open('output.xyz', 'w')
file_open.write('16\n#comment\n')
d = [0, 0, 0, 20]
e = [0, 20, 20, 20]
f = [0, 0, 20, 20]

for l, i in enumerate(np.linspace(0, 2 * np.pi, 4)):
    k = rotation(np.pi, np.pi, i, d[l], e[l], f[l], data)
    for j in range(0, 4):
        file_open.write('{} {} {} {}\n'.format(data[1][j], k[0][j], k[1][j], k[2][j]))
file_open.close()

data2 = pd.read_csv('output.xyz', delim_whitespace=True, header=None, skiprows=2)

data2[1] = data2[1] - data2[1].min()
data2[2] = data2[2] - data2[2].min()
data2[3] = data2[3] - data2[3].min()

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
ax.set_xscale('log')
ax.set_ylabel('$I(q)$')

ax.text(
    0.95,
    0.90,
    r"(d)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=8,
)
plt.tight_layout()
plt.savefig("../reports/figures/smallangle/fake.pdf")
plt.close()
