import numpy as np


def mutation(p, b, km):
    m = np.zeros_like(p)
    R = np.random.randint(p.shape[1], size=(2, p.shape[1]))
    for j in range(p.shape[1]):
        m[:, j] = b + km * (p[:, R[0, j]] - p[:, R[1, j]])
    return m
