from typing import List


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

    def bfs(self, start):
        visited = set()
        visited.add(start)
        queue = [start]
        res = set()
        while queue:
            root = queue.pop(0)
            res.add(root)
            for node in self.graph[root]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return res


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph()
        for i, j in prerequisites:
            g.addEdge(j, i)
        visited = set()
        return False
