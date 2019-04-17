import numpy as np


def mcmc(theta, f, a, data, iterations, nburn):
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
