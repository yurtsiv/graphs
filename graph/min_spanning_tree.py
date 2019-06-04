from queue import PriorityQueue
from .utils import convert_to_set_of_edges

def make_disjoint_set(nodes):
  result = {}
  for node in nodes:
    result[node] = -1
  return result

def find_set(disjoint_set, elem):
  if disjoint_set[elem] == -1:
    return elem

  return find_set(disjoint_set, disjoint_set[elem])

def union(disjoint_set, representative1, representative2):
  disjoint_set[representative1] = representative2

def MST_Kruskal(nodes):
  disjoint_set = make_disjoint_set(nodes)
  edges = convert_to_set_of_edges(nodes)
  edges.sort(key=lambda edge: edge[2], reverse=True)
  result = []

  while len(edges):
    node1, node2, weight = edges.pop()
    node1SetRep = find_set(disjoint_set, node1) 
    node2SetRep = find_set(disjoint_set, node2) 
    
    if node1SetRep != node2SetRep:
      result.append((node1, node2, weight))
      union(disjoint_set, node1SetRep, node2SetRep)

  return result

def MST_Prim(nodes):
  result = []
  active_nodes = []
  active_vertices = PriorityQueue()

  current_node = list(nodes.keys())[0]
  active_nodes.append(current_node)
  while len(result) != len(nodes) - 1:
    current_node_edges = nodes[current_node]
    for edge in current_node_edges:
      adjacent_node, weight = edge
      active_vertices.put(
        (weight, (current_node, adjacent_node, weight))
      )

    min_edge = None
    while not min_edge:
      _, posible_min_edge = active_vertices.get()
      if not posible_min_edge[1] in active_nodes:
        min_edge = posible_min_edge

    result.append(min_edge)
    active_nodes.append(min_edge[1])
    current_node = min_edge[1]
  
  return result