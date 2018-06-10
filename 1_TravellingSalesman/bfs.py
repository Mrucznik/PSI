import queue
import sys
import util

WHITE = 0
GRAY = 1
BLACK = 2


def breadth_first_search(towns, start_town):
    q = queue.Queue()
    colour = {}
    distance = {}

    for town in range(0, len(towns)):
        colour[town] = WHITE
        distance[town] = sys.maxsize

    colour[start_town] = GRAY
    distance[start_town] = 0

    q.put(start_town)
    while not q.empty():
        u = q.get()
        neighbours = list(range(0, len(towns)))
        neighbours.remove(u)
        for town in neighbours:
            if colour[town] == WHITE:
                colour[town] = GRAY
                distance[town] = util.distance(towns[u], towns[town])
                q.put(town)
        colour[u] = BLACK

