from utils.graph_utils import *


def generate_simple_test_graph():
    graph = create_graph('simple_test_graph')

    graph.add_node('00', cluster=0)
    graph.add_node('01', cluster=0)
    graph.add_node('02', cluster=0)
    graph.add_node('03', cluster=0)
    graph.add_node('04', cluster=0)

    graph.add_node('10', cluster=0)
    graph.add_node('11', cluster=0)
    graph.add_node('12', cluster=0)
    graph.add_node('13', cluster=0)
    graph.add_node('14', cluster=0)

    graph.add_node('20', cluster=0)
    graph.add_node('21', cluster=0)
    graph.add_node('22', cluster=0)
    graph.add_node('23', cluster=0)
    graph.add_node('24', cluster=0)

    graph.add_edge('00', '01', weight=1)
    graph.add_edge('00', '02', weight=2)
    graph.add_edge('00', '03', weight=3)
    graph.add_edge('00', '04', weight=4)

    graph.add_edge('10', '11', weight=1)
    graph.add_edge('10', '12', weight=2)
    graph.add_edge('10', '13', weight=3)
    graph.add_edge('10', '14', weight=4)

    graph.add_edge('20', '21', weight=1)
    graph.add_edge('20', '22', weight=2)
    graph.add_edge('20', '23', weight=3)
    graph.add_edge('20', '24', weight=4)

    graph.add_edge('04', '12', weight=8)
    graph.add_edge('04', '21', weight=8)
    graph.add_edge('21', '13', weight=8)

    save_graph(graph)

    print("""simple_test_graph is generated.
        count of nodes: {0}
        count of edges: {1}""".format(len(graph.nodes), len(graph.edges)))
    return graph
