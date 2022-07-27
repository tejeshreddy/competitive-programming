class Solution:
    def numOfWays(self, n: int) -> int:
        f = g = 6
        M = 10 ** 9 + 7
        for _ in range(n - 1):
            f, g = (2*f + 2*g) % M, (2*f + 3*g) % M
        return (f + g) % M
        