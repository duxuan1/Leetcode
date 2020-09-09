from typing import List, Set

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        counter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    counter += 1
        return counter

    def dfs(self, grid, r, c):
        row, col = len(grid), len(grid[0])
        if r < 0 or r > row - 1 or c < 0 or c > col - 1 or grid[r][c] != "1":
            return
        grid[r][c] = "v" # mark as visited
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c + 1)
