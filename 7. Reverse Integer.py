class Solution:
    def reverse(self, x: int) -> int:

        neg = False

        if x < 0:
            x *= -1
            neg = True

        s = str(x)[::-1]
        n = int(s)

        if neg:
            n *= -1

        if (abs(n) > (2 ** 31 - 1)):
            return 0

        return n
