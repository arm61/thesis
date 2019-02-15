import numpy as np


def recombination(p, m, kr):
    """
    The recombination step, where the mutant and parent population
    vectors are combined.

    Parameters
    ----------
    p: float, array_like
        The parent population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    m: float, array_like
        The mutant vector. An array of shape (i, j), where i
        is the number of varibles and j is the population size.
    kr: float
        The recombination constant.

    Returns
    -------
    float, array_like
        The offspring population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    """
    o = np.array(p)
    rand = np.random.rand(p.shape[0], p.shape[1])
    o[rand < kr] = m[rand < kr]
    return o
