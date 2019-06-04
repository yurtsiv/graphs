from .utils import reverse_directed_graph

def visit_node(node, nodes, visited_nodes, nodes_stack):
  if node in visited_nodes:
    return

  visited_nodes.append(node)

  for edge in nodes[node]:
    visit_node(edge[0], nodes, visited_nodes, nodes_stack)
  
  nodes_stack.append(node)

def detect_cycle(
  nodes,
  node,
  visited_nodes,
  nodes_stack
):
  visited_nodes.append(node)
  for edge in nodes[node]:
    if not edge[0] in visited_nodes:
      return True

  if len(visited_nodes) == len(nodes):
    return False

  next_node_to_visit = nodes_stack.pop() 
  return detect_cycle(
    nodes,
    next_node_to_visit,
    visited_nodes,
    nodes_stack,
  )

def detect_cycles_kosaraju(graph):
  nodes = graph.nodes
  stack_by_finish_time = []
  visited_nodes = []

  # create stack of nodes (by visit finish time)
  while(len(stack_by_finish_time) != len(nodes)):
    unvisited_node = set(nodes).difference(visited_nodes).pop()
    visit_node(
      unvisited_node,
      nodes,
      visited_nodes,
      stack_by_finish_time
    )

  reversed_graph = reverse_directed_graph(nodes)
  return detect_cycle(
    reversed_graph.nodes,
    stack_by_finish_time.pop(),
    [],
    stack_by_finish_time,
  )


def detect_cycles_tarjan(graph):
  return False