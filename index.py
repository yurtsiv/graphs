from graph.graph import Graph
from graph.constants import CycleDetectionAlgs

graph = Graph(directed=True)

# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')
# graph.add_node('D')
# graph.add_node('E')
# graph.add_node('F')
# graph.add_node('G')
# graph.add_node('H')
# graph.add_node('I')
# graph.add_node('J')
# graph.add_node('K')

# graph.add_edge('A', 'B')
# graph.add_edge('B', 'C')
# graph.add_edge('C', 'A')
# graph.add_edge('B', 'D')
# graph.add_edge('D', 'E')
# graph.add_edge('E', 'F')
# graph.add_edge('F', 'D')
# graph.add_edge('G', 'F')
# graph.add_edge('G', 'H')
# graph.add_edge('H', 'I')
# graph.add_edge('I', 'J')
# graph.add_edge('J', 'G')
# graph.add_edge('J', 'K')

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 5)

graph.detect_cycles(CycleDetectionAlgs.Tarjan)