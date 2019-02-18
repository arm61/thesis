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
mpl.rcParams["grid.linestyle"] = "--"
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
    chain1 = ['C15', 'C33']
    chain2 = ['C36', 'C54']
elif ff == 'martini':
    chain1 = ['GL1', 'C4A']
    chain2 = ['GL2', 'C4B']
elif ff == 'slipids':
    chain1 = ['C21', '8C21']
    chain2 = ['C31', '8C31']
if ff == 'berger':
    heads = ['C1', 'C2', 'C3', 'N4', 'C5', 'C6', 'O7', 'P8', 'O9', 'O10', 'O11',
             'C12', 'C13', 'O14', 'C15', 'O16', 'C34', 'O35', 'C36', 'O37']
    waters = ['OW', 'HW1', 'HW2']
if ff == 'martini':
    heads = ['NC3', 'PO4', 'GL1', 'GL2']
    waters = ['W', 'WP', 'WM']
if ff == 'slipids':
    waters = ['OW', 'HW1', 'HW2']
    heads = ['N', 'C13', 'H13A', 'H13B', 'H13C', 'C14', 'H14A', 'H14B', 'H14C',
           'C15', 'H15A', 'H15B', 'H15C', 'C12', 'H12A', 'H12B', 'C11', 'H11A',
           'H11B', 'P', 'O13', 'O14', 'O11', 'O12', 'C1', 'HA', 'HB', 'C2', 'HS',
           'O21', 'C21', 'O22', 'C3', 'HX', 'HY', 'O31', 'C31', 'O32']

tail = np.array([])
for i in range(1, 11):
    print(ff, sp, i)
    pdbfile = '../data/reflectometry2/dspc_{}/{}_frame{}.pdb'.format(sp, ff, i)
    u = mda.Universe(pdbfile)
    for ts in u.trajectory:
        tail_pos1 = np.zeros((100, 2, 3))
        tail_pos2 = np.zeros((100, 2, 3))
        k00 = 0
        k01 = 0
        k10 = 0
        k11 = 0
        for atom in range(len(u.atoms)):
            if u.atoms[atom].name not in waters:
                if u.atoms[atom].name == chain1[0]:
                    tail_pos1[k00, 0, :] = u.atoms[atom].position
                    k00 += 1
                if u.atoms[atom].name == chain1[1]:
                    tail_pos1[k01, 1, :] = u.atoms[atom].position
                    k01 += 1
                if u.atoms[atom].name == chain2[0]:
                    tail_pos1[k10, 0, :] = u.atoms[atom].position
                    k10 += 1
                if u.atoms[atom].name == chain2[1]:
                    tail_pos1[k11, 1, :] = u.atoms[atom].position
                    k11 += 1
        d1 = np.abs(tail_pos1[:, 0, :] - tail_pos1[:, 1, :])
        d2 = np.abs(tail_pos2[:, 0, :] - tail_pos2[:, 1, :])
        for j in range(0, 2):
            d1[d1[:, j] > u.dimensions[j] / 2., j] = np.abs(d1[d1[:, j] > u.dimensions[j] / 2., j] - u.dimensions[j])
            d2[d2[:, j] > u.dimensions[j] / 2., j] = np.abs(d2[d2[:, j] > u.dimensions[j] / 2., j] - u.dimensions[j])
        dist = np.sqrt(np.square(d1[:, 0]) + np.square(d1[:, 1]) + np.square(d1[:, 2]))
        tail = np.append(tail, dist)

file_open = open('../output/reflectometry2/dspc_{}/dspc_{}_{}_dt.txt'.format(sp, ff, sp), 'w')

alpha = 0.05
stat, p = scipy.stats.shapiro(tail[::10])
if p > alpha:
    quats = scipy.stats.mstats.mquantiles(
        tail, prob=[0.025, 0.5, 0.975]
    )
    a = "{:.2f}".format(quats[1])
    b = "{:.2f}".format(quats[1] - quats[0])
    string = "$" + str(a) + "\pm{" + str(b) + "}$"
    file_open.write(string)
    file_open.close()
else:
    quats = scipy.stats.mstats.mquantiles(
        tail, prob=[0.025, 0.5, 0.975]
    )
    a = "{:.2f}".format(quats[1])
    b = "{:.2f}".format(quats[2] - quats[1])
    c = "{:.2f}".format(quats[1] - quats[0])
    string = (
        "$" + str(a) + "^{+" + str(b) + "}_{-" + str(c) + "}$"
    )
    file_open.write(string)
    file_open.close()
