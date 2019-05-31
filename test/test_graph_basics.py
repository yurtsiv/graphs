import unittest

from graph.graph import Graph

class TestGraphBasics(unittest.TestCase):
  def test_add_node(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)

    self.assertEqual(graph.nodes, {
      1: [],
      2: []
    })
    self.assertRaises(Exception, Graph.add_node, 1)

  def test_add_edge_undirected(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    self.assertEqual(graph.nodes, {
      1: [(2, 0)],
      2: [(1, 0)]
    })
    self.assertRaises(Exception, Graph.add_edge, 0, 3)
  
  def test_add_edge_directed(self):
    graph = Graph(directed=True)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    self.assertEqual(graph.nodes, {
      1: [(2, 0)],
      2: []
    })

  def test_remove_node_directed(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(1,3)

    graph.remove_node(1)

    self.assertEqual(graph.nodes, {
      2: [(3,0)],
      3: [(2, 0)]
    })
  
  def test_remove_node_undirected(self):
    graph = Graph(directed=True)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1,2)
    graph.add_edge(2,1)
    graph.add_edge(2,3)
    graph.add_edge(3, 1)

    graph.remove_node(1)

    self.assertEqual(graph.nodes, {
      2: [(3,0)],
      3: []
    })

  def test_remove_edge(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(1,3)

    graph.remove_edge(1, 3)
    expected_val = {
      1: [(2, 0)],
      2: [(1, 0), (3,0)],
      3: [(2, 0)]
    }

    self.assertEqual(graph.nodes, expected_val)

    graph.remove_edge(1, 3)
    self.assertEqual(graph.nodes, expected_val)

    self.assertRaises(Exception, Graph.remove_edge, 0, 1)
    self.assertRaises(Exception, Graph.remove_edge, 1, 5)
  
  def test_weight_update(self):
    graph = Graph(weighted=True)
    graph.add_node("Node 1")
    graph.add_node("Node 2")

    graph.add_edge("Node 1", "Node 2", 10)
    
    graph.update_weight("Node 1", "Node 2", 5)
    self.assertEqual(graph.nodes, {
      "Node 1": [("Node 2", 5)],
      "Node 2": [("Node 1", 5)],
    })

    self.assertRaises(Exception, graph.update_weight, "Node 0", "Node 2", 5)
    self.assertRaises(Exception, graph.update_weight, "Node 1", "Node 4", 5)
  
  def test_update_node_undireted(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(1,3)

    graph.update_node(1, 4)

    self.assertEqual(graph.nodes, {
      4: [(2, 0), (3, 0)],
      2: [(4, 0), (3, 0)],
      3: [(2, 0), (4, 0)]
    })

  def test_update_node_direted(self):
    graph = Graph(directed=True)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)

    graph.add_edge(1,2)
    graph.add_edge(2,1)
    graph.add_edge(3, 1)

    graph.update_node(1, 4)

    self.assertEqual(graph.nodes, {
      4: [(2, 0)],
      2: [(4, 0)],
      3: [(4, 0)],
    })
