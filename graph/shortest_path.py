import math
from queue import PriorityQueue
from .utils import convert_to_set_of_edges

def get_min_weight_node(weights, nodes):
  min_weight_node = (nodes[0], weights[nodes[0]])
  for node in nodes:
    if weights[node] < min_weight_node[1]:
      min_weight_node = (node, weights[node])
  return min_weight_node

def dijkstra_shortest_path(nodes, origin):
  weights = {}
  for node in nodes:
    weights[node] = math.inf

  # mark direct neighbours of origin
  weights[origin] = 0
  for origin_edge in nodes[origin]:
    weights[origin_edge[0]] = origin_edge[1]
  
  unvisited_nodes = list(filter(lambda node: node != origin, nodes))
  
  while len(unvisited_nodes) != 0:
    min_weight_node, min_weight = get_min_weight_node(weights, unvisited_nodes)
    if min_weight < 0:
      raise Exception("Dijsktra's alogrithm doesn't work for graphs with negative weights")

    unvisited_nodes.remove(min_weight_node)

    for edge in nodes[min_weight_node]:
      new_weight = min_weight + edge[1]
      neighbour = edge[0]
      if new_weight < weights[neighbour]:
        weights[neighbour] = new_weight

  return weights

def relax_nodes(edges, weights):
  relaxed = False
  for edge in edges:
    node1, node2, weight = edge
    if (weights[node1] + weight) < weights[node2]:
      relaxed = True
      weights[node2] = weights[node1] + weight

  return relaxed

def bellman_ford_shortes_path(nodes, origin):
  weights = {}
  for node in nodes:
    if node == origin:
      weights[node] = 0
    else:
      weights[node] = math.inf
  
  edges = convert_to_set_of_edges(nodes)
  
  for _ in range(0, len(nodes) - 1):
    relax_nodes(edges, weights)

  if relax_nodes(edges, weights):
    raise Exception("Can't calculate shortest paths. There is a negative weight cycle in the graph")

  return weights
