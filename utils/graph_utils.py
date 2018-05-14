import json
import networkx as nx
from constants.constants import *
import networkx.readwrite.json_graph as json_graph

__splitter__ = '/'
__file_prefix__ = 'graph_files'
__file_format__ = '.json'
__default_graph_name__ = 'default_name'
__centers_suffix = '_centers'
__cp_suffix = '_cp'


def save_graph_sp(graph, sp):
    __save_data(sp, suffix=__cp_suffix, file_name=graph.graph[graph_name_key])


def save_graph_centers(graph, centers):
    __save_data(data=centers, suffix=__centers_suffix)


def save_graph(graph, suffix=''):
    data = json_graph.node_link_data(graph)
    __save_data(data, graph.graph[graph_name_key], suffix=suffix)


def save_graph_cp(graph, cp):
    __save_data(data=cp, suffix=__cp_suffix)


def __save_data(data, file_name, suffix='', prefix=''):
    with open(__get_full_file_name(file_name, suffix, prefix), 'w') as file:
        json.dump(data, file)


def load_graph(graph_name=__default_graph_name__, suffix='', prefix=''):
    graph = create_graph(graph_name)
    data = __load_data(graph_name, suffix=suffix, prefix=prefix)
    graph.add_nodes_from((node[id_key], {cluster_key: node[cluster_key]}) for node in data[nodes_key])
    graph.add_weighted_edges_from((link[from_key], link[to_key], link[weight_key]) for link in data[links_key])

    return graph


def load_cp(file_name, prefix='', suffix=''):
    return __load_data(file_name, suffix=suffix + __cp_suffix, prefix=prefix)


def load_centers(file_name, prefix='', suffix=''):
    return __load_data(file_name, suffix=suffix + __centers_suffix, prefix=prefix)


def __load_data(file_name, suffix='', prefix=''):
    with open(__get_full_file_name(file_name, suffix, prefix)) as file:
        return json.load(file)


def create_graph(graph_name=__default_graph_name__):
    return nx.Graph(name=graph_name)


def __get_full_file_name(graph_name, name_suffix='', name_prefix=''):
    return __file_prefix__ + __splitter__ + name_suffix + graph_name + name_prefix + __file_format__
