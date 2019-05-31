from .node import Node

class Graph:
  def __init__(self, weighted = False, directed = False):
    self.nodes = []
    self.weighted = weighted
    self.directed = directed
  
  def add_node(self, key):
    if any(node.key == key for node in self.nodes):
      raise Exception("Node with key " + str(key) + " already exists")

    new_node = Node(key)
    self.nodes.append(new_node)
    return new_node
  
  def add_edge(self, key1, key2, weight=0):
    node1 = next(node for node in self.nodes if node.key == key1) 
    if not node1:
      raise Exception("There is no node " + str(key1) + " in the graph")
    
    node2 = next(node for node in self.nodes if node.key == key2) 
    if not node2:
      raise Exception("There is no node " + str(key2) + " in the graph")

    if self.directed:
      node1.add_link(node2, weight)
    else:
      node1.add_link(node2, weight)
      node2.add_link(node1, weight)
    