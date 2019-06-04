from .utils import reverse_directed_graph

def _visit_node_kosaraju(node, nodes, visited_nodes, nodes_stack):
  if node in visited_nodes:
    return

  visited_nodes.append(node)
  # DFS
  for edge in nodes[node]:
    _visit_node_kosaraju(edge[0], nodes, visited_nodes, nodes_stack)
  
  nodes_stack.append(node)

def _detect_cycle_kosaraju(
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
  return _detect_cycle_kosaraju(
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
    _visit_node_kosaraju(
      unvisited_node,
      nodes,
      visited_nodes,
      stack_by_finish_time
    )

  reversed_graph = reverse_directed_graph(nodes)
  return _detect_cycle_kosaraju(
    reversed_graph.nodes,
    stack_by_finish_time.pop(),
    [],
    stack_by_finish_time,
  )

def _detect_cycle_tarjan(
  nodes,
  node,
  nodes_props,
  index_counter,
  stack
):
  nodes_props[node] = {
    'index': index_counter,
    'low_link': index_counter,
  }

  index_counter += 1
  stack.append(node)

  # DFS
  for edge in nodes[node]:
    neighbour = edge[0]

    # if not visited yet
    if nodes_props[neighbour]['index'] == -1:
      cycle_detected, index_counter = _detect_cycle_tarjan(
        nodes,
        neighbour,
        nodes_props,
        index_counter,
        stack
      )

      if cycle_detected:
        return (True, index_counter)

      # update node's low_link to neighbour's if it's lower
      nodes_props[node]['low_link'] = min(
        nodes_props[node]['low_link'],
        nodes_props[neighbour]['index']
      )

    elif neighbour in stack:
      # update node's low_link to neighbour's if it's lower
      nodes_props[node]['low_link'] = min(
        nodes_props[node]['low_link'],
        nodes_props[neighbour]['index']
      )
  
  node_props = nodes_props[node]
  # reached strongly connected components' "root"
  if node_props['low_link'] == node_props['index']:
    strongly_connected_comp_len = 0
    while stack.pop() != node:
      strongly_connected_comp_len += 1

    # if there are more than one strongly connected components there is a cycle
    return (
      strongly_connected_comp_len > 0,
      index_counter
    )
  else:
    return (False, index_counter)

def detect_cycles_tarjan(graph):
  nodes_props = {}
  index_counter = 0
  stack = []

  for node in graph.nodes:
    nodes_props[node] = {
      'index': -1,
      'low_link': -1
    }

  for node in graph.nodes:
    if nodes_props[node]['index'] == -1:
      cycle_detected, index_counter = _detect_cycle_tarjan(
        graph.nodes,
        node,
        nodes_props,
        index_counter, 
        stack
      )

      if cycle_detected:
        return True
  
  return False