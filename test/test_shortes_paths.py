import unittest
import math
from graph.graph import Graph
from graph.constants import ShortestPathAlgs

class TestShortestPaths(unittest.TestCase):
  def setUp(self):
    directed_graph = Graph(weighted=True, directed=True)
    directed_graph.add_node(1)
    directed_graph.add_node(2)
    directed_graph.add_node(3)
    directed_graph.add_node(4)
    directed_graph.add_node(5)
    directed_graph.add_node(6)

    directed_graph.add_edge(1, 2, 50)
    directed_graph.add_edge(1, 3, 45)
    directed_graph.add_edge(1, 4, 10)
    directed_graph.add_edge(2, 3, 10)
    directed_graph.add_edge(2, 4, 15)
    directed_graph.add_edge(3, 5, 30)
    directed_graph.add_edge(4, 1, 50)
    directed_graph.add_edge(4, 5, 15)
    directed_graph.add_edge(5, 2, 20)
    directed_graph.add_edge(5, 3, 35)
    directed_graph.add_edge(6, 5, 35)

    self.directed_graph = directed_graph

  def test_dijkstra_shortest_path(self):
    shortest_paths = self.directed_graph.get_shortest_paths(
      1,
      ShortestPathAlgs.Dijkstra
    )

    self.assertEqual(shortest_paths, {
      1: 0,
      2: 45,
      3: 45,
      4: 10,
      5: 25,
      6: math.inf,
    })

    # algorithm doesnt work with negative weights
    self.directed_graph.add_edge(1, 5, -1)
    self.assertRaises(
      Exception,
      self.directed_graph.get_shortest_paths,
      1,
      ShortestPathAlgs.Dijkstra
    )

  def test_bellman_ford_shortest_path(self):
    shortest_paths = self.directed_graph.get_shortest_paths(
      1,
      ShortestPathAlgs.BellmanFord
    )

    self.assertEqual(shortest_paths, {
      1: 0,
      2: 45,
      3: 45,
      4: 10,
      5: 25,
      6: math.inf,
    })
