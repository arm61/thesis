import numpy as np
import mutation as mut
import recombination as recomb
import selection as sel


def differential_evolution(
    population, f, km, kr, bounds, stop, max_iter
):
    """
    An implementaiton of a differential evolution algorithm.

    Parameters
    ----------
    population: float, array_like
        The initial parent population vector. An array of
        shape (i, j), where i is the number of varibles and
        j is the population size.
    f: function
        The figure of merit function to be minimised.
    km: float
        The mutation constant.
    kr: float
        The recombination constant.
    bounds: float, array_like
        The minimum and maximum values for the bounds.
    stop: float
        The value at which the optimisation should stop.
    max_iter: int
        The maximum number of iterations that should be performed
        regardless of if stop is reached.

    Returns
    -------
    float, array_like
        The history of the parameters being fit. An array of
        shape (m, n, j), where n is the number of iterations,
        m is the number of parameters, and j is the population
        size.
    """
    history = np.array([population])
    best = population[:, np.argmin(f(population))]
    i = 0
    while f(best) > stop and i < max_iter:
        mutant = mut.mutation(population, best, km)
        offspring = recomb.recombination(population, mutant, kr)
        offspring[
            np.where(offspring >= bounds[1])
            or np.where(offspring < bounds[0])
        ] = np.random.uniform(bounds[0], bounds[1], 1)
        selected = sel.selection(population, offspring, f)
        history = np.append(history, selected)
        history = np.reshape(
            history, (i + 2, population.shape[0], population.shape[1])
        )
        population = np.array(selected)
        best = population[:, np.argmin(f(population))]
        i += 1
    return history
