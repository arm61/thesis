import numpy as np


def selection(p, o, f):
    """
    The selection function, where the population member that
    return the minimum value for the figure of merit is brought
    forward to the next generation.

    Parameters
    ----------
    p: float, array_like
        The parent population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    o: float, array_like
        The offspring population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    f: function
        The figure of merit function to be minimised.

    Returns
    -------
    float, array_like
        The new parent population vector. An array of shape (i, j),
        where i is the number of varibles and j is the population
        size.
    """
    new_p = np.array(p)
    for j in range(p.shape[1]):
        p_fom = f(p[:, j])
        o_fom = f(o[:, j])
        if o_fom < p_fom:
            new_p[:, j] = o[:, j]
    return new_p
