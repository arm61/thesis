import numpy as np


def lj_energy(coordinates, cell, cut_off, A, B):
    """
    Calculates the potential energy arising from the Lennard-Jones
    potential model from a series of atomistic particles.

    Parameters
    ----------
    coordinates: float, array-like (N, 3)
        An array of the x, y, and z coordinates for each of the N
        particles in the simulation.
    cell: float, array-like
        An array of length 3 containing the simulation cell vectors.
    cut_off: float
        The potential energy cut_off value for the simulation.
    A: float
        The A parameter in the Lennard-Jones potential model.
    B: float
        The B parameter in the Lennard-Jones potential model.

    Returns
    -------
    float, array-like
        An array of length N containing the energy of each particle
        in the simulation.
    """
    energy = np.zeros((coordinates.shape[0]))
    for i in range(coordinates.shape[0] - 1):
        for j in range(i + 1, coordinates.shape[0]):
            d = coordinates[j] - coordinates[i]
            d = d % cell
            r = np.sqrt(np.sum(np.square(d)))
            if r > cut_off:
                break
            else:
                energy[i] += A / np.power(r, 12) - B / np.power(r, 6)
                energy[j] += A / np.power(r, 12) - B / np.power(r, 6)
    return energy
