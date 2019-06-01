from enum import Enum

class MinSpanningTreeAlgs(Enum):
  Kruskal='Kruskal'
  Prim='Prim'

class ShortestPathAlgs(Enum):
  Dijkstra='Dijkstra'
  BellmanFord='BellmanFord'

class CycleDetectionAlgs(Enum):
  Kosaraju='Kosaraju'
  Tarjan='Tarjan'