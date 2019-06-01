import math
from queue import PriorityQueue

def get_min_weight_node(weights, nodes):
  min_weight_node = (nodes[0], weights[nodes[0]])
  for node in nodes:
    if weights[node] < min_weight_node[1]:
      min_weight_node = (node, weights[node])
  return min_weight_node

def dijkstra_shortest_path(nodes, origin):
  result = {}
  for node in nodes:
    result[node] = math.inf

  # mark direct neighbours of origin
  result[origin] = 0
  for origin_edge in nodes[origin]:
    result[origin_edge[0]] = origin_edge[1]
  
  unvisited_nodes = list(filter(lambda node: node != origin, nodes))
  
  while len(unvisited_nodes) != 0:
    min_weight_node, min_weight = get_min_weight_node(result, unvisited_nodes)
    if min_weight < 0:
      raise Exception("Dijsktra's alogrithm doesn't work for graphs with negative weights")

    unvisited_nodes.remove(min_weight_node)

    for edge in nodes[min_weight_node]:
      new_weight = min_weight + edge[1]
      neighbour = edge[0]
      if new_weight < result[neighbour]:
        result[neighbour] = new_weight

  return result

def bellman_ford_shortes_path(nodes, origin):
  pass