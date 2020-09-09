# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    # Constructor
    def __init__(self):
        # dictionary to store graph
        self.graph = {}

    # function to add an edge to graph
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pass