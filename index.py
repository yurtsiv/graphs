from graph.graph import Graph
from graph.constants import CycleDetectionAlgs

graph = Graph(directed=True)

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 5)
graph.print()
