from utils import graph_generator, graph_utils
from algorithms import k_means
from constants.constants import *
import random
import networkx as nx
import json
from algorithms.forel import Forel

graph = graph_utils.load_graph('simple_test_graph')

# start_time = time.time()
# graph.add_weighted_edges_from((index, index + 1, random.randint(0, 100)) for index in range(0, max_count))
# print("graph.add_weighted_edges_from")
# print("--- %s seconds ---" % (time.time() - start_time))

f = Forel(graph)
f.run()
