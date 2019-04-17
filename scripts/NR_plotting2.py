from __future__ import division
import refnx
from refnx.reflect import structure, ReflectModel, SLD
from refnx.dataset import ReflectDataset
from refnx.analysis import Transform, CurveFitter, Objective, GlobalObjective, Parameter

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
mpl.rcParams["grid.linestyle"] = "--"
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

# The surface pressures to probe
sp = sys.argv[3]
cont = ['d13acmw', 'd13d2o', 'hd2o', 'd70acmw',
        'd70d2o', 'd83acmw', 'd83d2o']
apm = sys.argv[4]
neutron = 1

# A label for the output files
label = "{}_{}".format(lipid, sp)


# Relative directory locations
data_dir = "../data/reflectometry2/{}".format(label)
fig_dir = "../reports/figures/reflectometry2/"
anal_dir = "../output/reflectometry2/{}".format(label)


# For the analysis to be reproduced exactly, the same versions of `refnx`, `scipy`, and `numpy`, must be present.
# The versions used in the original version are:
#
# refnx.version.full_version == 0.1.2
# scipy.version.version == 1.1.0
# np.__version__ == 1.15.4


refnx.version.full_version, scipy.version.version, np.__version__

datasets = []
for i in range(len(cont)):
    datasets.append(
        ReflectDataset(
            "{}/{}{}.dat".format(
                data_dir, cont[i], sp
            )
        )
    )

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


d_h = 8.5
V_h = 330.0
V_t = 1100.0
min_d_t = 9


lipids = []
for i in range(len(cont)):
    lipids.append(
        mv.VolMono(
            [V_h, V_t], [b_head[i], b_tail[i]], d_h, t_length, name=label
        )
    )


air = SLD(0, "air")
structures = []
for i in range(len(cont)):
    if cont[i][-3:] == 'd2o':
        water = SLD(6.35, "d2o")
    elif cont[i][-4:] == 'acmw':
        water = SLD(0.0, "acmw")
    structures.append(air(0, 0) | lipids[i] | water(0, 3.3))


for i in range(len(cont)):
    lipids[i].vol[0].setp(
        vary=True, bounds=(V_h * 0.8, V_h * 1.2)
    )
    lipids[i].vol[1].setp(
        vary=True, bounds=(V_t * 0.8, V_t * 1.2)
    )
    lipids[i].d[0].setp(vary=True, bounds=(5, 12))
    max_d_t = 1.54 + 1.265 * t_length
    lipids[i].d[1].setp(vary=True, bounds=(min_d_t, max_d_t))
    lipids[i].vol[1].constraint = lipids[i].d[1] * float(apm)
    structures[i][-1].rough.setp(vary=True, bounds=(3.3, 6))



lipids = rh.set_constraints(
    lipids,
    structures,
    hold_tails=True,
    hold_rough=True,
    hold_phih=True,
)


models = []
t = len(cont)

for i in range(t):
    models.append(ReflectModel(structures[i]))
    models[i].scale.setp(vary=True, bounds=(0.005, 10))
    models[i].bkg.setp(datasets[i].y[-1], vary=False)

objectives = []
t = len(cont)
for i in range(t):
    objectives.append(
        Objective(models[i], datasets[i], transform=Transform("YX4"))
    )

global_objective = GlobalObjective(objectives)

chain = refnx.analysis.load_chain("{}/{}_chain.txt".format(anal_dir, label))

pchain = refnx.analysis.process_chain(global_objective, chain)


para_labels = ['{}_scale_{}_{}'.format(label, sp, cont[0]),
               '{}-V_h_{}'.format(label, sp),
               '{}-d_h_{}'.format(label, sp),
               '{}-d_t_{}'.format(label, sp),
               '{}_rough_{}'.format(label, sp),
               '{}_scale_{}_{}'.format(label, sp, cont[1]),
               '{}_scale_{}_{}'.format(label, sp, cont[2]),
               '{}_scale_{}_{}'.format(label, sp, cont[3]),
               '{}_scale_{}_{}'.format(label, sp, cont[4]),
               '{}_scale_{}_{}'.format(label, sp, cont[5]),
               '{}_scale_{}_{}'.format(label, sp, cont[6])]
units = ['', '\\angstrom3', '\\angstrom', '\\angstrom', '\\angstrom',
         '', '', '', '', '', '']

from scipy.stats.mstats import mquantiles

alpha = 0.05
for i in range(len(pchain)):
    file_open = open('{}/{}.tex'.format(anal_dir, para_labels[i]), 'w')
    stat, p = scipy.stats.shapiro(pchain[i].chain[::5000])
    if p > alpha:
        quats = mquantiles(pchain[i].chain.flatten(), prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '\pm{' + str(b) + '}$'
        file_open.write(string)
        file_open.close()
    else:
        quats = mquantiles(pchain[i].chain.flatten(), prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[2]-quats[1])
        c = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '^{+' + str(b) + '}_{-' + str(c) + '}$'
        file_open.write(string)
        file_open.close()


def get_value(file):
    f = open(file, "r")
    for line in f:
        k = line
    if "^" in k:
        l = k.split("$")[1].split("^")[0]
    else:
        l = k.split("$")[1].split("\\pm")[0]
    return float(l)

import corner
from scipy.misc import factorial
per_sp = np.zeros((pchain[0].chain.size, 6, 1))
names=['$V_t$/Å$^3$', '$V_h$/Å$^3$', '$d_t$/Å', '$d_h$/Å', r'$\phi_h/\times10^{-2}$', r'$\sigma_{t,h,s}$/Å']
abc = {'dspc_20': '(a)', 'dspc_30': '(b)', 'dspc_40': '(c)', 'dspc_50': '(d)'}
solh_store = np.zeros((1, pchain[0].chain.size))
vt_store = np.zeros((1, pchain[0].chain.size))
p_lab=['V_t', 'V_h', 'd_t', 'd_h', 'phi_h', 'sigma']
p_all = np.array([])
i=0
per_sp[:, 1, i] = list(pchain[1].chain.flatten())
per_sp[:, 2, i] = list(pchain[3].chain.flatten())
per_sp[:, 3, i] = list(pchain[2].chain.flatten())
per_sp[:, 0, i] = per_sp[:, 2, i] * float(apm)
vt_store[0, :] = list(per_sp[:, 0, i])
solh = 1 - (per_sp[:, 1, i] * per_sp[:, 2, i] / (per_sp[:, 0, i] * per_sp[:, 3, i]))
per_sp[:, 4, i] = list(solh)
solh_store[0, :] = list(solh)
per_sp[:, 5, i] = list(pchain[4].chain.flatten())
figure = corner.corner(per_sp[:, :, i],
                       max_n_ticks=3, show_titles=True,
                       color=sns.color_palette()[i], smooth1d=True)
figure.set_size_inches(4.13, 3.51)
axes = np.array(figure.axes).reshape((per_sp.shape[1],
                                      per_sp.shape[1]))
for j, n in enumerate(names):
    axes[j, j].set_title(n)
axes[0, 0].text(
    0.02, 0.75, abc[label], transform=axes[0, 0].transAxes
)
p_mag = np.array([])
for j in range(0, axes.shape[0]-1):
    for k in range(j+1, axes.shape[1]):
        pear = pearsonr(per_sp[:, j, i], per_sp[:, k, i])[0]
        file_open = open('{}/{}_p_{}_{}_sp{}.txt'.format(anal_dir, lipid, p_lab[j], p_lab[k], sp), 'w')
        file_open.write('{:.2f}'.format(pear))
        file_open.close()
        p_mag = np.append(p_mag, pear)
        p_all = np.append(p_all, pear)
        if pear < 0:
            axes[k, j].text(0.95, 0.95, '{:.2f}'.format(pear), ha='right',
                            transform=axes[k, j].transAxes, size=8,
                            va='top', zorder=10)
        else:
            axes[k, j].text(0.05, 0.95, '{:.2f}'.format(pear), ha='left',
                            transform=axes[k, j].transAxes, size=8,
                            va='top', zorder=10)
file_open = open('{}/{}_p_sum_sp{}.txt'.format(anal_dir, lipid, sp), 'w')
file_open.write('{:.2f}'.format(np.sum(np.abs(p_mag))))
file_open.close()
plt.savefig('{}/{}_pdf.pdf'.format(fig_dir, label),
            bbox_inches='tight', pad_inches=0.1)
plt.close()
file_open = open('{}/{}_p_all_sp{}.txt'.format(anal_dir, lipid, sp), 'w')
file_open.write('{:.2f}'.format(np.sum(np.abs(p_all))))
file_open.close()

para_labels = ['{}-wph_{}'.format(label, sp)]

wph = pchain[1].chain.flatten() * solh / (29.9 - 29.9 * solh)
alpha = 0.05
file_open = open('{}/{}.tex'.format(anal_dir, para_labels[i]), 'w')
stat, p = scipy.stats.shapiro(wph[::5000])
if p > alpha:
    quats = mquantiles(wph, prob=[0.025, 0.5, 0.975])
    a = '{:.2f}'.format(quats[1])
    b = '{:.2f}'.format(quats[1]-quats[0])
    string = '$' + str(a) + '\pm{' + str(b) + '}$'
    file_open.write(string)
    file_open.close()
else:
    quats = mquantiles(wph, prob=[0.025, 0.5, 0.975])
    a = '{:.2f}'.format(quats[1])
    b = '{:.2f}'.format(quats[2]-quats[1])
    c = '{:.2f}'.format(quats[1]-quats[0])
    string = '$' + str(a) + '^{+' + str(b) + '}_{-' + str(c) + '}$'
    file_open.write(string)
    file_open.close()

para_labels = ['{}-V_t_{}'.format(label, sp)]

for i in range(len(para_labels)):
    alpha = 0.05
    file_open = open('{}/{}.tex'.format(anal_dir, para_labels[i]), 'w')
    stat, p = scipy.stats.shapiro(vt_store[i][::5000])
    if p > alpha:
        quats = mquantiles(vt_store[i], prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '\pm{' + str(b) + '}$'
        file_open.write(string)
        file_open.close()
    else:
        quats = mquantiles(vt_store[i], prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[2]-quats[1])
        c = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '^{+' + str(b) + '}_{-' + str(c) + '}$'
        file_open.write(string)
        file_open.close()

para_labels = ['{}-phih_{}'.format(label, sp)]

for i in range(len(para_labels)):
    alpha = 0.05
    file_open = open('{}/{}.tex'.format(anal_dir, para_labels[i]), 'w')
    stat, p = scipy.stats.shapiro(solh_store[i][::5000])
    if p > alpha:
        quats = mquantiles(solh_store[i] * 100, prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '\pm{' + str(b) + '}$'
        file_open.write(string)
        file_open.close()
    else:
        quats = mquantiles(solh_store[i] * 100, prob=[0.025, 0.5, 0.975])
        a = '{:.2f}'.format(quats[1])
        b = '{:.2f}'.format(quats[2]-quats[1])
        c = '{:.2f}'.format(quats[1]-quats[0])
        string = '$' + str(a) + '^{+' + str(b) + '}_{-' + str(c) + '}$'
        file_open.write(string)
        file_open.close()

fig = plt.figure(figsize=(4.13, 3.51*1.3))
gs = mpl.gridspec.GridSpec(1, 3)
ax1 = plt.subplot(gs[0, 0:2])
ax2 = plt.subplot(gs[0, 2])
abc = {'dspc_20': '(a)', 'dspc_30': '(b)', 'dspc_40': '(c)', 'dspc_50': '(d)'}
chi = np.zeros((7))
for i in range(len(cont)):
    choose = global_objective.pgen(ngen=100)
    ax1.errorbar(datasets[i].x,
                 datasets[i].y*(datasets[i].x)**4 * 10**(i-1),
                 yerr=datasets[i].y_err*(
                     datasets[i].x)**4 * 10**(i-1),
                 linestyle='', marker='o',
                 color=sns.color_palette()[i])
    for pvec in choose:
        global_objective.setp(pvec)
        ax1.plot(datasets[i].x,
                 models[i](datasets[i].x,
                           x_err=datasets[i].x_err)*(
                     datasets[i].x)**4 * 10**(i-1),
                 color=sns.color_palette()[i], alpha=0.1)
        zs, sld = structures[i].sld_profile()
        ax2.plot(zs, sld + i*10, color=sns.color_palette()[i],
                 alpha=0.1)
    ax1.plot(datasets[i].x,
             models[i](datasets[i].x,
                       x_err=datasets[i].x_err)*(
                 datasets[i].x)**4 * 10**(i-1),
             color='k', zorder=10)
    chi[i] = global_objective.objectives[i].chisqr()
    file_open = open('{}/dspc_{}_{}_chi.txt'.format(anal_dir, sp, cont[i]), 'w')
    file_open.write('{:.2f}'.format(chi[i]))
    file_open.close()
file_open = open('{}/dspc_{}_all_chi.txt'.format(anal_dir, sp), 'w')
file_open.write('${:.2f}\\pm{:.2f}$'.format(np.average(chi), np.std(chi)))
file_open.close()
ax1.set_ylabel(r'$Rq^4$/Å$^{-4}$')
ax1.set_yscale('log')
ax1.set_xlabel(r'$q$/Å$^{-1}$')
ax2.set_xlabel(r'$z$/Å')
ax2.set_ylabel(r'SLD/$10^{-6}$Å$^{-2}$')
ax1.text(0.02, 0.98, '(a)', transform=ax1.transAxes, va='top', ha='left', size=8)
plt.tight_layout()
plt.savefig('{}{}_ref_sld.pdf'.format(fig_dir, label), bbox_inches='tight', pad_inches=0.1)
plt.close()
