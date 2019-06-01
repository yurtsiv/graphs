from graph.graph import Graph
from graph.constants import MinSpanningTreeAlgs

graph = Graph(weighted=True)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 0)
graph.add_edge(1, 5, 3)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 4, 5)
graph.add_edge(3, 4, 2)
graph.add_edge(4, 5, 1)

spanning_tree = graph.get_min_spanning_tree(MinSpanningTreeAlgs.Prim)