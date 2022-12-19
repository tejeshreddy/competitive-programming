class Solution:
    def __init__(self):
        self.hmap = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.hmap:
            return self.hmap[(m, n)]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        self.hmap[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return self.hmap[(m, n)]
        