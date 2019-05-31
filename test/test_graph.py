import unittest

from graph.graph import Graph

class TestGraphMethods(unittest.TestCase):
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

  def test_remove_node(self):
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