import random
import networkx as nx
from constants.constants import *

__shortens_path = {}


def __generate_shortens_path(graph, update=False):
    if update:
        for node in graph.nodes:
            __shortens_path.update({node: nx.shortest_path_length(graph, node, weight=weight_key)})
    # else:


def run(graph, cluster_count):
    __generate_shortens_path(graph)
    cluster_center_nodes = __init_center_node(graph, cluster_count)
    print("center nodes: %s" % cluster_center_nodes)
    while __update_cluster(graph, cluster_center_nodes):
        cluster_center_nodes = __update_cluster_centers(graph, cluster_count)
    print(graph.nodes(data=True))


def __update_cluster(graph, center_nodes):
    any_update = False
    for target_node in graph.nodes(data=True):
        min_length = {node_name_key: None, length_key: None}
        for center_node in center_nodes:
            length_to_target = __shortens_path[center_node][target_node[0]]
            if min_length[length_key] is None or length_to_target < min_length[length_key]:
                min_length[node_name_key] = center_node
                min_length[length_key] = length_to_target

        if __update_node_cluster(target_node, center_nodes.index(min_length[node_name_key])):
            any_update = True

    return any_update


def __update_node_cluster(node, cluster):
    if node[1][cluster_key] is not cluster:
        node[1][cluster_key] = cluster
        return True
    return False


def __update_cluster_centers(graph, count_of_cluster):
    new_centers = []
    for cluster_index in range(0, count_of_cluster):
        node_in_cluster = [node[0] for node in graph.nodes(data=True) if node[1][cluster_key] == cluster_index]
        sub_sp = {}
        for from_node in node_in_cluster:
            from_node_len = {}
            for to_node in node_in_cluster:
                from_node_len.update({to_node: __shortens_path[from_node][to_node]})
            sub_sp.update({from_node: from_node_len})

        subgraph = nx.subgraph(graph, node_in_cluster)
        cluster_centers = nx.center(subgraph, e=nx.eccentricity(subgraph, sp=sub_sp))
        new_centers.append(cluster_centers[0])
    return new_centers


def __init_center_node(graph, cluster_count):
    return ['01', '11', '21']
    # return random.sample(graph.nodes, cluster_count)
