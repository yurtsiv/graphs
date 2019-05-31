import unittest

from graph.graph import Graph

class TestGraphMethods(unittest.TestCase):
  def test_add_node(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    self.assertEqual(len(graph.nodes), 2)
    self.assertEqual(graph.nodes[0].key, 1)
    self.assertEqual(graph.nodes[1].key, 2)
    self.assertRaises(Exception, Graph.add_node, 1)

  def test_add_edge_undirected(self):
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    self.assertEqual(graph.nodes[0].links[0][0].key, 2)
    self.assertEqual(graph.nodes[1].links[0][0].key, 1)
    self.assertRaises(Exception, Graph.add_edge, 0, 3)
  
  def test_add_edge_directed(self):
    graph = Graph(directed=True)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    self.assertEqual(graph.nodes[0].links[0][0].key, 2)
    self.assertEqual(graph.nodes[1].links, [])
