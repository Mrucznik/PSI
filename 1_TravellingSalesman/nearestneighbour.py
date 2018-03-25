import sys
from util import *


def nearest_neighbour(towns, start_town):
    not_used_towns = list(towns)
    not_used_towns.remove(start_town)
    path_towns = [start_town]
    shortest_town = start_town

    while len(not_used_towns):
        shortest_distance_town = sys.maxsize

        for other_town in not_used_towns:
            if distance(shortest_town, other_town) < shortest_distance_town:
                shortest_distance_town = distance(shortest_town, other_town)
                shortest_town = other_town

        path_towns.append(shortest_town)
        not_used_towns.remove(shortest_town)

    return path_towns, path_distance(path_towns)


def nearest_neighbour_alltowns(towns):
    shortest_distance = sys.maxsize
    shortest_path = []

    for town in towns:
        path, distance_path = nearest_neighbour(towns, town)

        if distance_path < shortest_distance:
            shortest_distance = distance_path
            shortest_path = path

    return shortest_path, shortest_distance

