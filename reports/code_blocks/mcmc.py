import numpy as np


def mcmc(theta, f, a, data, iterations, nburn):
    """
    A simple implemation of the Metropolis-Hasting MCMC algorithm

    Parameters
    ----------
    theta: float, array_like
        Initial values for the variables. An array of length n,
        where n is the number of variables.
    f: function
        The function being fit to the data.
    a: float, array_like
        The step size. An array of length n, where n is the number
        of variables.
    data: float, array_like
        The data being assessed. An array of shape  (m, 3)
        containing x, y, and dy.
    iterations: int
        The number of accepted iterations to obtain.
    nburn: int
        The number of accepted iterations to ignore during the
        burn-in phase.

    Returns
    -------
    float, array_like
        The history of the parameters being fit. An array of
        shape (m, n), where n is the number of iterations,
        and m is the number of parameters.
    """
    accepted = np.array([])
    calc_y = f(data[0], theta)
    chi2 = np.sum(np.square((data[1] - calc_y) / data[2]))
    i = 0
    while i < iterations:
        new_theta = theta + a * np.random.randn(theta.size)
        new_calc_y = f(data[0], new_theta)
        new_chi2 = np.sum(np.square((data[1] - new_calc_y) / data[2]))
        prob = np.exp((-new_chi2 + chi2) / 2)
        n = np.random.rand()
        if n < prob:
            i += 1
            theta = new_theta
            chi2 = new_chi2
            if i > nburn:
                accepted = np.append(accepted, theta)
                accepted = np.reshape(
                    accepted, (i - nburn, theta.size)
                )
    return accepted
