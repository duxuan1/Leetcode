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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = Graph()
        for u, v in edges:
            g.addEdge(u, v)
            g.addEdge(v, u)

        visited = set()
        count = 0
        for start in g.graph:
            if start not in visited:
                visit = g.bfs(start)
                visited.update(visit)
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    g = s.countComponents(4, [[2,3],[1,2],[1,3]])

