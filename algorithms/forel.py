import networkx as nx

from constants.constants import *


class Forel():

    def __init__(self, graph, r=5, is_update_sp=True):
        self.__graph = graph
        self.__R = r
        self.__is_update_sp = is_update_sp
        self.__init_shores_path()

    def run(self):
        print('run')
        self.__init_graph()
        print(self.__init_cluster_center())

    def __init_graph(self):
        for node in self.__graph.nodes(data=True):
            node[1][cluster_key] = None

    def __init_cluster_center(self):
        cluster_centers = [nx.center(self.__graph, e=nx.eccentricity(self.__graph, self.__sp))[0]]
        return cluster_centers

    def __init_shores_path(self):
        self.__sp = {}
        if self.__is_update_sp:
            for node in self.__graph.nodes:
                self.__sp.update({node: nx.shortest_path_length(self.__graph, node, weight=weight_key)})
