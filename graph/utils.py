import graph

def convert_to_set_of_edges(nodes):
  result = []
  for node in nodes:
    for edge in nodes[node]:
      result.append((node, edge[0], edge[1]))

  return result

def reverse_directed_graph(nodes):
  reversed_graph = graph.Graph(directed=True)
  for node in nodes:
    reversed_graph.add_node(node)

  for node in nodes:
    for edge in nodes[node]:
      reversed_graph.add_edge(edge[0], node, edge[1])
 
  return reversed_graph
