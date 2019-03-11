import numpy as np
import MDAnalysis as mda
import os.path


import scipy
import sys

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set(palette="colorblind")


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

ff = sys.argv[1]

sp = sys.argv[2]

if ff == 'berger':
    heads = ['C1', 'C2', 'C3', 'N4', 'C5', 'C6', 'O7', 'P8', 'O9', 'O10', 'O11',
             'C12', 'C13', 'O14', 'C15', 'O16', 'C34', 'O35', 'C36', 'O37']
    waters = ['OW', 'HW1', 'HW2']
    tail_len = 54 - len(heads)
if ff == 'martini':
    heads = ['NC3', 'PO4', 'GL1', 'GL2']
    waters = ['W', 'WP', 'WM']
    tail_len = 8
if ff == 'slipids':
    waters = ['OW', 'HW1', 'HW2']
    heads = ['N', 'C13', 'H13A', 'H13B', 'H13C', 'C14', 'H14A', 'H14B', 'H14C',
           'C15', 'H15A', 'H15B', 'H15C', 'C12', 'H12A', 'H12B', 'C11', 'H11A',
           'H11B', 'P', 'O13', 'O14', 'O11', 'O12', 'C1', 'HA', 'HB', 'C2', 'HS',
           'O21', 'C21', 'O22', 'C3', 'HX', 'HY', 'O31', 'C31', 'O32']
    tail_len = 142 - len(heads)

bin_width = 1.
pdbfile = '../data/reflectometry2/dspc_{}/{}_frame{}.pdb'.format(sp, ff, 1)
u = mda.Universe(pdbfile)
hb = np.zeros((int(np.ceil(u.dimensions[2] / bin_width)), 501))
wb = np.zeros((int(np.ceil(u.dimensions[2] / bin_width)), 501))
tb = np.zeros((int(np.ceil(u.dimensions[2] / bin_width)), 501))
j = 0
for i in range(1, 11):
    print(ff, sp, i)
    pdbfile = '../data/reflectometry2/dspc_{}/{}_frame{}.pdb'.format(sp, ff, i)
    u = mda.Universe(pdbfile)
    for ts in u.trajectory:
        for atom in range(len(u.atoms)):
            if u.atoms[atom].name in heads:
                hb[int(u.atoms[atom].position[2] / bin_width), j] += 1
            elif u.atoms[atom].name in waters:
                wb[int(u.atoms[atom].position[2] / bin_width), j] += 1
            else:
                tb[int(u.atoms[atom].position[2] / bin_width), j] += 1
        print(i, j)
        j += 1
wb = wb[::-1, :]
if ff == 'martini':
    wb = wb * 4
hb = hb[::-1, :]
tb = tb[::-1, :]

wab = wb / (float(len(waters)))
hab = hb / (float(len(heads)))
tab = tb / (float(tail_len))
water_bin = wb / (float(len(waters)) * u.dimensions[0] * u.dimensions[1] * bin_width)
head_bin = hb / (float(len(heads)) * u.dimensions[0] * u.dimensions[1] * bin_width)
tail_bin = tb / (float(tail_len) * u.dimensions[0] * u.dimensions[1] * bin_width)

av_w = np.average(water_bin, axis=1)
av_h = np.average(head_bin, axis=1)

st_w = np.std(water_bin, axis=1) / water_bin.shape[1]
st_h = np.std(head_bin, axis=1) / head_bin.shape[1]

wph = np.divide(av_w, av_h, out=np.zeros_like(av_w), where=np.logical_or(av_h!=0, av_w!=0))
wphs = np.divide(st_w, st_h, out=np.zeros_like(st_w), where=np.logical_or(st_h!=0, st_w!=0))
wph[np.isinf(wph)] = 0
wphs[np.isinf(wphs)] = 0

print(wph, wphs)

fig, ax = plt.subplots(figsize=(5, 25/11))
ax1 = ax.twinx()
ax.errorbar(range(int(np.ceil(u.dimensions[2] / bin_width))), np.average(head_bin, axis=1)*10000, yerr=np.std(head_bin, axis=1)*10000 / head_bin.shape[1], c=sns.color_palette()[0])
ax.errorbar(range(int(np.ceil(u.dimensions[2] / bin_width))), np.average(tail_bin, axis=1)*10000, yerr=np.std(tail_bin, axis=1)*10000 / tail_bin.shape[1], c=sns.color_palette()[1])
ax1.errorbar(range(int(np.ceil(u.dimensions[2] / bin_width))), np.average(water_bin, axis=1)*100, yerr=np.std(water_bin, axis=1)*100 / water_bin.shape[1], c=sns.color_palette()[2])
x = np.arange(int(np.ceil(u.dimensions[2] / bin_width)))[wph != 0]
y = wph[wph!=0]
dy = wphs[wph!=0]
ax.errorbar(x, y, yerr=dy, ls='', marker='o', alpha = 0.2, c=sns.color_palette()[3])
ax.set_xlim([-20, 70])
ax.set_ylim([0, 20])
ax1.set_ylim([0, 3.4])
ax.set_xlabel(r'$z$/Å')
ax.set_ylabel(r'Number Density Lipid/$\times 10 ^{-4}$Å$^{-3}$'
              '\n'
              r'& wph')
ax1.set_ylabel(r'Number Density Water/$\times 10 ^{-2}$Å$^{-3}$')
plt.tight_layout()
plt.savefig('../reports/figures/reflectometry2/number_density.pdf')
