from math import sqrt
from constants.constants import *
import networkx as nx
import collections


class Scan(object):

    def __init__(self, eps=0.55, mu=3) -> None:
        self.__graph = None
        self.__EPS = eps
        self.__MU = mu

    def run(self, graph):
        self.__graph = graph
        self.__init_graph()
        for v in self.__graph.nodes(data=True):
            if v[1][cluster_key] is not None:
                continue
            if self.__core(v[0]):
                cluster_index = self.__get_next_cluster_index()
            queue = collections.deque()
            for w in self.__n(v[0]):
                queue.append(w)
            while len(queue):
                y = queue.pop()
                r = {x for x in self.__graph.nodes if self.__dir_reach(y, x)}
                for x in r:
                    if self.__graph.node[x][cluster_key] is None:
                        self.__graph.node[x][cluster_key] = cluster_index
                        queue.append(x)
        for node in self.__graph.nodes(data=True):
            print(node)

    def __init_graph(self):
        self.__graph.graph[next_cluster_index_key] = 0
        for node in self.__graph.nodes(data=True):
            node[1][cluster_key] = None

    def __get_next_cluster_index(self):
        next = self.__graph.graph[next_cluster_index_key]
        self.__graph.graph[next_cluster_index_key] += 1
        return next

    def __get_neighbors(self, vertex):
        result = {next_vertex for next_vertex in self.__graph[vertex]}
        result.add(vertex)
        return result

    def __delta(self, v, w):
        neighbors_v = self.__get_neighbors(v)
        neighbors_w = self.__get_neighbors(w)
        return len(neighbors_v.intersection(neighbors_w)) / sqrt(len(neighbors_v) * len(neighbors_w))

    def __n(self, v):
        return {w for w in self.__get_neighbors(v) if self.__delta(v, w) >= self.__EPS}

    def __core(self, v):
        return len(self.__n(v)) >= self.__MU

    def __dir_reach(self, v, w):
        return self.__core(v) and w in self.__n(v)
