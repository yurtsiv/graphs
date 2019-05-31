class Graph:
  def __init__(self, weighted = False, directed = False):
    self.nodes = {} 
    self.weighted = weighted
    self.directed = directed
  
  def add_node(self, key):
    if key in self.nodes:
      raise Exception("Node with key " + str(key) + " already exists")

    self.nodes[key] = []


  def add_edge(self, key1, key2, weight=0):
    if not key1 in self.nodes:
      raise Exception("There is no node " + str(key1) + " in the graph")
    if not key2 in self.nodes:
      raise Exception("There is no node " + str(key2) + " in the graph")

    if self.directed:
      self.nodes[key1].append((key2, weight))
    else:
      self.nodes[key1].append((key2, weight))
      self.nodes[key2].append((key1, weight))
