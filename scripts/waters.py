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

bin_width = 0.001
wph = np.array([])
for i in range(1, 11):
    print(ff, sp, i)
    pdbfile = '../data/reflectometry2/dspc_{}/{}_frame{}.pdb'.format(sp, ff, i)
    u = mda.Universe(pdbfile)
    for ts in u.trajectory:
        hb = np.zeros((int(np.ceil(u.dimensions[2] / bin_width))))
        wb = np.zeros((int(np.ceil(u.dimensions[2] / bin_width))))
        for atom in range(len(u.atoms)):
            if u.atoms[atom].name in heads:
                hb[int(u.atoms[atom].position[2] / bin_width)] += 1
            if u.atoms[atom].name in waters:
                wb[int(u.atoms[atom].position[2] / bin_width)] += 1

        wb = wb[::-1]
        if ff == 'martini':
            wb = wb * 4
        hb = hb[::-1]

        wab = wb / (float(len(waters)))
        hab = hb / (float(len(heads)))
        water_bin = wb / (float(len(waters)) * u.dimensions[0] * u.dimensions[1] * bin_width)
        head_bin = hb / (float(len(heads)) * u.dimensions[0] * u.dimensions[1] * bin_width)
        total_head = np.sum(head_bin)

        start = 0
        end = 0
        summing = 0
        for i in range(0, len(water_bin)):
            if summing > total_head * 0.2:
                start = i * bin_width
                break
            else:
                summing += head_bin[i]
        summing = 0
        for i in range(0, len(water_bin)):
            if summing > total_head * 0.8:
                end = i * bin_width
                break
            else:
                summing += head_bin[i]

        w = 0
        h = 0
        for i in np.arange(0, int(np.ceil(u.dimensions[2] / bin_width))):
            if i * bin_width > start and i * bin_width <= end + bin_width:
                w += wab[i]
                h += hab[i]
        wph = np.append(wph, w/h)

file_open = open('../output/reflectometry2/dspc_{}/dspc_{}_{}_wph.txt'.format(sp, ff, sp), 'w')

alpha = 0.05
stat, p = scipy.stats.shapiro(wph)
if p > alpha:
    quats = scipy.stats.mstats.mquantiles(
        wph, prob=[0.025, 0.5, 0.975]
    )
    a = "{:.2f}".format(quats[1])
    b = "{:.2f}".format(quats[1] - quats[0])
    string = "$" + str(a) + "\pm{" + str(b) + "}$"
    file_open.write(string)
    file_open.close()
else:
    quats = scipy.stats.mstats.mquantiles(
        wph, prob=[0.025, 0.5, 0.975]
    )
    a = "{:.2f}".format(quats[1])
    b = "{:.2f}".format(quats[2] - quats[1])
    c = "{:.2f}".format(quats[1] - quats[0])
    string = (
        "$" + str(a) + "^{+" + str(b) + "}_{-" + str(c) + "}$"
    )
    file_open.write(string)
    file_open.close()
