import numpy as np
from genetic import *

# ustawienia
population_size = 10
mutation_chance = 0.01


def func(x):
    return 2*(x*x+1)


pop = generate_population(population_size)
for _ in range(100):
    print(pop)
    pop = selection(func, pop)

    crossed_pop = []
    rp = np.random.permutation(len(pop))
    for i, j in zip(rp[0::2], rp[1::2]):
        c1, c2 = crossing(pop[i], pop[j])

        if random.random() < mutation_chance:
            crossed_pop.append(mutate(c1))
        else:
            crossed_pop.append(c1)
        if random.random() < mutation_chance:
            crossed_pop.append(mutate(c2))
        else:
            crossed_pop.append(c2)

    pop = crossed_pop

print(pop)
