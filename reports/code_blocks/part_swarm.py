import numpy as np


def particle_swarm(position, f, omega, psig, psip, stop, max_iter):
    """
    An implementaiton of a particle swarm optimisation algorithm.

    Parameters
    ----------
    position: float, array_like
        The initial position vector. An array of shape (i, j),
        where i is the number of varibles and j is the
        population size.
    f: function
        The figure of merit function to be minimised.
    omega: float
        The interia weight.
    psig: float
        The global acceleration coefficient.
    psip: float
        The personal acceleration coefficient.
    stop: float
        The value at which the optimisation should stop.
    max_iter: int
        The maximum number of iterations that should be performed
        regardless of if stop is reached.

    Returns
    -------
    float, array_like
        The history of the parameters being fit. An array of
        shape (m, n, j), where n is the number of iterations,
        m is the number of parameters, and j is the population
        size.
    """
    history = np.array([position])
    velocity = np.zeros_like(position)
    g_best = position[:, np.argmin(f(position))]
    p_best = np.array(position)
    i = 0
    while f(g_best) > stop and i < max_iter:
        for j in range(velocity.shape[1]):
            velocity[:, j] = (
                omega * velocity[:, j]
                + psig * np.random.rand() * (g_best - position[:, j])
                + psip
                * np.random.rand()
                * (p_best[:, j] - position[:, j])
            )
            position[:, j] = position[:, j] + velocity[:, j]
        history = np.append(history, position)
        history = np.reshape(
            history, (i + 2, position.shape[0], position.shape[1])
        )
        test_g_best = position[:, np.argmin(f(position))]
        if f(test_g_best) < f(g_best):
            g_best = test_g_best
        test_p_best = np.array(position)
        for j in range(position.shape[1]):
            if f(test_p_best[:, j]) < f(p_best[:, j]):
                p_best[:, j] = test_p_best[:, j]
        i += 1
    return history
