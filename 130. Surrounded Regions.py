from typing import List, Set


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        row, col = len(board), len(board[0])
        # find 'O's on the boundary, and dfs all 'O's that were connected
        for i in range(col):
            self.dfs(board, 0, i)
            self.dfs(board, row - 1, i)
        for j in range(row):
            self.dfs(board, j, 0)
            self.dfs(board, j, col - 1)
        # Set all 'B's to 'O', all 'O's to 'X'
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                if board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board: List[List[str]], r, c):
        row, col = len(board), len(board[0])
        if r < 0 or r > row - 1 or c < 0 or c > col - 1 or board[r][c] != 'O': return
        board[r][c] = 'B'
        self.dfs(board, r - 1, c)
        self.dfs(board, r + 1, c)
        self.dfs(board, r, c - 1)
        self.dfs(board, r, c + 1)


if __name__ == "__main__":
    s = Solution()
    b = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]
    s.solve(b)
    print(b)
