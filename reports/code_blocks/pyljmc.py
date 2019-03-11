def mc_simulation(
    number_of_particles, temperature, box_length, number_of_steps
):
    """
    A simple NVT ensemble Monte Carlo simulation implemented in the
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
        Number of Monte Carlo iterations

    Returns
    -------
    System
        A pylj class containing all inform from the simulation
    """
    system = mc.initialise(
        number_of_particles, temperature, box_length, "square"
    )
    sample_system = sample.Energy(system)
    system.compute_energy()
    system.old_energy = system.energies.sum()
    system.mc_sample()
    for i in range(0, number_of_steps):
        system.step += 1
        system.select_random_particle()
        system.new_random_position()
        system.compute_energy()
        system.new_energy = system.energies.sum()
        if mc.metropolis(
            temperature, system.old_energy, system.new_energy
        ):
            system.accept()
        else:
            system.reject()
        system.mc_sample()
        if system.step % 10 == 0:
            sample_system.update(system)
    return system
