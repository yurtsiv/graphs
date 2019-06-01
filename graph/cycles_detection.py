def visit_node(node, nodes, visited_nodes):
  if node in visited_nodes:
    return True

  visited_nodes.append(node)
  for edge in nodes[node]:
    cycle_detected = visit_node(edge[0], nodes, visited_nodes)
    if cycle_detected:
      return True
  
  return False

def detect_cycles_kosaraju(graph):
  nodes = graph.nodes
  return visit_node(
    list(nodes.keys())[0],
    nodes,
    []
  )

def detect_cycles_tarjan(graph):
  return False