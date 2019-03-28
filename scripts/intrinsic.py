import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette="colorblind")
import matplotlib as mpl

from math import sqrt

def xydist(a, b, cell):
    dx = b[:, 0]-a[0]
    dx = dx % cell[0]
    dy = b[:, 1]-a[1]
    dy = dy % cell[1]
    dist = np.sqrt(np.square(dx) + np.square(dy))
    return dist

import sys

ff = sys.argv[1]
sp = sys.argv[2]

waters = ['OW', 'HW1', 'HW2']
heads = ['N', 'C13', 'H13A', 'H13B', 'H13C', 'C14', 'H14A', 'H14B', 'H14C',
       'C15', 'H15A', 'H15B', 'H15C', 'C12', 'H12A', 'H12B', 'C11', 'H11A',
       'H11B', 'O13', 'O14', 'O11', 'O12', 'C1', 'HA', 'HB', 'C2', 'HS',
       'O21', 'C21', 'O22', 'C3', 'HX', 'HY', 'O31', 'C31', 'O32']

def my_func():
    aks = 1
    for f in range(1, 11):
        print('frame{}'.format(f))
        u = mda.Universe('../data/reflectometry2/dspc_{}/{}_frame{}.pdb'.format(sp, ff, f))
        p_pos = np.zeros((len(u.trajectory), 100, 3))
        for k, ts in enumerate(u.trajectory):
            count = 0
            count_w = 0
            count_h = 0
            count_t = 0
            for i in u.atoms:
                if i.name in waters:
                    count_w += 1
                elif i.name in heads:
                    count_h += 1
                else:
                    if i.name != 'P':
                        count_t += 1
                if i.name == 'P':
                    p_pos[k, count, :] = i.position
                    count += 1
            print(k)

        nearest = np.zeros((count_w, len(u.trajectory)), dtype=int)
        nearest_h = np.zeros((count_h, len(u.trajectory)), dtype=int)
        nearest_t = np.zeros((count_t, len(u.trajectory)), dtype=int)
        sda = np.zeros((51, count_w))
        sdh = np.zeros((51, count_h))
        sdt = np.zeros((51, count_t))
        for k, ts in enumerate(u.trajectory):
            count = 0
            count_h = 0
            count_t = 0
            for i in u.atoms:
                if i.name in waters:
                    best = 0
                    dist = ts.dimensions[0]
                    new_d = xydist(i.position, p_pos[k], ts.dimensions)
                    best = np.argmin(new_d)
                    nearest[count, k] = best
                    count += 1
                elif i.name in heads:
                    best = 0
                    dist = ts.dimensions[0]
                    new_d = xydist(i.position, p_pos[k], ts.dimensions)
                    best = np.argmin(new_d)
                    nearest_h[count_h, k] = best
                    count_h += 1
                else:
                    if i.name != 'P':
                        best = 0
                        dist = ts.dimensions[0]
                        new_d = xydist(i.position, p_pos[k], ts.dimensions)
                        best = np.argmin(new_d)
                        nearest_t[count_t, k] = best
                        count_t += 1
            count = 0
            count_h = 0
            count_t = 0
            for i in u.atoms:
                if i.name in waters:
                    a = p_pos[k, nearest[count, k]][2] - i.position[2]
                    b = i.position[2]
                    c = p_pos[k, nearest[count, k]][2]
                    d = a - b + c
                    sda[k, count] = d
                    count += 1
                elif i.name in heads:
                    a = p_pos[k, nearest_h[count_h, k]][2] - i.position[2]
                    b = i.position[2]
                    c = p_pos[k, nearest_h[count_h, k]][2]
                    d = a - b + c
                    sdh[k, count_h] = d
                    count_h += 1
                else:
                    if i.name != 'P':
                        a = p_pos[k, nearest_t[count_t, k]][2] - i.position[2]
                        b = i.position[2]
                        c = p_pos[k, nearest_t[count_t, k]][2]
                        d = a - b + c
                        sdt[k, count_t] = d
                        count_t += 1
            aks += 1
            print(k, sda.shape, sdh.shape, sdt.shape)

    jj = len(np.arange(int(np.floor(np.min(sda))), int(np.ceil(np.max(sda))), 1))
    jj_h = len(np.arange(int(np.floor(np.min(sdh))), int(np.ceil(np.max(sdh))), 1))
    jj_t = len(np.arange(int(np.floor(np.min(sdt))), int(np.ceil(np.max(sdt))), 1))
    ks = np.zeros((sda.shape[0], jj))
    ks_h = np.zeros((sdh.shape[0], jj_h))
    ks_t = np.zeros((sdt.shape[0], jj_t))
    for dd, sd in enumerate(sda):
        z = np.arange(int(np.floor(np.min(sda))), np.ceil(np.max(sda)), 1)
        jk = int(np.ceil(np.min(sda))) / 1
        for i in sd:
            ks[dd, int(i-jk)] += 1
    for dd, sd in enumerate(sdh):
        z_h = np.arange(int(np.floor(np.min(sdh))), np.ceil(np.max(sdh)), 1)
        jk = int(np.ceil(np.min(sdh))) / 1
        for i in sd:
            ks_h[dd, int(i-jk)] += 1
    for dd, sd in enumerate(sdt):
        z_t = np.arange(int(np.floor(np.min(sdt))), np.ceil(np.max(sdt)), 1)
        jk = int(np.ceil(np.min(sdt))) / 1
        for i in sd:
            ks_t[dd, int(i-jk)] += 1
    water_out = ks / (0.5 * ts.dimensions[0] * ts.dimensions[1] * len(waters))
    heads_out = ks_h / (0.5 * ts.dimensions[0] * ts.dimensions[1] * len(heads))
    tails_out = ks_t / (0.5 * ts.dimensions[0] * ts.dimensions[1] * 104)

    outarray = np.array([z+0.5, np.average(water_out, axis=0), np.std(water_out, axis=0)])
    np.savetxt('../output/reflectometry2/dspc_{}/waters_{}_{}.txt'.format(sp, ff, sp), outarray)
    outarray = np.array([z_h+0.5, np.average(heads_out, axis=0), np.std(heads_out, axis=0)])
    np.savetxt('../output/reflectometry2/dspc_{}/heads_{}_{}.txt'.format(sp, ff, sp), outarray)
    outarray = np.array([z_t+0.5, np.average(tails_out, axis=0), np.std(tails_out, axis=0)])
    np.savetxt('../output/reflectometry2/dspc_{}/tails_{}_{}.txt'.format(sp, ff, sp), outarray)

my_func()
