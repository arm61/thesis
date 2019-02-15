import numpy as np
import periodictable as pt


def set_constraints(
    lipids,
    structures,
    hold_tails=False,
    hold_rough=False,
    hold_phih=False,
):
    i = 0
    lipids[i].phi[0].constraint = 1 - (
        lipids[0].vol[0] / lipids[0].vol[1]
    ) * (lipids[i].d[1] / lipids[i].d[0])
    lipids[i].sigma.constraint = structures[i][-1].rough
    for i in range(1, len(lipids)):
        lipids[i].vol[0].constraint = lipids[0].vol[0]
        lipids[i].vol[1].constraint = lipids[0].vol[1]
        lipids[i].d[0].constraint = lipids[0].d[0]
        if hold_tails:
            lipids[i].d[1].constraint = lipids[0].d[1]
        lipids[i].phi[0].constraint = 1 - (
            lipids[i].vol[0] / lipids[i].vol[1]
        ) * (lipids[i].d[1] / lipids[i].d[0])
        lipids[i].phi[1].constraint = lipids[0].phi[1]
        if hold_rough:
            structures[i][-1].rough.constraint = structures[0][
                -1
            ].rough
        lipids[i].sigma.constraint = structures[i][-1].rough
        if hold_phih:
            lipids[i].phi[0].constraint = lipids[0].phi[0]
    return lipids


def get_scattering_length(component, neutron=False):
    if not neutron:
        scattering_length = 0 + 0j
        import scipy.constants as const

        cre = const.physical_constants["classical electron radius"][0]
        for key in component:
            scattering_length += np.multiply(
                pt.elements.symbol(key).xray.scattering_factors(
                    energy=12
                )[0],
                cre * component[key],
            )
            scattering_length += (
                np.multiply(
                    pt.elements.symbol(key).xray.scattering_factors(
                        energy=12
                    )[1],
                    cre * component[key],
                )
                * 1j
            )
    else:
        scattering_length = 0 + 0j
        for key in component:
            scattering_length += (
                pt.elements.symbol(key).neutron.b_c * component[key]
            )
            if pt.elements.symbol(key).neutron.b_c_i:
                inc = pt.elements.symbol(key).neutron.b_c_i
            else:
                inc = 0
                scattering_length += inc * 1j * component[key]
        scattering_length *= 1e-15
    return scattering_length
