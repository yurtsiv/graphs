def convert_to_set_of_edges(nodes):
  result = []
  for node in nodes:
    for edge in nodes[node]:
      result.append((node, edge[0], edge[1]))

  result.sort(key=lambda edge: edge[2], reverse=True)
  return result

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

def kruskal_algorithm(nodes):
  disjoint_set = make_disjoint_set(nodes)
  edges = convert_to_set_of_edges(nodes)
  result = []

  while len(edges):
    node1, node2, weight = edges.pop()
    node1SetRep = find_set(disjoint_set, node1) 
    node2SetRep = find_set(disjoint_set, node2) 
    
    if node1SetRep != node2SetRep:
      result.append((node1, node2, weight))
      union(disjoint_set, node1SetRep, node2SetRep)

  return result

def prim_algorithm(node):
  pass