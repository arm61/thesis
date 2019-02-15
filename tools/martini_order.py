import numpy as np
import os.path

import refnx, scipy

# the ReflectDataset object will contain the data
from refnx.dataset import ReflectDataset

# the reflect module contains functionality relevant to reflectometry
from refnx.reflect import ReflectModel

# the analysis module contains the curvefitting engine
from refnx.analysis import Objective, Transform, CurveFitter
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

import sys
sys.path.insert(0, '../reports/code_blocks')
import sim_lengths as sl
import md_simulation as md


forcefield = 'martini'
surface_pressure = '30'
traj_dir = '../data/reflectometry2/dspc_{}/{}'.format(surface_pressure, forcefield)
anal_dir = "../output/reflectometry2/dspc_{}/".format(surface_pressure)
print('{} {}'.format(forcefield, surface_pressure))

head = ['D', 'D']
tail = ['H', 'H']
sol = ['D', 'D']
contrasts = ['d13d2o', 'd13d2o']
lt = [1, 4]
rough = [0, 0.8]
co=30

fig = plt.figure(figsize=(5, 25/11))
gs = mpl.gridspec.GridSpec(1, 1)
ax2 = plt.subplot(gs[0, 0])
for ci, contrast in enumerate(contrasts):
    for k in range(0, len(contrasts)):
        if contrasts[k] == contrast:
            break

    models = []
    datasets = []
    structures = []

    lgts = sl.get_lgts(head[k], tail[k], sol[k], forcefield)
    l = np.array([])
    timesteps = 0
    for i in range(1, 2):
        print('frame{}'.format(i))
        try:
            del sim
        except:
            pass
        sim = md.MDSimulation(traj_dir + '_frame{}.pdb'.format(i), flip=True,
                              verbose=True, layer_thickness=lt[ci], roughness=rough[ci])

        sim.assign_scattering_lengths('neutron', atom_types=lgts[0], scattering_lengths=lgts[1])

        sim.run()
        layers_to_cut = int(co / lt[ci]) + 1
        timesteps += sim.layers.shape[0]
        l = np.append(l, sim.layers[:, :-layers_to_cut, :])

    n = l.reshape(timesteps, sim.layers.shape[1]-layers_to_cut, sim.layers.shape[2])

    data_dir = '../data/reflectometry2/dspc_{}/'.format(surface_pressure)
    dataset = ReflectDataset(os.path.join(data_dir, '{}{}.dat'.format(contrast, surface_pressure)))

    refy = np.zeros((n.shape[0], dataset.x.size))
    sldy = []
    chi = np.zeros((n.shape[0]))
    print(n.shape[0])
    for i in range(n.shape[0]):
        sim.av_layers = n[i, :, :]
        model = ReflectModel(sim)
        model.scale.setp(1, vary=True, bounds=(0.00000001, np.inf))
        model.bkg.setp(dataset.y[-1], vary=False)
        objective = Objective(model, dataset, transform=Transform('YX4'))
        fitter = CurveFitter(objective)
        res = fitter.fit()
        refy[i] = model(dataset.x, x_err=dataset.x_err)*(dataset.x)**4
        sldy.append(sim.sld_profile()[1])
        if i % 5 == 0:
            zs, sld = sim.sld_profile()
            ax2.plot(zs, sld, color=sns.color_palette()[ci],
                     alpha=0.1)
ax2.set_xlabel(r'$z$/Å')
ax2.set_ylabel(r'SLD/$10^{-6}$Å$^{-2}$')
ax2.set_xlim([-2, 70])
plt.tight_layout()
fig_dir = "../reports/figures/reflectometry2/"
plt.savefig('{}martini_order.pdf'.format(fig_dir))
