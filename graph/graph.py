class Graph:
  def __init__(self, weighted = False, directed = False):
    self.nodes = {} 
    self.weighted = weighted
    self.directed = directed
  
  def check_node_exists(self, key):
    if not key in self.nodes:
      raise Exception("There is no node " + str(key) + " in the graph")

  def add_node(self, key):
    if key in self.nodes:
      raise Exception("Node " + str(key) + " already exists")

    self.nodes[key] = []
  
  def remove_single_edge(self, node, neighbour):
    self.nodes[node] = list(
      edge for edge in self.nodes[node] if edge[0] != neighbour
    )
  
  def modify_single_edge(self, node1, node2, modify_func):
    self.nodes[node1] = list(map(
      lambda edge: modify_func(edge) if edge[0] == node2 else edge,
      self.nodes[node1]
    ))

  def remove_node(self, node_to_remove):
    self.check_node_exists(node_to_remove)

    if self.directed:
      for node in self.nodes:
        self.remove_single_edge(node, node_to_remove)
    else:
      for edge in self.nodes[node_to_remove]:
        self.remove_single_edge(edge[0], node_to_remove)

    del self.nodes[node_to_remove]

  def add_edge(self, key1, key2, weight=0):
    self.check_node_exists(key1)
    self.check_node_exists(key2)

    if self.directed or key1 == key2:
      self.nodes[key1].append((key2, weight))
    else:
      self.nodes[key1].append((key2, weight))
      self.nodes[key2].append((key1, weight))

  def remove_edge(self, key1, key2):
    self.check_node_exists(key1)
    self.check_node_exists(key2)

    self.remove_single_edge(key1, key2)
    if not self.directed:
      self.remove_single_edge(key2, key1)
  
  def update_weight(self, key1, key2, new_weight):
    if not self.weighted:
      raise Exception("Graph is not weighted")
    self.check_node_exists(key1)
    self.check_node_exists(key2)
    
    self.modify_single_edge(key1, key2, lambda x: (x[0], new_weight))
    if not self.directed:
      self.modify_single_edge(key2, key1, lambda x: (x[0], new_weight))
  
  def update_node(self, original_key, updated_key):
    self.check_node_exists(original_key)
    if updated_key in self.nodes:
      raise Exception("Can't update node to " + updated_key + " since such node already exists")

    if self.directed:
      for node in self.nodes:
        self.modify_single_edge(node, original_key, lambda x: (updated_key, x[1]))
    else:
      for edge in self.nodes[original_key]:
        self.modify_single_edge(edge[0], original_key, lambda x: (updated_key, x[1]))

    self.nodes[updated_key] = self.nodes[original_key]
    del self.nodes[original_key]
  
  def get_node_degree(self, key):
    self.check_node_exists(key)
    if not self.directed:
      return len(self.nodes[key])

    degree = len(self.nodes[key])
    for node in self.nodes:
      for edge in self.nodes[node]:
        if edge[0] == key:
          degree += 1

    return degree

  
  def print(self):
    print("Directed: " + self.directed)
    print("Weighted: " + self.directed)
    print("Nodes:")
    for node in self.nodes:
      print(str(node) + " | ")

    if self.weighted:
      print("Edges (node, weight):")
    else:
      print("Edges:")
    
    for node in self.nodes:
      for edge in self.nodes[node]:
        if self.weighted:
          print("(" + str(edge[0]) + ", " + str(edge[1]) + ") | ")
        else:
          print(str(edge[0]))
