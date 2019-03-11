from __future__ import division
import refnx
from refnx.reflect import structure, ReflectModel, SLD
from refnx.dataset import ReflectDataset
from refnx.analysis import (
    Transform,
    CurveFitter,
    Objective,
    GlobalObjective,
    Parameter,
)

import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

sns.set(palette="colorblind")
import corner

import sys

sys.path.insert(0, "../reports/code_blocks")
import mol_vol as mv
import ref_help as rh

import matplotlib as mpl

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


# The lipid to be investigated
lipid = sys.argv[1]
# Number of carbon atoms in tail group
t_length = int(sys.argv[2])
# The type of radiation that is used
neutron = int(sys.argv[7])

# The surface pressures to probe
if lipid == 'dspc':
    sp = sys.argv[3]
    cont = ['d13acmw', 'd13d2o', 'hd2o', 'd70acmw',
            'd70d2o', 'd83acmw', 'd83d2o']
    apm = sys.argv[4]
    neutron = 1
else:
    if neutron:
        sp = sys.argv[3]
        cont = [sys.argv[4], sys.argv[5]]
    else:
        sp = np.array(
            [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]
        )

# A label for the output files
if lipid == 'dspc':
    label = "{}_{}".format(lipid, sp)
else:
    if neutron:
        radiation = "neutron"
        label = "{}_{}_{}".format(lipid, radiation, sp)

    else:
        radiation = "xray"
        label = "{}_{}".format(lipid, radiation)


# Relative directory locations
if lipid == 'dspc':
    data_dir = "../data/reflectometry2/{}".format(label)
    fig_dir = "../reports/figures/reflectometry2/{}".format(label)
    anal_dir = "../output/reflectometry2/{}".format(label)
else:
    if neutron:
        data_dir = "../data/reflectometry1/{}".format(label[:-3])
        fig_dir = "../reports/figures/reflectometry1/{}".format(
            label[:-3]
        )
        anal_dir = "../output/reflectometry1/{}".format(label[:-3])
        xanal_dir = "../output/reflectometry1/{}_xray".format(lipid)
    else:
        data_dir = "../data/reflectometry1/{}".format(label)
        fig_dir = "../reports/figures/reflectometry1/{}".format(label)
        anal_dir = "../output/reflectometry1/{}".format(label)


# For the analysis to be reproduced exactly, the same versions of `refnx`, `scipy`, and `numpy`, must be present.
# The versions used in the original version are:
#
# refnx.version.full_version == 0.1.2
# scipy.version.version == 1.1.0
# np.__version__ == 1.15.4


refnx.version.full_version, scipy.version.version, np.__version__

datasets = []
if lipid == 'dspc':
    for i in range(len(cont)):
        datasets.append(
            ReflectDataset(
                "{}/{}{}.dat".format(
                    data_dir, cont[i], sp
                )
            )
        )
else:
    if neutron:
        for i in range(len(cont)):
            datasets.append(
                ReflectDataset(
                    "{}/{}_{}_sp_{}.dat".format(
                        data_dir, label[:-3], cont[i], sp
                    )
                )
            )
            datasets[i].mask = datasets[i].x <= 0.6
    else:
        for i in range(sp.size):
            datasets.append(
                ReflectDataset(
                    "{}/{}_sp_{}.dat".format(data_dir, label, sp[i])
                )
            )
            datasets[i].mask = datasets[i].x <= 0.6

if lipid == 'dspc':
    b_head = []
    b_tail = []
    for i in range(len(cont)):
        if cont[i][:3] == 'd13':
            head = {"C": 10, "D": 13, "H": 5, "O": 8, "N": 1, "P": 1}
            tail = {"C": t_length * 2, "H": t_length * 4 + 2}
        elif cont[i][:3] == 'd70':
            head = {"C": 10, "D": 5, "H": 13, "O": 8, "N": 1, "P": 1}
            tail = {"C": t_length * 2, "D": t_length * 4 + 2}
        elif cont[i][:3] == 'd83':
            head = {"C": 10, "D": 18, "O": 8, "N": 1, "P": 1}
            tail = {"C": t_length * 2, "D": t_length * 4 + 2}
        elif cont[i][:1] == 'h':
            head = {"C": 10, "H": 18, "O": 8, "N": 1, "P": 1}
            tail = {"C": t_length * 2, "H": t_length * 4 + 2}
        b_head.append(rh.get_scattering_length(head, 1))
        b_tail.append(rh.get_scattering_length(tail, 1))
else:
    if lipid == "dmpg":
        head = {"C": 8, "H": 12, "O": 10, "Na": 1, "P": 1}
    else:
        head = {"C": 10, "H": 18, "O": 8, "N": 1, "P": 1}
    if neutron:
        tail = {"C": t_length * 2, "D": t_length * 4 + 2}
    else:
        tail = {"C": t_length * 2, "H": t_length * 4 + 2}
    b_head = rh.get_scattering_length(head, neutron)
    b_tail = rh.get_scattering_length(tail, neutron)


def get_value(file):
    f = open(file, "r")
    for line in f:
        k = line
    if "^" in k:
        l = k.split("$")[1].split("^")[0]
    else:
        l = k.split("$")[1].split("\\pm")[0]
    return float(l)

if lipid == 'dspc':
    d_h = 8.5
    V_h = 330.0
    V_t = 1100.0
    min_d_t = 9
else:
    if neutron:
        d_h = get_value(
            "{}/{}.tex".format(xanal_dir, "{}_xray-d_h".format(lipid))
        )
        V_h = get_value(
            "{}/{}.tex".format(xanal_dir, "{}_xray-V_h".format(lipid))
        )
        if lipid[:2] == "dl":
            V_t = get_value(
                "{}/{}.tex".format(xanal_dir, "{}_xray-V_t".format(lipid))
            )
            min_d_t = 5
        elif lipid[:2] == "dm":
            V_t = get_value(
                "{}/{}.tex".format(xanal_dir, "{}_xray-V_t".format(lipid))
            )
            min_d_t = 7
        elif lipid[:2] == "dp":
            V_t = get_value(
                "{}/{}.tex".format(xanal_dir, "{}_xray-V_t".format(lipid))
            )
            min_d_t = 9
    else:
        d_h = 12.0
        V_h = 330.0
        if lipid[:2] == "dl":
            V_t = 667.0
            min_d_t = 5
        elif lipid[:2] == "dm":
            V_t = 779.0
            if lipid[2:] == "pg":
                min_d_t = 5
            else:
                min_d_t = 7
        elif lipid[:2] == "dp":
            V_t = 891.0
            min_d_t = 9

if lipid == 'dspc':
    lipids = []
    for i in range(len(cont)):
        lipids.append(
            mv.VolMono(
                [V_h, V_t], [b_head[i], b_tail[i]], d_h, t_length, name=label
            )
        )
else:
    if neutron:
        t = len(cont)
    else:
        t = sp.size
    lipids = []
    for i in range(t):
        lipids.append(
            mv.VolMono(
                [V_h, V_t], [b_head, b_tail], d_h, t_length, name=label
            )
        )


air = SLD(0, "air")
if lipid == 'dspc':
    structures = []
    for i in range(len(cont)):
        if cont[i][-3:] == 'd2o':
            water = SLD(6.35, "d2o")
        elif cont[i][-4:] == 'acmw':
            water = SLD(0.0, "acmw")
        structures.append(air(0, 0) | lipids[i] | water(0, 3.3))
else:
    if neutron:
        des_1 = SLD(0.43, "hdes")
        des_2 = SLD(3.15, "hddes")

        structures = []
        structure_lipid_1 = air(0, 0) | lipids[0] | des_1(0, 0)
        structure_lipid_2 = air(0, 0) | lipids[1] | des_2(0, 0)
        structures.append(structure_lipid_1)
        structures.append(structure_lipid_2)

    else:
        des = SLD(10.8, "des")

        structures = []
        for i in range(sp.size):
            structures.append(air(0, 0) | lipids[i] | des(0, 3.3))

if lipid == 'dspc':
    for i in range(len(cont)):
        lipids[i].vol[0].setp(
            vary=True, bounds=(V_h * 0.8, V_h * 1.2)
        )
        lipids[i].vol[1].setp(
            vary=True, bounds=(V_t * 0.8, V_t * 1.2)
        )
        lipids[i].d[0].setp(vary=True, bounds=(5, 15))
        max_d_t = 1.54 + 1.265 * t_length
        lipids[i].d[1].setp(vary=True, bounds=(min_d_t, max_d_t))
        lipids[i].vol[1].constraint = lipids[i].d[1] * float(apm)
        structures[i][-1].rough.setp(vary=True, bounds=(3.3, 6))
else:
    if neutron:
        t = len(cont)
        for i in range(t):
            lipids[i].vol[0].setp(vary=False)
            lipids[i].vol[1].setp(vary=False)
            lipids[i].d[0].setp(vary=False)
            max_d_t = 1.54 + 1.265 * t_length
            lipids[i].d[1].setp(vary=True, bounds=(min_d_t, max_d_t))
            structures[i][-1].rough.setp(vary=True, bounds=(3.3, 6))
    else:
        t = sp.size
        for i in range(t):
            lipids[i].vol[0].setp(
                vary=True, bounds=(V_h * 0.8, V_h * 1.2)
            )
            lipids[i].vol[1].setp(
                vary=True, bounds=(V_t * 0.8, V_t * 1.2)
            )
            lipids[i].d[0].setp(vary=True, bounds=(10, 17))
            max_d_t = 1.54 + 1.265 * t_length
            lipids[i].d[1].setp(vary=True, bounds=(min_d_t, max_d_t))
            structures[i][-1].rough.setp(vary=True, bounds=(3.3, 6))


if neutron:
    lipids = rh.set_constraints(
        lipids,
        structures,
        hold_tails=True,
        hold_rough=True,
        hold_phih=True,
    )
else:
    lipids = rh.set_constraints(lipids, structures, hold_rough=False)

models = []
if neutron:
    t = len(cont)
else:
    t = sp.size

for i in range(t):
    models.append(ReflectModel(structures[i]))
    models[i].scale.setp(vary=True, bounds=(0.005, 10))
    models[i].bkg.setp(datasets[i].y[-1], vary=False)

objectives = []
if neutron:
    t = len(cont)
else:
    t = sp.size
for i in range(t):
    objectives.append(
        Objective(models[i], datasets[i], transform=Transform("YX4"))
    )

global_objective = GlobalObjective(objectives)

fitter = CurveFitter(global_objective)
np.random.seed(1)
res = fitter.fit("differential_evolution")

print(global_objective)


fitter.sample(200, random_state=1)
fitter.sampler.reset()
res = fitter.sample(
    1000,
    nthin=1,
    random_state=1,
    f="{}/{}_chain.txt".format(anal_dir, label),
)
