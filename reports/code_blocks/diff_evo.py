import numpy as np
import mutation as mut
import recombination as recomb
import selection as sel


def differential_evolution(population, f, km, kr, bounds, max_iter):
    history = np.array([population])
    best = population[:, np.argmin(f(population))]
    i = 0
    while i < max_iter:
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
