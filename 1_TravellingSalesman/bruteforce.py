import itertools
from util import *
import sys


def bruteforce(towns):
    shortest_distance = sys.maxsize
    win_permutation = []
    paths = itertools.permutations(towns, len(towns))

    for path in paths:
        distance_sum = path_distance(path)
        if distance_sum < shortest_distance:
            shortest_distance = distance_sum
            win_permutation = path

    return win_permutation, shortest_distance

