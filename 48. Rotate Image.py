from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    s = Solution()
    matrix =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    s.rotate(matrix)
    print(matrix)
