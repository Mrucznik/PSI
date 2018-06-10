import random

ch_size = 7 


def generate_population(population_size):
    return random.sample(range(1, 2**ch_size), population_size)


def selection(func, population):
    adaptation = [func(x) for x in population]
    suma = sum(adaptation)
    current = 0
    probability = [0]
    for x in adaptation:
        current += x / suma
        probability.append(current)

    pop = []
    for _ in range(0, len(population)):
        rand = random.uniform(0, 1)
        for i in range(1, len(population)+1):
            if probability[i] >= rand > probability[i-1]:
                pop.append(population[i-1])
                break

    return pop


def get_mask(position):
    return (2**ch_size-1) - ((1 << position) - 1)


def crossing(ch1, ch2):
    locus = random.randint(1, ch_size-1)
    mask = get_mask(locus)
    return (ch1 & mask) | (ch2 & ~mask), (ch2 & mask) | (ch1 & ~mask)


def mutate(ch):
    return ch ^ (1 << random.randint(0, ch_size-1))
