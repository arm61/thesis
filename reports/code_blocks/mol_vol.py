import numpy as np
from refnx.analysis import possibly_create_parameter as pcp
from refnx.analysis import Parameters
from refnx.reflect import Component


class VolMono(Component):
    def __init__(self, vol, b, d_h, c_length, name=""):
        """
        The custom model class to enable control of the
        phospholipid head and tail volumes.

        Parameters
        ----------
        vol: float, array_like
            The initial values for the head and tail group volumes.
        b: complex, array_like
            The calculated scattering length for the head and tail
            groups.
        d_h: float
            The initial value for the thickness of the head group
            region.
        c_length: int
            Number of carbon atoms in the phospholipid tail.
        name: str
            A name to be given to the object.
        """
        super(VolMono, self).__init__()
        t_t = 1.54 + 1.265 * c_length
        self.vol = [
            pcp(vol[0], "{}-V_h".format(name)),
            pcp(vol[1], "{}-V_t".format(name)),
        ]
        self.realb = [
            pcp(b[0].real, name="{}-b_h".format(name)),
            pcp(b[1].real, name="{}-b_t".format(name)),
        ]
        self.imagb = [
            pcp(b[0].imag, name="{}-ib_h".format(name)),
            pcp(b[1].imag, name="{}-ib_t".format(name)),
        ]
        self.d = [
            pcp(d_h, name="{}-d_h".format(name)),
            pcp(t_t * 0.8, name="{}-d_t".format(name)),
        ]
        self.phi = [
            pcp(0.5, name="{}-phi_h".format(name)),
            pcp(0.0, name="{}-phi_t".format(name)),
        ]
        self.sigma = pcp(3.0, name="{}-sigma".format(name))
        self.name = name

    @property
    def slabs(self):
        """
        Returns
        -------
        float, array_like
            Slab representaions of phospholipid monolayer.
        """
        layers = np.zeros((2, 5))
        layers[0, 0] = self.d[1]
        layers[0, 1] = self.realb[1] * 1.0e16 / self.vol[1]
        layers[0, 2] = self.imagb[1] * 1.0e16 / self.vol[1]
        layers[0, 3] = self.sigma
        layers[0, 4] = self.phi[1]
        layers[1, 0] = self.d[0]
        layers[1, 1] = self.realb[0] * 1.0e16 / self.vol[0]
        layers[1, 2] = self.imagb[0] * 1.0e16 / self.vol[0]
        layers[1, 3] = self.sigma
        layers[1, 4] = self.phi[0]
        return layers

    @property
    def parameters(self):
        """
        Returns
        -------
        Parameter, array_like
            An array of the parameters in the fitting.
        """
        p = Parameters(name=self.name)
        p.extend(
            [
                self.vol[0],
                self.vol[1],
                self.realb[0],
                self.realb[1],
                self.imagb[0],
                self.imagb[1],
                self.d[0],
                self.d[1],
                self.phi[0],
                self.phi[1],
                self.sigma,
            ]
        )
        return p

    def lnprob(self):
        """
        Returns
        -------
        float
            The contribution of the monolayer to the posterior
            probability.
        """
        return 0
