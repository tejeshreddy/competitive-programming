class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        result = [0] * (n + 1)
        
        for i, j in trust:
            result[i] -= 1
            result[j] += 1
        
        for i in range(1, n + 1):
            if result[i] == n - 1:
                return i
        return -1