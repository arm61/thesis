
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(palette='colorblind')


# In[ ]:


import matplotlib as mpl
# Default parameters for matplotlib plots
mpl.rcParams['xtick.labelsize'] = 8
mpl.rcParams['ytick.labelsize'] = 8
mpl.rcParams['axes.facecolor'] = 'w'
mpl.rcParams['lines.linewidth'] = 2
#mpl.rcParams['axes.grid'] = True
#mpl.rcParams['grid.color'] = (0.8, 0.8, 0.8)
mpl.rcParams['xtick.top'] = False
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.left'] = True
mpl.rcParams['grid.linestyle'] = '--'
mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['legend.facecolor'] = [1,1,1]
mpl.rcParams['legend.framealpha'] = 0.75
mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.edgecolor'] = 'k'


# In[ ]:


x = np.arange(-10, 10, 0.01)
y = np.ones_like(x) * 2.0719e-6
for i in range(0, len(x)):
    if x[i] < 0:
        y[i] = 0


# In[ ]:


x2 = np.array(x[:-1])
y2 = np.array(x[:-1])
for i in range(0, len(x)-1):
    y2[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])


# In[ ]:


q = np.arange(0.0001, 0.6001, 0.0001)
r = np.zeros_like(q)
for i in range(0, len(q)):
    r[i] = np.sum((y2 * np.exp(-1j * x2 * q[i])) ** 2)
    r[i] *= 16 * np.pi ** 2
    r[i] /= q[i] ** 4


# In[ ]:


import matplotlib.gridspec as gridspec
plt.figure(figsize=(5, 25/6))
gs = gridspec.GridSpec(2, 2)
ax = plt.subplot(gs[0, 0])
ax.plot(x, y*1e6)
ax.set_xlabel(r'$z$/Å')
ax.set_ylabel(r'$\rho(z)$/$\times10^{-6}$ Å$^{-2}$')
ax.set_xlim([-10, 10])
ax.set_xticks(np.arange(-10, 15, 5))
ax.text(0.1, 0.92, '(a)',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes, size=8)
ax = plt.subplot(gs[0, 1])
ax.plot(x2, y2*1e4)
ax.set_xlabel(r'$z$/Å')
ax.set_ylabel(r"$\rho'(z)$/$\times10^{-6}$ Å$^{-3}$")
ax.set_xlim([-10, 10])
ax.set_xticks(np.arange(-10, 15, 5))
ax.text(0.1, 0.92, '(b)',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes, size=8)
ax = plt.subplot(gs[1, :])
ax.plot(q, r)
ax.plot(q, np.ones_like(q))
ax.set_xlabel(r'$q$/Å$^{-1}$')
ax.set_ylabel(r'$R(q)$')
ax.text(0.05, 0.92, '(c)',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes, size=8)
ax.set_yscale('log')
ax.set_xlim([0, 0.6])
plt.tight_layout()
plt.savefig('reports/figures/theory/kine.pdf')
plt.close()

