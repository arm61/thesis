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
from scipy.stats import pearsonr

sns.set(palette="colorblind")
import corner

import sys

sys.path.insert(0, "../reports/code_blocks")
import mol_vol as mv
import ref_help as rh

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

# The lipid to be investigated
lipid = sys.argv[1]
# Number of carbon atoms in tail group
t_length = int(sys.argv[2])
# The type of radiation that is used
neutron = int(sys.argv[7])
# The surface pressures to probe
sp = np.array([sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]])
# A label for the output files
radiation = "xray"
label = "{}_{}".format(lipid, radiation)

# Relative directory locations
data_dir = "../data/reflectometry1/{}".format(label)
fig_dir = "../reports/figures/reflectometry1/"
anal_dir = "../output/reflectometry1/{}".format(label)

datasets = []
for i in range(sp.size):
    datasets.append(
        ReflectDataset(
            "{}/{}_sp_{}.dat".format(data_dir, label, sp[i])
        )
    )
    datasets[i].mask = datasets[i].x <= 0.6

if lipid == "dmpg":
    head = {"C": 8, "H": 12, "O": 10, "Na": 1, "P": 1}
else:
    head = {"C": 10, "H": 18, "O": 8, "N": 1, "P": 1}
tail = {"C": t_length * 2, "H": t_length * 4 + 2}
b_head = rh.get_scattering_length(head, neutron)
b_tail = rh.get_scattering_length(tail, neutron)

d_h = 12.0
V_h = 330.0
if lipid[:2] == "dl":
    V_t = 667.0
    min_d_t = 5
elif lipid[:2] == "dm":
    V_t = 779.0
    min_d_t = 7
elif lipid[:2] == "dp":
    V_t = 891.0
    min_d_t = 9

t = sp.size
lipids = []
for i in range(t):
    lipids.append(
        mv.VolMono(
            [V_h, V_t], [b_head, b_tail], d_h, t_length, name=label
        )
    )


air = SLD(0, "air")
des = SLD(10.8, "des")

structures = []
for i in range(sp.size):
    structures.append(air(0, 0) | lipids[i] | des(0, 3.3))

t = sp.size
for i in range(t):
    lipids[i].vol[0].setp(vary=True, bounds=(V_h * 0.8, V_h * 1.2))
    lipids[i].vol[1].setp(vary=True, bounds=(V_t * 0.8, V_t * 1.2))
    lipids[i].d[0].setp(vary=True, bounds=(7, 20))
    max_d_t = 1.54 + 1.265 * t_length
    lipids[i].d[1].setp(vary=True, bounds=(min_d_t, max_d_t))
    structures[i][-1].rough.setp(vary=True, bounds=(2.5, 6))


lipids = rh.set_constraints(
    lipids, structures, hold_tails=False, hold_rough=False
)

models = []
t = sp.size

for i in range(t):
    models.append(ReflectModel(structures[i]))
    models[i].scale.setp(vary=True, bounds=(0.005, 10))
    models[i].bkg.setp(datasets[i].y[-1], vary=False)

objectives = []
t = sp.size
for i in range(t):
    objectives.append(
        Objective(models[i], datasets[i], transform=Transform("YX4"))
    )

global_objective = GlobalObjective(objectives)

chain = refnx.analysis.load_chain(
    "{}/{}_chain.txt".format(anal_dir, label)
)

pchain = refnx.analysis.process_chain(global_objective, chain)

para_labels = [
    "{}_scale_{}".format(lipid, sp[0]),
    "{}-V_h".format(label),
    "{}-V_t".format(label),
    "{}-d_h".format(label),
    "{}-d_t_{}".format(label, sp[0]),
    "{}_rough_{}".format(label, sp[0]),
    "{}_scale_{}".format(lipid, sp[1]),
    "{}-d_t_{}".format(label, sp[1]),
    "{}_rough_{}".format(label, sp[1]),
    "{}_scale_{}".format(lipid, sp[2]),
    "{}-d_t_{}".format(label, sp[2]),
    "{}_rough_{}".format(label, sp[2]),
    "{}_scale_{}".format(lipid, sp[3]),
    "{}-d_t_{}".format(label, sp[3]),
    "{}_rough_{}".format(label, sp[3]),
]
units = [
    "",
    "\\angstrom\\cubed",
    "\\angstrom\\cubed",
    "\\angstrom",
    "\\angstrom",
    "\\angstrom",
    "",
    "\\angstrom",
    "\\angstrom",
    "",
    "\\angstrom",
    "\\angstrom",
    "",
    "\\angstrom",
    "\\angstrom",
]

from scipy.stats.mstats import mquantiles

alpha = 0.05
for i in range(len(pchain)):
    file_open = open(
        "{}/{}.tex".format(anal_dir, para_labels[i]), "w"
    )
    stat, p = scipy.stats.shapiro(pchain[i].chain[::5000])
    if p > alpha:
        quats = mquantiles(
            pchain[i].chain.flatten(), prob=[0.025, 0.5, 0.975]
        )
        a = "{:.2f}".format(quats[1])
        b = "{:.2f}".format(quats[1] - quats[0])
        string = "$" + str(a) + "\pm{" + str(b) + "}$"
        file_open.write(string)
        file_open.close()
    else:
        quats = mquantiles(
            pchain[i].chain.flatten(), prob=[0.025, 0.5, 0.975]
        )
        a = "{:.2f}".format(quats[1])
        b = "{:.2f}".format(quats[2] - quats[1])
        c = "{:.2f}".format(quats[1] - quats[0])
        string = (
            "$" + str(a) + "^{+" + str(b) + "}_{-" + str(c) + "}$"
        )
        file_open.write(string)
        file_open.close()

import corner
from scipy.misc import factorial

per_sp = np.zeros((pchain[0].chain.size, 6, 4))
names = [
    "$V_t$/Å$^3$",
    "$V_h$/Å$^3$",
    "$d_t$/Å",
    "$d_h$/Å",
    r"$\phi_h/\times10^{-2}$",
    r"$\sigma_{t,h,s}$/Å",
]
fig_lab = {"dppc":"(a)", "dmpc":"(b)", "dlpc":"(c)", "dmpg":"(d)"}
solh_store = np.zeros((4, pchain[0].chain.size))
p_lab = ["V_t", "V_h", "d_t", "d_h", "  phi_h", "sigma"]
p_all = np.array([])
for i in range(sp.size):
    per_sp[:, 0, i] = list(pchain[2].chain.flatten())
    per_sp[:, 1, i] = list(pchain[1].chain.flatten())
    per_sp[:, 2, i] = list(pchain[(i + 1) * 4 - i].chain.flatten())
    per_sp[:, 3, i] = list(pchain[3].chain.flatten())
    solh = 1 - (
        per_sp[:, 2, i]
        * per_sp[:, 1, i]
        / (per_sp[:, 3, i] * per_sp[:, 0, i])
    )
    solh_store[i, :] = np.array(solh)
    per_sp[:, 4, i] = list(solh)
    per_sp[:, 5, i] = list(
        pchain[(i + 1) * 4 - i + 1].chain.flatten()
    )
    figure = corner.corner(
        per_sp[:, :, i],
        max_n_ticks=3,
        show_titles=True,
        color=sns.color_palette()[i],
        smooth1d=True,
    )
    figure.set_size_inches(4.13, 3.51)
    axes = np.array(figure.axes).reshape(
        (per_sp.shape[1], per_sp.shape[1])
    )
    for j, n in enumerate(names):
        axes[j, j].set_title(n)
    axes[0, 0].text(
        0.04, 0.73, fig_lab[lipid], transform=axes[0, 0].transAxes, size=12
    )
    p_mag = np.array([])
    for j in range(0, axes.shape[0] - 1):
        for k in range(j + 1, axes.shape[1]):
            pear = pearsonr(per_sp[:, j, i], per_sp[:, k, i])[0]
            file_open = open(
                "{}/{}_p_{}_{}_sp{}.txt".format(
                    anal_dir, lipid, p_lab[j], p_lab[k], sp[i]
                ),
                "w",
            )
            file_open.write("{:.2f}".format(pear))
            file_open.close()
            p_mag = np.append(p_mag, pear)
            p_all = np.append(p_all, pear)
            if pear < 0:
                axes[k, j].text(
                    0.95,
                    0.95,
                    "{:.2f}".format(pear),
                    ha="right",
                    transform=axes[k, j].transAxes,
                    size=8,
                    va="top",
                    zorder=10,
                )
            else:
                axes[k, j].text(
                    0.05,
                    0.95,
                    "{:.2f}".format(pear),
                    ha="left",
                    transform=axes[k, j].transAxes,
                    size=8,
                    va="top",
                    zorder=10,
                )
    file_open = open(
        "{}/{}_p_sum_sp{}.txt".format(anal_dir, lipid, sp[i]), "w"
    )
    file_open.write("{:.2f}".format(np.sum(np.abs(p_mag))))
    file_open.close()
    plt.savefig(
        "{}/{}_sp_{}_pdf.pdf".format(fig_dir, label, sp[i]),
        bbox_inches="tight",
        pad_inches=0.1,
    )
    plt.close()
file_open = open(
    "{}/{}_p_all_sp{}.txt".format(anal_dir, lipid, sp[i]), "w"
)
file_open.write("{:.2f}".format(np.sum(np.abs(p_all))))
file_open.close()

para_labels = [
    "{}-phih_{}".format(label, sp[0]),
    "{}-phih_{}".format(label, sp[1]),
    "{}-phih_{}".format(label, sp[2]),
    "{}-phih_{}".format(label, sp[3]),
]

for i in range(len(para_labels)):
    alpha = 0.05
    file_open = open(
        "{}/{}.tex".format(anal_dir, para_labels[i]), "w"
    )
    stat, p = scipy.stats.shapiro(solh_store[i][::5000])
    if p > alpha:
        quats = mquantiles(
            solh_store[i] * 100, prob=[0.025, 0.5, 0.975]
        )
        a = "{:.2f}".format(quats[1])
        b = "{:.2f}".format(quats[1] - quats[0])
        string = "$" + str(a) + "\pm{" + str(b) + "}$"
        file_open.write(string)
        file_open.close()
    else:
        quats = mquantiles(
            solh_store[i] * 100, prob=[0.025, 0.5, 0.975]
        )
        a = "{:.2f}".format(quats[1])
        b = "{:.2f}".format(quats[2] - quats[1])
        c = "{:.2f}".format(quats[1] - quats[0])
        string = (
            "$" + str(a) + "^{+" + str(b) + "}_{-" + str(c) + "}$"
        )
        file_open.write(string)
        file_open.close()

fig = plt.figure(figsize=(4.13, 3.51*0.5))
gs = mpl.gridspec.GridSpec(1, 3)
ax1 = plt.subplot(gs[0, 0:2])
ax2 = plt.subplot(gs[0, 2])
abc = {"dppc": "(a)", "dmpc": "(b)", "dlpc": "(c)", "dmpg": "(d)"}
for i in range(sp.size):
    choose = global_objective.pgen(ngen=100)
    ax1.errorbar(
        datasets[i].x,
        datasets[i].y * (datasets[i].x) ** 4 * 100 ** (i - 1),
        yerr=datasets[i].y_err
        * (datasets[i].x) ** 4
        * 100 ** (i - 1),
        linestyle="",
        marker="o",
        color=sns.color_palette()[i],
    )
    for pvec in choose:
        global_objective.setp(pvec)
        ax1.plot(
            datasets[i].x,
            models[i](datasets[i].x, x_err=datasets[i].x_err)
            * (datasets[i].x) ** 4
            * 100 ** (i - 1),
            color=sns.color_palette()[i],
            alpha=0.1,
        )
        zs, sld = structures[i].sld_profile()
        ax2.plot(
            zs, sld + i * 5, color=sns.color_palette()[i], alpha=0.1
        )
    ax1.plot(
        datasets[i].x,
        models[i](datasets[i].x, x_err=datasets[i].x_err)
        * (datasets[i].x) ** 4
        * 100 ** (i - 1),
        color="k",
        zorder=10,
    )
    ax1.set_ylabel(r"$Rq^4$/Å$^{-4}$")
    ax1.set_yscale("log")
    ax1.set_xlabel(r"$q$/Å$^{-1}$")
    ax2.set_xlabel(r"$z$/Å")
    ax2.set_ylabel(r"SLD/$10^{-6}$Å$^{-2}$")
ax2.text(0.63, 0.05, abc[lipid], transform=ax2.transAxes, size=8)
plt.tight_layout()
plt.savefig("{}{}_ref_sld.pdf".format(fig_dir, label), bbox_inches='tight', pad_inches=0.1)
plt.close()

xax = {
    "dppc": np.arange(int(sp[0]), int(sp[-1]) + 5, 5),
    "dmpc": np.arange(int(sp[0]), int(sp[-1]) + 5, 5),
    "dlpc": np.arange(int(sp[0]), int(sp[-1]) + 5, 5),
    "dmpg": np.arange(int(sp[0]), int(sp[-1]) + 5, 5),
}

fig = plt.figure(figsize=(4.13, 3.51*0.5))
gs = mpl.gridspec.GridSpec(1, 1)
ax2 = plt.subplot(gs[0, 0])
ax3 = ax2.twinx()
tails = np.array(
    [
        pchain[4].chain.flatten(),
        pchain[7].chain.flatten(),
        pchain[10].chain.flatten(),
        pchain[13].chain.flatten(),
    ]
)
ax2.plot(
    sp.astype(np.int),
    np.average(tails, axis=1),
    c=sns.color_palette()[0],
    marker="o",
    ls="",
)
ax3.plot(
    sp.astype(np.int),
    np.average(solh_store, axis=1),
    c=sns.color_palette()[1],
    marker="s",
    ls="",
)
ax2.set_xlabel(r"Surface Pressure/mNm$^{-1}$")
ax2.set_ylabel(r"$d_t$/Å")
ax3.set_ylabel(r"$\phi_h$/$\times 10^{-2}$")

ax2.yaxis.label.set_color(sns.color_palette()[0])
ax3.yaxis.label.set_color(sns.color_palette()[1])
ax2.text(0.88, 0.07, abc[lipid], transform=ax2.transAxes, size=8)
ax2.tick_params(axis="y", colors=sns.color_palette()[0])
ax3.tick_params(axis="y", colors=sns.color_palette()[1])
ax2.set_xticks(xax[lipid])
plt.tight_layout()
plt.savefig("{}{}_dt_phi.pdf".format(fig_dir, label), bbox_inches='tight', pad_inches=0.1)
plt.close()
