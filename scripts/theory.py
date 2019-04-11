import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import matplotlib.gridspec as gridspec
import pandas as pd
import warnings

np.random.seed(1)

warnings.filterwarnings("ignore")

sns.set(palette="colorblind")
sys.path.insert(0, "../reports/code_blocks/")
import reflectometry as refl

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

x = np.arange(-10, 10, 0.01)
y = np.ones_like(x) * 2.0719e-6
for i in range(0, len(x)):
    if x[i] < 0:
        y[i] = 0

x2 = np.array(x[:-1])
y2 = np.array(x[:-1])
for i in range(0, len(x) - 1):
    y2[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])

q = np.arange(0.0005, 0.101, 0.0005)
r = np.zeros_like(q)
for i in range(0, len(q)):
    r[i] = np.sum((y2 * np.exp(-1j * x2 * q[i])) ** 2)
    r[i] *= 16 * np.pi ** 2
    r[i] /= q[i] ** 4

plt.figure(figsize=(4.13, 3.51))
gs = gridspec.GridSpec(2, 2)
ax = plt.subplot(gs[0, 0])
ax.plot(x, y * 1e6)
ax.set_xlabel(r"$z$/Å")
ax.set_ylabel(r"$\rho(z)$/$\times10^{-6}$ Å$^{-2}$")
ax.set_xlim([-10, 10])
ax.set_xticks(np.arange(-10, 20, 10))
ax.text(
    0.12,
    0.9,
    "(a)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
ax = plt.subplot(gs[0, 1])
ax.plot(x2, y2 * 1e4)
ax.set_xlabel(r"$z$/Å")
ax.set_ylabel(r"$\rho'(z)$/$\times10^{-6}$ Å$^{-3}$")
ax.set_xlim([-10, 10])
ax.set_xticks(np.arange(-10, 20, 10))
ax.text(
    0.12,
    0.9,
    "(b)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
ax = plt.subplot(gs[1, :])
ra = refl.abeles(q, np.array([0, 2.0719e-6]), np.array([10, 10]))
ax.plot(q, r * ra[-1] / r[-1], zorder=10)
ax.plot(q, np.ones_like(q), lw=1)
ax.set_xlabel(r"$q$/Å$^{-1}$")
ax.set_ylabel(r"$R(q)$")
ax.text(
    0.95,
    0.9,
    "(c)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
ax.set_yscale("log")
ax.set_xlim([0, 0.1])
plt.tight_layout()
plt.savefig("../reports/figures/theory/kine.pdf")
plt.close()


x = np.arange(-10, 10, 0.01)
y = np.ones_like(x) * 2.0719e-6
for i in range(0, len(x)):
    if x[i] < 0:
        y[i] = 0

x2 = np.array(x[:-1])
y2 = np.array(x[:-1])
for i in range(0, len(x) - 1):
    y2[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])

q = np.arange(0.0005, 0.101, 0.0005)
r = np.zeros_like(q)
for i in range(0, len(q)):
    r[i] = np.sum((y2 * np.exp(-1j * x2 * q[i])) ** 2)
    r[i] *= 16 * np.pi ** 2
    r[i] /= q[i] ** 4

plt.figure(figsize=(4.13, 1.755))
gs = gridspec.GridSpec(1, 2)
ax = plt.subplot(gs[0, :])
ra = refl.abeles(q, np.array([0, 2.0719e-6]), np.array([10, 10]))
ax.plot(q, ra, "--", zorder=10, c="#029E73")
ax.plot(q, r * ra[-1] / r[-1], zorder=9, c="#0173B2")
ax.plot(q, np.ones_like(q), c="#DE8F05", lw=1)
ax.set_xlabel(r"$q$/Å$^{-1}$")
ax.set_ylabel(r"$R(q)$")
ax.set_yscale("log")
ax.set_xlim([0, 0.1])
plt.tight_layout()
plt.savefig("../reports/figures/theory/dyna.pdf")
plt.close()


x = np.arange(-10, 10, 0.005)
beta = np.zeros_like(x)
beta[np.where((x >= -5) & (x < 5))] = 1
qx = np.arange(-1.5, 1.5, 0.001)
dsc = np.zeros_like(qx)
for i, q in enumerate(qx):
    dsc[i] = np.sum(beta * np.exp(1j * q * x)) ** 2
plt.figure(figsize=(1.77, 3.54))
gs = gridspec.GridSpec(2, 1)
ax = plt.subplot(gs[0, 0])
ax.plot(x, beta)
ax.set_yticks([0])
ax.set_xlabel(r"x/Å")
ax.set_ylabel(r"SLD/Å$^{-2}$")
ax.text(
    0.12,
    0.88,
    "(a)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
ax = plt.subplot(gs[1, 0])
ax.plot(qx, dsc)
ax.set_yticks([0])
ax.set_xticks([-1.2566, 0, 1.2566])
ax.set_xticklabels(
    [
        r"$\frac{-4\pi}{d_x}$",
        0,
        r"$\frac{4\pi}{d_x}$",
    ]
)
ax.set_xlabel(r"$q_x$/Å$^{-1}$")
ax.set_ylabel(r"$\frac{d\sigma}{d\Omega}$/Å$^{2}$")
ax.text(
    0.12,
    0.88,
    "(b)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
plt.tight_layout()
plt.savefig("../reports/figures/theory/scales.pdf")
plt.close()


def sphere(r, q):
    return np.square(
        np.divide(
            (3 * (np.sin(q * r) - q * r * np.cos(q * r))),
            np.power((q * r), 3),
        )
    )


q = np.linspace(0.001, 0.75, 100)
i = sphere(20, q)
plt.figure(figsize=(4.13, 3.51))
gs = gridspec.GridSpec(2, 1)
ax = plt.subplot(gs[0, 0])
ax.plot(q, i, "o")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel(r"$q$/Å$^{-1}$")
ax.set_ylabel(r"$I(q)$")
ax.set_xlim(0.01, 0.75)
ax.set_ylim(0.0001, 1)
ax.text(
    0.12,
    0.1,
    "(a)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax.transAxes,
    size=10,
)
ax1 = plt.subplot(gs[1, 0])
ax1.plot(q * q, np.log(i), "o")
ax1.plot(
    q[:40] * q[:40],
    -((20 * np.sqrt(3 / 5)) ** 2 / 3) * q[:40] * q[:40],
)
ax1.set_xlim(0.0, 0.25)
ax1.set_ylim(-8.5, 0)
ax1.set_xlabel(r"$q^2$/Å$^{-2}$")
ax1.set_ylabel(r"ln[$I(q)$]")
ax1.text(
    0.06,
    0.1,
    "(b)",
    horizontalalignment="center",
    verticalalignment="center",
    transform=ax1.transAxes,
    size=10,
)
plt.tight_layout()
plt.savefig("../reports/figures/theory/rg.pdf")
plt.close()


exp_file = "../data/theory/Experimental-sphere.txt"

data = pd.read_csv(exp_file, delim_whitespace=True)

plt.figure(figsize=(4.13, 1.755))
plt.errorbar(
    data["<X>"],
    data["<Y>"],
    yerr=data["<Y>"] * 0.1,
    marker="o",
    ls="",
)
plt.yscale("log")
r = 50
q = np.linspace(data["<X>"].iloc[0], data["<X>"].iloc[-1], 1000)
a = sphere(r, q)
a *= data["<Y>"][0] / a[0]
plt.plot(q, a)
plt.ylim([0.1, 10000])
plt.xlim([0, 0.5])
plt.ylabel("$I(q)$/cm$^{-1}$")
plt.xlabel("$q$/Å$^{-1}$")
plt.tight_layout()
plt.savefig("../reports/figures/theory/sphere.pdf")
plt.close()


def attractive_energy(rij, b):
    return -b / np.power(rij, 6)


def repulsive_energy(rij, a):
    return a / np.power(rij, 12)


def lj_energy(rij, a, b):
    return repulsive_energy(rij, a) + attractive_energy(rij, b)


r = np.linspace(3e-10, 6e-10, 100)
fig = plt.figure(figsize=(4.13, 2.6325))
ax = fig.add_subplot(111)
ax.plot(r * 1e10, 6.022e23 * 1e-3 * attractive_energy(r, 9.273e-78))
ax.plot(r * 1e10, 6.022e23 * 1e-3 * repulsive_energy(r, 1.363e-134))
ax.plot(
    r * 1e10, 6.022e23 * 1e-3 * lj_energy(r, 1.363e-134, 9.273e-78)
)
ax.set_xlabel("$r$/Å")
ax.set_ylabel(r"$E$/kJmol$^{-1}$")
plt.tight_layout()
plt.savefig("../reports/figures/theory/lj.pdf")
plt.close()

import grad


def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def xrosen(x, y):
    return 400 * x ** 3 + (2 - 400 * y) * x - 2


def yrosen(x, y):
    return 200 * (y - x ** 2)


def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    first = -a * np.exp(
        -b * np.sqrt(1 / 2 * np.sum(np.square(x), axis=0))
    )
    second = np.exp(1 / 2 * np.sum(np.cos(c * x), axis=0))
    return first - second + a + np.exp(1)


startx1 = np.random.uniform(-40, 40, 8)
startx2 = np.random.uniform(-40, 40, 8)

import diff_evo

route = diff_evo.differential_evolution(
    np.array([startx1, startx2]),
    ackley,
    0.5,
    0.5,
    [-40, 40],
    2.5,
    100,
)

xs = np.linspace(-40.0, 40.0, 50)
ys = np.linspace(-40.0, 40.0, 50)
es = np.zeros((xs.size, ys.size))
for i in range(xs.size):
    for j in range(ys.size):
        es[i, j] = ackley(np.array([xs[i], ys[j]]))

fig = plt.figure(figsize=(4.13, 3.304))
ax = fig.add_subplot(111)
im = ax.contourf(ys, xs, es, 100, cmap="Blues")
for i in range(route.shape[2]):
    ax.plot(
        route[:, 0, i],
        route[:, 1, i],
        marker="o",
        ms=4,
        c=sns.color_palette()[i + 1],
    )
ax.set_ylabel(r"$x_1$")
ax.set_xlabel(r"$x_2$")
plt.colorbar(im, label=r"$F(\mathbf{x})$")

plt.tight_layout()
plt.savefig("../reports/figures/theory/diff_evo.pdf")
plt.close()


startx1 = np.random.uniform(-40, 40, 8)
startx2 = np.random.uniform(-40, 40, 8)

import part_swarm

a = 40
route = 100
while np.max(np.abs(route)) > 40:
    route = part_swarm.particle_swarm(
        np.array([startx1, startx2]),
        ackley,
        0.9,
        0.05,
        0.05,
        2.5,
        100,
    )

xs = np.linspace(-a, a, 50)
ys = np.linspace(-a, a, 50)
es = np.zeros((xs.size, ys.size))
for i in range(xs.size):
    for j in range(ys.size):
        es[i, j] = ackley(np.array([xs[i], ys[j]]))

fig = plt.figure(figsize=(5, 25 / 6))
ax = fig.add_subplot(111)
im = ax.contourf(ys, xs, es, 100, cmap="Blues")
for i in range(route.shape[2]):
    ax.plot(
        route[:, 0, i],
        route[:, 1, i],
        marker="o",
        ms=4,
        c=sns.color_palette()[i + 1],
    )
ax.set_ylabel(r"$x_1$")
ax.set_xlabel(r"$x_2$")
plt.colorbar(im, label=r"$F(\mathbf{x})$")

plt.tight_layout()
plt.savefig("../reports/figures/theory/part_swarm.pdf", bbox_inches = 'tight',
    pad_inches = 0)
plt.close()


from scipy.stats import norm
from scipy.optimize import curve_fit


def gaussianfit(x, a1, a2, b1, b2):
    return a1 * norm.pdf(x - b1) + a2 * norm.pdf(x - b2)


def gaussian(x, a1):
    return a1[0] * norm.pdf(x - a1[2]) + a1[1] * norm.pdf(x - a1[3])


x = np.linspace(-5, 8, 25)
y = gaussian(x, [0.5, 1, 3, 0]) + np.random.randn(
    25
) * 0.05 * gaussian(x, [0.5, 1, 3, 0])
dy = y * 0.2

popt, pcov = curve_fit(gaussianfit, x, y, sigma=dy, p0=[0.5, 1, 3, 0])

x2 = np.linspace(-5, 8, 2500)

theta1 = np.zeros((4))
guess1 = gaussian(x, [popt[0], popt[1], popt[2], popt[3]])
plt.figure(figsize=(5, 25 / 4))
gs = gridspec.GridSpec(3, 2)

ax1 = plt.subplot(gs[2, :])
ax1.errorbar(
    x, y, marker="o", ls="", yerr=dy, c=sns.color_palette()[0]
)
import mcmc

history = mcmc.mcmc(popt, gaussian, 0.1, [x, y, dy], 600, 100)

for i in range(0, history.shape[0], 5):
    ax1.plot(
        x2,
        gaussian(
            x2,
            [
                history[i, 0],
                history[i, 1],
                history[i, 2],
                history[i, 3],
            ],
        ),
        alpha=0.05,
        c=sns.color_palette()[2],
    )

ax1.plot(x2, gaussian(x2, popt), c=sns.color_palette()[1])

ax2 = plt.subplot(gs[0, 0])
w = np.ones_like(history[:, 0]) / float(history.shape[0])
ax2.hist(history[:, 0], bins=20, weights=w, histtype="stepfilled")
ax3 = plt.subplot(gs[0, 1])
ax3.hist(history[:, 1], bins=20, weights=w, histtype="stepfilled")
ax4 = plt.subplot(gs[1, 0])
ax4.hist(history[:, 2], bins=20, weights=w, histtype="stepfilled")
ax5 = plt.subplot(gs[1, 1])
ax5.hist(history[:, 3], bins=20, weights=w, histtype="stepfilled")
ax2.set_ylabel(r"$p(\theta_1)$")
ax3.set_ylabel(r"$p(\theta_2)$")
ax4.set_ylabel(r"$p(\theta_3)$")
ax5.set_ylabel(r"$p(\theta_4)$")
ax2.set_xlabel(r"$\theta_1$")
ax3.set_xlabel(r"$\theta_2$")
ax4.set_xlabel(r"$\theta_3$")
ax5.set_xlabel(r"$\theta_4$")
ax1.set_ylabel(r"$y$")
ax1.set_xlabel(r"$x$")
ax1.set_ylim(0, 0.55)
ax2.set_ylim(0, 0.15)
ax3.set_ylim(0, 0.15)
ax4.set_ylim(0, 0.15)
ax5.set_ylim(0, 0.15)
ax2.text(
    0.95,
    0.92,
    r"$\theta_1$ = {:.2f}$\pm${:.2f}".format(
        np.average(history[:, 0]), np.std(history[:, 0])
    ),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax2.transAxes,
    color="k",
    size=8,
)
ax3.text(
    0.95,
    0.92,
    r"$\theta_2$ = {:.2f}$\pm${:.2f}".format(
        np.average(history[:, 1]), np.std(history[:, 1])
    ),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax3.transAxes,
    color="k",
    size=8,
)
ax4.text(
    0.95,
    0.92,
    r"$\theta_3$ = {:.2f}$\pm${:.2f}".format(
        np.average(history[:, 2]), np.std(history[:, 2])
    ),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax4.transAxes,
    color="k",
    size=8,
)
ax5.text(
    0.95,
    0.92,
    r"$\theta_4$ = {:.2f}$\pm${:.2f}".format(
        np.average(history[:, 3]), np.std(history[:, 3])
    ),
    horizontalalignment="right",
    verticalalignment="center",
    transform=ax5.transAxes,
    color="k",
    size=8,
)
ax2.text(
    0.05,
    0.92,
    r"(a)",
    horizontalalignment="left",
    verticalalignment="center",
    transform=ax2.transAxes,
    color="k",
    size=8,
)
ax3.text(
    0.05,
    0.92,
    r"(b)",
    horizontalalignment="left",
    verticalalignment="center",
    transform=ax3.transAxes,
    color="k",
    size=8,
)
ax4.text(
    0.05,
    0.92,
    r"(c)",
    horizontalalignment="left",
    verticalalignment="center",
    transform=ax4.transAxes,
    color="k",
    size=8,
)
ax5.text(
    0.05,
    0.92,
    r"(d)".format(np.average(history[:, 3]), np.std(history[:, 3])),
    horizontalalignment="left",
    verticalalignment="center",
    transform=ax5.transAxes,
    color="k",
    size=8,
)
ax1.text(
    0.025,
    0.92,
    r"(e)",
    horizontalalignment="left",
    verticalalignment="center",
    transform=ax1.transAxes,
    color="k",
    size=8,
)

plt.tight_layout()
plt.savefig("../reports/figures/theory/mcmc.pdf", bbox_inches = 'tight',
    pad_inches = 0)
plt.close()
