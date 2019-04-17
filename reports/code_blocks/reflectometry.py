# Copyright 2015-2019 A. R. J. Nelson
# Australian Nuclear Science and Technology Organisation
# Licensed under the BSD 3-Clause "New" or "Revised" License

import numpy as np


def abeles(q_values, sld, d):
    R = np.zeros_like(q_values)
    kn = np.sqrt(
        q_values[:, np.newaxis] ** 2.0 / 4.0 - 4.0 * np.pi * sld
    )
    B = np.zeros((2, 2, q_values.size))
    B[0, 0, :] = 1
    B[1, 1, :] = 1
    k = kn[:, 0]
    nmax = sld.size
    for n in range(1, nmax):
        kn1 = kn[:, n]
        r = (k - kn1) / (k + kn1)
        betan = k * d[n]
        if n > 0:
            Mn = np.array(
                [
                    [np.exp(betan * 1j), r * np.exp(betan * 1j)],
                    [r * np.exp(-betan * 1j), np.exp(-betan * 1j)],
                ]
            )
        else:
            Mn = np.array([[1, r], [r, 1]])
        p0 = B[0, 0, :] * Mn[0, 0, :] + B[1, 0, :] * Mn[0, 1, :]
        p1 = B[0, 0, :] * Mn[1, 0, :] + B[1, 0, :] * Mn[1, 1, :]
        B[0, 0, :] = p0
        B[1, 0, :] = p1
        p0 = B[0, 1, :] * Mn[0, 0, :] + B[1, 1, :] * Mn[0, 1, :]
        p1 = B[0, 1, :] * Mn[1, 0, :] + B[1, 1, :] * Mn[1, 1, :]
        B[0, 1, :] = p0
        B[1, 1, :] = p1
        k = kn1
    R = (B[0, 1, :] * np.conj(B[0, 1, :])) / (
        B[0, 0, :] * np.conj(B[0, 0, :])
    )
    R[np.where(np.isnan(R))] = 1.0
    return np.real(R)
