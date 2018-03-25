import random

from bruteforce import *
from nearestneighbour import *
from bfs import * # przeszukiwanie wszerz
from dfs import * # przeszukiwanie wgłąb


towns_count = 5
towns = [random.sample(range(100), 2) for x in range(towns_count)]  # pozycje miast x,y
print(towns)

bf_result = bruteforce(towns)
print("Win permutation: " + str(bf_result))
