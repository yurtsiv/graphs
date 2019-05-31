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

  def remove_node(self, key):
    self.check_node_exists(key)

    if self.directed:
      for node in self.nodes:
        self.nodes[node] = list(
          edge for edge in self.nodes[node] if edge[0] != key
        )
    else:
      for edge in self.nodes[key]:
        liked_node = edge[0]
        self.nodes[liked_node] = list(
          edge for edge in self.nodes[liked_node] if edge[0] != key
        )

    del self.nodes[key]

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

    self.nodes[key1] = list(
      edge for edge in self.nodes[key1] if edge[0] != key2
    )

    if not self.directed:
      self.nodes[key2] = list(
        edge for edge in self.nodes[key2] if edge[0] != key1
      )
  
  def update_weight(self, key1, key2, new_weight):
    if not self.weighted:
      raise Exception("Graph is not weighted")
    self.check_node_exists(key1)
    self.check_node_exists(key2)
    
    self.nodes[key1] = list(map(
      lambda edge: (key2, new_weight) if edge[0] == key2 else edge,
      self.nodes[key1]
    ))

    if not self.directed:
      self.nodes[key2] = list(map(
        lambda edge: (key1, new_weight) if edge[0] == key1 else edge,
        self.nodes[key2]
      ))
  
  def update_node(self, original_key, updated_key):
    self.check_node_exists(original_key)
    if updated_key in self.nodes:
      raise Exception("Can't update node to " + updated_key + " since such node already exists")
    
    for edge in self.nodes[original_key]:
      liked_node = edge[0]
      self.nodes[liked_node] = list(map(
        lambda edge: (updated_key, edge[1]) if edge[0] == original_key else edge,
        self.nodes[liked_node]
      ))

    self.nodes[updated_key] = self.nodes[original_key]
    del self.nodes[original_key]  