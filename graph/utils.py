def convert_to_set_of_edges(nodes):
  result = []
  for node in nodes:
    for edge in nodes[node]:
      result.append((node, edge[0], edge[1]))

  return result