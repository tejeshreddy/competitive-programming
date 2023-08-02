class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(start, path, total):
            if len(path) == k:
                result.append(path)
                return
            
            for i in range(start, n):
                dfs(i + 1, path + [total[i]], total)
        
        dfs(0, [], [i for i in range(1, n + 1)])
        return result