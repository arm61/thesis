from pylj import md, sample


def md_simulation(
    number_of_particles, temperature, box_length, number_of_steps
):
    """
    A simple NVT ensemble molecular dynamics simulation implemented in the
    pylj package

    Parameters
    ----------
    number_of_particles: int
        Number of particles to be simulated
    temperature: float
        Temperature of thermostat (Kelvin)
    box_length: float
        Size of the periodic cell (Angstrom)
    number_of_steps: int
        Number of molecular dynamics iterations

    Returns
    -------
    System
        A pylj class containing all inform from the simulation
    """
    system = md.initialise(
        number_of_particles, temperature, box_length, "square"
    )
    sample_system = sample.Energy(system)
    system.time = 0
    for i in range(0, number_of_steps):
        system.integrate(md.velocity_verlet)
        system.md_sample()
        system.heat_bath(temperature)
        system.time += system.timestep_length
        system.step += 1
        if system.step % 10 == 0:
            sample_system.update(system)
    return system
