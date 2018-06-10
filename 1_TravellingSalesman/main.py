import random
import time
from bruteforce import *
from nearestneighbour import *
from bfs import *


towns_count = 10
towns = [random.sample(range(100), 2) for x in range(towns_count)]  # pozycje miast x,y
print("Towns positions: " + str(towns))

time_elapsed = time.time()
bf_result = bruteforce(towns)
print("Bruteforce win path (time: " + str(time.time() - time_elapsed) + " ): " + str(bf_result))

time_elapsed = time.time()
bf_result = nearest_neighbour(towns, towns[random.randint(0, len(towns)-1)])
print("NN win path: (time: " + str(time.time() - time_elapsed) + " ): " + str(bf_result))

time_elapsed = time.time()
bf_result = nearest_neighbour_alltowns(towns)
print("NN for all towns win path: (time: " + str(time.time() - time_elapsed) + " ): " + str(bf_result))
