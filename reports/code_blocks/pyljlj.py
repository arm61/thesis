import numpy as np


def lennard_jones(dr, constants, force=False):
    if force:
        return 12 * constants[0] * np.power(dr, -13) - (
            6 * constants[1] * np.power(dr, -7)
        )
    else:
        return constants[0] * np.power(dr, -12) - (
            constants[1] * np.power(dr, -6)
        )
