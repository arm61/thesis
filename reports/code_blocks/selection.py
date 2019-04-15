import numpy as np


def selection(p, o, f):
    new_p = np.array(p)
    for j in range(p.shape[1]):
        p_fom = f(p[:, j])
        o_fom = f(o[:, j])
        if o_fom < p_fom:
            new_p[:, j] = o[:, j]
    return new_p
