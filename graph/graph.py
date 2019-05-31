class Graph:
  def __init__(self, weighted = False, directed = False):
    self.nodes = {} 
    self.weighted = weighted
    self.directed = directed
  
  def raise_no_node_exception(self, key):
    raise Exception("There is no node " + str(key) + " in the graph")
  
  def check_nodes_exist(self, key1, key2):
    if not key1 in self.nodes:
      self.raise_no_node_exception(key1)
    if not key2 in self.nodes:
      self.raise_no_node_exception(key2)

  def add_node(self, key):
    if key in self.nodes:
      self.raise_no_node_exception(key)

    self.nodes[key] = []

  def remove_node(self, key):
    if not key in self.nodes:
      self.raise_no_node_exception(key) 
    
    for edge in self.nodes[key]:
      liked_node = edge[0]
      self.nodes[liked_node] = list(
        edge for edge in self.nodes[liked_node] if edge[0] != key
      )
    
    del self.nodes[key]
        
  def add_edge(self, key1, key2, weight=0):
    self.check_nodes_exist(key1, key2)

    if self.directed:
      self.nodes[key1].append((key2, weight))
    else:
      self.nodes[key1].append((key2, weight))
      self.nodes[key2].append((key1, weight))

  def remove_edge(self, key1, key2):
    self.check_nodes_exist(key1, key2)

    self.nodes[key1] = list(
      edge for edge in self.nodes[key1] if edge[0] != key2
    )
    self.nodes[key2] = list(
      edge for edge in self.nodes[key2] if edge[0] != key1
    )
  
  def update_weight(self, key1, key2, new_weight):
    if not self.weighted:
      raise Exception("Graph is not weighted")

    self.check_nodes_exist(key1, key2)
    
    self.nodes[key1] = list(map(
      lambda edge: (key2, new_weight) if edge[0] == key2 else edge,
      self.nodes[key1]
    ))

    if not self.directed:
      self.nodes[key2] = list(map(
        lambda edge: (key1, new_weight) if edge[0] == key1 else edge,
        self.nodes[key2]
      ))