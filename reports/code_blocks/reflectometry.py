import numpy as np

def abeles(q_values, sld, d)
    R = np.zeros_like(q_values)
    for i, q in enumerate(q_values):
        k0 = q / 2.
        kn = k0
        Bn = np.array([[1, 0],
                       [0, 1]])
        for n in range(0, nmax-1):
            kn1 = np.sqrt(k0 ** 2. - 4 * pi *
                          (sld[i + 1] - sld[0]))
            r = (kn - kn1) / (kn + kn1)
            betan = kn * d[n]
            if n > 0:
                Mn = np.array([[np.exp(betan), r * np.exp(-betan)],
                               [r * np.exp(betan), np.exp(-betan)]])
            else:
                Mn = np.array([[1, r],
                               [r, 1]])
            Bn1 = np.dot(Mn, Bn)
            Bn = Bn1
            kn = kn1
        R[i] = Bn[0][1] / Bn[0][0]
    return R
