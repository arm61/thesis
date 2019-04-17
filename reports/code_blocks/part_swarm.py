import numpy as np


def particle_swarm(position, f, omega, psig, psip, max_iter):
    history = np.array([position])
    velocity = np.zeros_like(position)
    g_best = position[:, np.argmin(f(position))]
    p_best = np.array(position)
    i = 0
    while i < max_iter:
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
