import unittest
from graph.constants import CycleDetectionAlgs
from graph.graph import Graph

class TestCyclesDetection(unittest.TestCase):
  def setUp(self):
    graph = Graph(directed=True)

    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge(1, 2)
    graph.add_edge(3, 1)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)

    self.graph = graph

  def test_kosaraju_algorithm(self):
    self.assertFalse(self.graph.detect_cycles(CycleDetectionAlgs.Kosaraju))
    self.graph.add_edge(5, 3)
    self.assertTrue(self.graph.detect_cycles(CycleDetectionAlgs.Kosaraju))

