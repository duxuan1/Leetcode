class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x < 2 and y < 2:
            return 0
        step = 1
        move = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        visited = set()
        this, next = [[0, 0]], []
        while this:
            for i in this:
                for j in move:
                    sub = (i[0] + j[0], i[1] + j[1])
                    if sub[0] == x and sub[1] == y:
                        return step
                    if sub not in visited:
                        next.append(sub)
                        visited.add(sub)
            this, next = next, []
            step += 1


if __name__ == "__main__":
    s = Solution()
    ans = s.minKnightMoves(2, 112)
    print(ans)