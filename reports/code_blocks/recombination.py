import numpy as np


def recombination(p, m, kr):
    o = np.array(p)
    rand = np.random.rand(p.shape[0], p.shape[1])
    o[rand < kr] = m[rand < kr]
    return o
