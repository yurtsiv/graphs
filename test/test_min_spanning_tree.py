import unittest
from graph.graph import Graph
from graph.constants import MinSpanningTreeAlgs

class TestMinSpanningTree(unittest.TestCase):
  def setUp(self):
    graph = Graph(weighted=True)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 0)
    graph.add_edge(1, 5, 3)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 4, 5)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 5, 1)
    self.graph = graph

  def test_kruskal_algorithm(self):
    graph = Graph(directed=True)
    self.assertRaises(Exception, Graph.get_min_spanning_tree, MinSpanningTreeAlgs.Kruskal)


    spanning_tree = self.graph.get_min_spanning_tree(MinSpanningTreeAlgs.Kruskal)
    self.assertEqual(spanning_tree, [
      (3, 1, 0), (5, 4, 1), (4, 3, 2), (5, 2, 4)
    ])

  def test_prim_algorithm(self):
    spanning_tree = self.graph.get_min_spanning_tree(MinSpanningTreeAlgs.Prim)
    self.assertEqual(spanning_tree, [
      (1, 3, 0), (3, 4, 2), (4, 5, 1), (5, 2, 4)
    ])
