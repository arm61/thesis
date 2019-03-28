import MDAnalysis as mda
import numpy as np
import sys

interest = {'N': np.array([]), 'P': np.array([]),
            'C2': np.array([]), 'C21': np.array([]),
            'C31': np.array([]), 'C29': np.array([]),
            'C39': np.array([]),
            '8C21': np.array([]),
            '8C31': np.array([])}

sp = sys.argv[1]
for dsf in range(1, 11):
    u = mda.Universe('../data/reflectometry2/dspc_{}/slipids_frame{}.pdb'.format(sp, dsf))
    print(dsf, 'start')
    for k, ts in enumerate(u.trajectory):
        for i in u.atoms:
            if i.name in interest.keys():
                interest[i.name] = np.append(interest[i.name], i.position[2])

from scipy.stats.mstats import mquantiles

alpha = 0.05

for k, i in enumerate(interest.keys()):
    m =  mquantiles(interest[i], prob=[0.05, 0.5, 0.95])
    file_open = open('../output/reflectometry2/dspc_{}/slipids_position_{}_{}.txt'.format(sp, i, sp), 'w')
    file_open.write('{:.1f}'.format(m[2]-m[1]))
    file_open.close()
    file_open = open('../output/reflectometry2/dspc_{}/slipids_mean_{}_{}.txt'.format(sp, i, sp), 'w')
    file_open.write('{:.1f}'.format(m[1]))
    file_open.close()
    file_open = open('../output/reflectometry2/dspc_{}/slipids_uq_{}_{}.txt'.format(sp, i, sp), 'w')
    file_open.write('{:.1f}'.format(m[2]))
    file_open.close()
