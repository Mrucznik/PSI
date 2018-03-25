import math


def distance(a, b):
    return math.sqrt(math.pow(b[0]-a[0], 2) + math.pow(b[1]-a[1], 2))


def path_distance(path):
    last_town = -1
    distance_sum = 0
    for town in path:
        if last_town == -1:
            last_town = town
            continue
        distance_sum += distance(last_town, town)
        last_town = town
    return distance_sum
