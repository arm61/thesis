import numpy as np


def lj_energy(coordinates, cell, cut_off, A, B):
    energy = np.zeros((coordinates.shape[0]))
    for i in range(coordinates.shape[0] - 1):
        for j in range(i + 1, coordinates.shape[0]):
            d = coordinates[j] - coordinates[i]
            d = d % cell
            r = np.sqrt(np.sum(np.square(d)))
            if r > cut_off:
                continue
            else:
                energy[i] += A / np.power(r, 12) - B / np.power(r, 6)
                energy[j] += A / np.power(r, 12) - B / np.power(r, 6)
    return energy
