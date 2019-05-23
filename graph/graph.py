class Graph:
  def __init__(self, weighted = False, directed = False):
    self.nodes = set()
    self.edges = set()
    self.weighted = weighted
    self.directed = directed
    