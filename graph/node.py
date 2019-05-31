from uuid import uuid4

class Node:
  def __init__(self, key):
    self.id = uuid4() 
    self.key = key
    self.weight = None
    self.links = []
  
  def add_link(self, node, weight):
    self.links.append((node, weight))