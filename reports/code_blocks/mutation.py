import numpy as np


def mutation(p, b, km):
    """
    Performs the mutation step, where the parent population vector
    is transforms to produce a mutant vector.

    Parameters
    ----------
    p: float, array_like
        The parent population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    b: float, array_like
        The best member of the parent population. An array of
        size i, where i is the number of variables.
    km: float
        The mutation constant.

    Returns
    -------
    float, array_like
        The mutant vector. An array of shape (i, j), where i is
        the number of varibles and j is the population size.
    """
    m = np.zeros_like(p)
    R = np.random.randint(p.shape[1], size=(2, p.shape[1]))
    for j in range(p.shape[1]):
        m[:, j] = b + km * (p[:, R[0, j]] - p[:, R[1, j]])
    return m
